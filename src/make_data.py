"""Генерация учебного датасета «Квартиры» (data/housing.csv).

Данные синтетические: цена считается по формуле + случайный шум, затем в данные
намеренно добавляются «дефекты» (пропуски, выбросы, дубликаты), как требует ПР-2.
Запуск:  python src/make_data.py
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 1000

district = rng.choice(["Центр", "Север", "Юг", "Восток"], n, p=[.2, .3, .25, .25])
dist_mean = pd.Series(district).map({"Центр": 2, "Север": 8, "Юг": 7, "Восток": 10}).values
dist_km = np.clip(rng.normal(dist_mean, 2.5), 0.3, None).round(1)
area = np.clip(np.exp(rng.normal(np.log(60), 0.35, n)), 20, 250).round(1)
rooms = np.clip(np.round(area / 25 + rng.normal(0, 0.5, n)), 1, 6).astype(int)
floor = rng.integers(1, 17, n)
year = rng.integers(1960, 2025, n)
condition = rng.choice(["требует ремонта", "хороший", "новый"], n, p=[.25, .5, .25])
balcony = rng.choice(["да", "нет"], n, p=[.6, .4])

price = (15 + 1.15 * area - 0.9 * dist_km + 0.12 * (year - 1960) + 0.3 * floor
         + pd.Series(district).map({"Центр": 25, "Север": 0, "Юг": 5, "Восток": -5}).values
         + pd.Series(condition).map({"требует ремонта": -15, "хороший": 0, "новый": 12}).values
         + np.where(balcony == "да", 3, 0) + rng.normal(0, 10, n))
price = np.clip(price, 10, None).round(1)

df = pd.DataFrame({
    "area_m2": area,
    "living_area_m2": (area * 0.72 + rng.normal(0, 3, n)).round(1),   # почти дублирует area_m2
    "area_sqft": (area * 10.764 + rng.normal(0, 2, n)).round(0),      # та же площадь в футах
    "rooms": rooms, "floor": floor, "year_built": year.astype(float),
    "dist_center_km": dist_km, "district": district, "condition": condition,
    "balcony": balcony, "price_kusd": price,
})
df["floor"] = df["floor"].astype(float)

# --- дефекты ---
for col, share in [("year_built", .08), ("dist_center_km", .05), ("district", .06),
                   ("condition", .10), ("area_m2", .03), ("floor", .03)]:
    df.loc[rng.choice(n, int(n * share), replace=False), col] = np.nan
df.loc[rng.choice(n, 6, replace=False), "area_m2"] = rng.choice([650, 720, 880, 990], 6)  # опечатки
df.loc[rng.choice(n, 3, replace=False), "year_built"] = [2099, 1800, 1850]               # невозможные годы
df = pd.concat([df, df.sample(10, random_state=1)], ignore_index=True)                   # дубликаты
df = df.sample(frac=1, random_state=7).reset_index(drop=True)
df.to_csv("data/housing.csv", index=False, encoding="utf-8")
print("Сохранено:", df.shape)
