import requests
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# 1. جلب البيانات من الـ API
url = "https://api.github.com/search/repositories?q=machine+learning&sort=stars&order=desc&per_page=100"
response = requests.get(url)
data = response.json()
items = data["items"]

# 2. تحويل البيانات وتنظيفها
df = pd.DataFrame(items)

selected_columns = [
    "name", "owner", "language", "stargazers_count",
    "forks_count", "watchers_count", "open_issues_count",
    "created_at", "updated_at", "license"
]
df = df[selected_columns]

df["owner"] = df["owner"].apply(lambda x: x.get("login") if x else None)
df["license"] = df["license"].apply(lambda x: x.get("name") if x else "No License")

df["language"] = df["language"].fillna("Unknown")
df["license"] = df["license"].fillna("No License")

df = df.drop_duplicates(subset=["name", "owner"])

df["created_at"] = pd.to_datetime(df["created_at"]).dt.date
df["updated_at"] = pd.to_datetime(df["updated_at"]).dt.date

rename_map = {
    "stargazers_count": "stars",
    "forks_count": "forks",
    "watchers_count": "watchers",
    "open_issues_count": "open_issues",
    "created_at": "created_date",
    "updated_at": "updated_date"
}
df = df.rename(columns=rename_map)

# حفظ ملف CSV
df.to_csv("github_projects.csv", index=False)

# 3. التخزين في قاعدة البيانات واستعلام SQL
conn = sqlite3.connect("github_data.db")
df.to_sql("Repositories", conn, if_exists="replace", index=False)

query_top10 = "SELECT name, stars FROM Repositories ORDER BY stars DESC LIMIT 10"
top10_df = pd.read_sql_query(query_top10, conn)
conn.close()

# 4. إنشاء الرسم البياني وحفظه
plt.figure(figsize=(12, 5))
plt.barh(top10_df["name"], top10_df["stars"], color="skyblue")
plt.title("Top 10 Most Popular Repositories")
plt.xlabel("Stars Count")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("chart_top10.png")

print("✓ تم إنشاء وتعبئة ملف main.py بنجاح")
