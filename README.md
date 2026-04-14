# 🤖 AI Data Cleaning Agent

An **interactive, heuristic-based AI agent** that automates data preprocessing tasks such as handling missing values, removing duplicates, detecting outliers, and generating explainable cleaning reports.

---

## 🚀 Project Overview

This project demonstrates a modular **AI agent architecture** designed for intelligent data preprocessing. The agent analyzes raw datasets and applies rule-based (heuristic) decisions to improve data quality.

### 🧠 Agent Architecture

* **Perception Layer** → Profiles dataset (missing values, data types, distribution)
* **Decision Layer** → Applies heuristic rules
* **Action Layer** → Executes cleaning operations
* **Memory Layer** → Logs decisions for explainability

---

## 📊 Features

* 📂 Upload CSV dataset via web UI
* 📈 Automatic data profiling
* ⚙️ Heuristic-based decision making
* 🧹 Data cleaning:

  * Missing value handling
  * Duplicate removal
  * Outlier detection (IQR method)
  * Low-variance column removal
* 📊 Before vs After metrics dashboard
* 🧠 Explainable logs (what & why)
* ⬇ Download cleaned dataset

---

## 🏗️ Project Structure

```bash
project/
│
├── agent.py        # Core AI agent logic
├── app.py          # Streamlit UI
├── utils.py        # Helper functions (metrics)
├── requirements.txt
├── README.md
└── data/
    └── sample.csv  # Sample dataset
```

---

## ⚙️ Tech Stack

* Python
* Pandas
* NumPy
* Streamlit

---

## ▶️ How to Run Locally

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Application

```bash
streamlit run app.py
```

---

## 📊 Example Workflow

1. Upload dataset (CSV)
2. Click **Run Agent**
3. View:

   * Before vs After metrics
   * Cleaned dataset preview
   * Decision logs
4. Download cleaned dataset

---

## 🧪 Heuristic Rules Implemented

* Drop columns with >30% missing values
* Fill numeric columns using mean
* Fill categorical columns using mode
* Remove duplicate rows
* Detect & cap outliers using IQR method
* Drop low-variance columns

---

## 📈 Metrics Tracked

* Number of rows & columns
* Total missing values
* Duplicate rows
* Data quality improvement

---

## 🌐 Deployment

Deployed using **Streamlit Community Cloud** for real-time access.

---

## 📌 Dataset

* Includes datasets with:

  * Missing values
  * Outliers
  * Duplicate rows
  * Mixed data types

---

## 🎯 Resume Description

> Built a heuristic-based AI data cleaning agent with modular architecture, enabling automated preprocessing, explainable decision-making, and real-time data quality visualization via an interactive Streamlit interface.

---

## 🚀 Future Improvements

* Add advanced visualizations (charts/graphs)
* Support Excel & JSON formats
* User-configurable heuristics via UI
* Integration with ML pipelines

---

## 👨‍💻 Author

* Purna Chandra Rao

---
