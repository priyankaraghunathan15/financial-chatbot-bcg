
# 💬 AI-Powered Financial Chatbot (BCG GenAI Prototype)

This repository contains a dynamic financial analysis chatbot developed as part of a consulting simulation at **Boston Consulting Group (BCG)** within the **GenAI Consulting Team**. The chatbot analyzes financial data from 10-K filings for Apple, Microsoft, and Tesla (2022–2024) and responds to natural language queries with accurate, data-driven insights.

<p align="center">
  <img src="images/bcg.png" alt="BCG Image" width="700"/>
</p>


---

## 🧠 Project Context

Global Finance Corp. (GFC), a leading financial institution, has partnered with BCG to modernize their approach to analyzing corporate financial performance. As part of the GenAI Consulting team, this prototype was developed to showcase how conversational AI can make 10-K and 10-Q financial reports more accessible, faster to interpret, and easier to scale.

---

## 🎯 Objectives

- Extract and analyze 10-K data for Apple, Microsoft, and Tesla (2022–2024).
- Develop a Flask-based chatbot capable of responding to financial queries.
- Apply rule-based logic to compute metrics like revenue, ROA, ROE, and profit margin.
- Provide a clean and intuitive interface suitable for use by financial analysts and non-experts.

---

## 🗃️ Data Extraction

Financial metrics were manually extracted from SEC EDGAR 10-K filings:
- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Cash Flow from Operating Activities

Stored in: `Company_Financial_data_2022_2024.csv`

---

## ⚙️ Technologies Used

- **Python**
- **Pandas** – for financial data handling and trend analysis
- **Flask** – to build the web-based chatbot
- **Jupyter Notebook** – for initial data exploration and trend summaries
- **HTML/CSS (inline)** – for chatbot UI styling

---

## 🤖 Features

- Accepts user queries in natural language (e.g. "What is Tesla's ROE in 2024?")
- Calculates:
  - Revenue
  - Net Income / Profit
  - Profit Margin
  - ROA (Return on Assets)
  - ROE (Return on Equity)
- Dynamically responds using real financial data
- Simple, clean UI powered by Flask

---

## 💬 Sample Supported Queries

| Example Query                                 | Interpreted As                     |
|----------------------------------------------|------------------------------------|
| `What is Apple’s revenue in 2024?`           | Total Revenue                      |
| `How much profit did Tesla make in 2023?`    | Net Income                         |
| `Show Microsoft’s profit margin in 2022`     | Profit Margin = Net Income / Revenue |
| `What’s Tesla’s ROA in 2024?`                | Return on Assets                   |
| `Give me ROE for Apple 2023`                 | Return on Equity = Net Income / (Assets - Liabilities) |

---

## 🚧 Limitations

- Currently supports only **Apple**, **Microsoft**, and **Tesla**
- Limited to **2022–2024** fiscal years
- Uses keyword matching (rule-based NLP)
- Not integrated with live SEC API or document parsing tools

---

## 📂 Repository Structure

```
├── app_dynamic.py                  # Flask chatbot with dynamic financial logic
├── Company_Financial_data_2022_2024.csv  # Cleaned financial dataset (manual extraction)
├── financial_analysis.ipynb        # Jupyter notebook with trend analysis
├── README.md                       # Project documentation
```

---

## 📈 Insights from Data

In `financial_analysis.ipynb`, we used pandas to:
- Calculate YoY growth in revenue and net income
- Identify performance trends by company
- Prepare metrics for chatbot logic

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/priyankaraghunathan15/financial-chatbot-bcg.git
cd financial-chatbot-bcg
```

2. Install dependencies:
```bash
pip install flask pandas
```

3. Run the chatbot:
```bash
python app_dynamic.py
```

4. Open browser and go to:
```
http://127.0.0.1:5000
```

---

## 🏁 Outcome

This project demonstrates how GenAI concepts can be applied in finance consulting to:
- Automate financial document interpretation
- Deliver insights interactively
- Improve speed and scalability in client-facing tools

---


