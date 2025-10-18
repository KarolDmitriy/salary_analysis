import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Пути
DATA_PATH = Path("data/salaries.csv")
OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)

# Загрузка данных
df = pd.read_csv(DATA_PATH)

# Анализ
avg_salary = df["salary"].mean()
max_salary = df.loc[df["salary"].idxmax()]
min_salary = df.loc[df["salary"].idxmin()]

print(f"Средняя зарплата по регионам: {avg_salary:.0f} ₽")
print(f"Максимальная: {max_salary['region']} — {max_salary['salary']} ₽")
print(f"Минимальная: {min_salary['region']} — {min_salary['salary']} ₽")

# Сохранение в Excel
output_excel = OUTPUT_PATH / "results.xlsx"
df.to_excel(output_excel, index=False)

# Построение графика
plt.figure(figsize=(10, 6))
plt.barh(df["region"], df["salary"])
plt.title("Средние зарплаты по регионам РФ")
plt.xlabel("₽ в месяц")
plt.tight_layout()

# Сохранение графика
output_chart = OUTPUT_PATH / "charts.png"
plt.savefig(output_chart)
plt.show()
