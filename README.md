# Машинное обучение — практические работы

**Студент:** Акматов Элдар Аскарович

Репозиторий содержит практические работы № 1–7 по машинному обучению на Python (уровень сложности B).

## Практические работы

| Работа | Тема | Основные технологии | Ноутбук |
|--------|------|---------------------|---------|
| PR1 | Настройка окружения и первичный анализ данных | Pandas, NumPy, Matplotlib | `PR1_environment.ipynb` |
| PR2 | Разведочный анализ данных (EDA) | Pandas, Matplotlib, Seaborn | `PR2_EDA.ipynb` |
| PR3 | Пайплайн предобработки данных | Scikit-learn, Pipeline, ColumnTransformer | `PR3_preprocessing.ipynb` |
| PR4 | Линейная регрессия, мультиколлинеарность (VIF) | Scikit-learn, Pandas, Matplotlib | `PR4_regression.ipynb` |
| PR5 | Классификация, метрики, подбор порога | Logistic Regression, Scikit-learn | `PR5_classification.ipynb` |
| PR6 | Классификация текстов | TF-IDF, Naive Bayes, Scikit-learn | `PR6_text_classification.ipynb` |
| PR7 | Случайный лес | Random Forest, GridSearchCV, Scikit-learn | `PR7_random_forest.ipynb` |

## Структура проекта

**Все практические работы выполнены в одном проекте и лежат в одной папке `notebooks/`** — отдельных папок под каждую работу (pr1, pr2 и т. д.) нет. Данные и общий код вынесены в отдельные папки, чтобы все ноутбуки использовали их совместно:

```
ml-practice/
├── README.md
├── requirements.txt
├── .gitignore
├── data/                 # наборы данных (housing.csv, reviews.csv)
├── notebooks/            # все 7 практических работ (PR1 … PR7)
└── src/                  # общий код: preprocessing.py и скрипты генерации данных
```

Такая структура удобнее: пайплайн предобработки из `src/preprocessing.py` написан один раз и используется в ПР-4 и ПР-7, а ноутбуки читают данные из общей папки `data/` по относительным путям.

## Данные

- `housing.csv` и `reviews.csv` — синтетические учебные данные (создаются скриптами из `src/`), в которые намеренно добавлены пропуски, выбросы и дубликаты.
- В ПР-5 используется встроенный датасет `breast_cancer` из scikit-learn.

## Как запустить

1. Склонировать репозиторий.
2. Создать виртуальное окружение и установить библиотеки.
3. Открыть нужный `.ipynb` в Jupyter Notebook или Visual Studio Code.
4. Выполнить ячейки ноутбука по порядку.

```
git clone https://github.com/searchers1221-lang/ml-su-course3.git
cd ml-su-course3
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook
```
