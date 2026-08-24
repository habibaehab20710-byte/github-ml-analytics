# 📊 GitHub Machine Learning Repositories Analytics

An end-to-end data analytics project that collects, cleans, analyzes, and visualizes real-world data from top Machine Learning repositories using GitHub REST API, Pandas, SQLite, and Matplotlib.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Workflow & Methodology](#workflow--methodology)
- [Key Insights & Findings](#key-insights--findings)

---

## 🎯 Project Overview
The main goal of this project is to explore Machine Learning repositories available on GitHub to understand their popularity, programming language distribution, and activity over time.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Collection:** `requests` (GitHub REST API)
- **Data Manipulation:** `pandas`
- **Database:** `SQLite`
- **Visualization:** `matplotlib`
- **Version Control:** Git & GitHub

---

## 🔄 Workflow & Methodology
1. **Data Collection & Cleaning (Task 1):** Pulled repository data via API, parsed nested values (`owner`, `license`), dropped duplicates, handled missing values, and saved data to `github_projects.csv`.
2. **Database & SQL Queries (Task 2):** Imported clean data into SQLite, queried key metrics using `AND`/`OR`/`NOT`, `GROUP BY`, `HAVING`, and sorted the top 10 repositories.
3. **Visualization & Insights:** Generated horizontal bar charts and line charts using `matplotlib` to highlight top projects and creation trends over time.

---

## 💡 Key Insights & Findings
- **Dominant Languages:** Python represents the vast majority among top-rated machine learning repositories.
- **Popularity Factors:** Top-starred projects belong to established open-source frameworks (e.g., TensorFlow, PyTorch).
- **Activity Trends:** Historical creation dates show consistent growth matching the rise in machine learning adoption.
