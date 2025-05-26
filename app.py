
from flask import Flask, render_template_string, request
import pandas as pd
import re

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("Company_Financial_data_2022_2024.csv")

def format_query_nicely(text):
    words = text.title().split()
    abbreviations = {'ROE', 'ROA', 'CEO', 'CFO'}
    return ' '.join([word.upper() if word.upper() in abbreviations else word for word in words])

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Financial Chatbot</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f6f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .chatbox {
            background-color: white;
            padding: 30px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 500px;
        }
        h2 {
            text-align: center;
            color: #2e3a59;
        }
        label {
            display: block;
            margin-top: 20px;
            font-weight: 500;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px 12px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 15px;
        }
        input[type="submit"] {
            margin-top: 25px;
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
            width: 100%;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .response-box {
            margin-top: 30px;
            background-color: #eaf4ff;
            padding: 15px 20px;
            border-left: 4px solid #2196F3;
            border-radius: 6px;
            font-size: 15px;
        }
    </style>
</head>
<body>
    <div class="chatbox">
        <h2>Financial Chatbot</h2>
        <form method="post">
            <label for="company">Enter Company (Apple, Microsoft, Tesla):</label>
            <input type="text" name="company" required value="{{ company }}">
            <label for="query">Ask your financial question:</label>
            <input type="text" name="query" required value="{{ query }}">
            <input type="submit" value="Ask">
        </form>
        {% if response %}
        <div class="response-box">
            <strong>Response:</strong><br>
            {{ response }}
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    response = None
    company = ""
    query = ""

    if request.method == 'POST':
        original_company = request.form['company'].strip()
        company = original_company.lower()
        formatted_company = original_company.title()

        original_query = request.form['query'].strip()
        query = original_query.lower()
        formatted_query = format_query_nicely(original_query)

        year_match = re.search(r'\b\d{4}\b', query)
        year = int(year_match.group()) if year_match else 2024
        valid_years = {2022, 2023, 2024}

        if year not in valid_years:
            response = f"Sorry, I only have data for {formatted_company} in 2022, 2023, or 2024."
            return render_template_string(HTML_TEMPLATE, response=response, company=formatted_company, query=formatted_query)

        match = df[(df['Company Name'].str.lower() == company) & (df['Fiscal Year'] == year)]

        if match.empty:
            response = f"Sorry, I don't have data for {formatted_company} in {year}."
        else:
            row = match.iloc[0]
            if "revenue" in query:
                response = f"The total revenue for {formatted_company} in {year} is ${int(row['Total Revenue (USD)']):,}."
            elif "net income" in query or "profit" in query:
                response = f"The net income for {formatted_company} in {year} is ${int(row['Net Income (USD)']):,}."
            elif "profit margin" in query:
                margin = row['Net Income (USD)'] / row['Total Revenue (USD)'] * 100
                response = f"The profit margin for {formatted_company} in {year} is {margin:.2f}%."
            elif "roa" in query or "return on assets" in query:
                roa = row['Net Income (USD)'] / row['Total Assets (USD)'] * 100
                response = f"The Return on Assets (ROA) for {formatted_company} in {year} is {roa:.2f}%."
            elif "roe" in query or "return on equity" in query:
                equity = row['Total Assets (USD)'] - row['Total Liabilities (USD)']
                roe = row['Net Income (USD)'] / equity * 100 if equity != 0 else 0
                response = f"The Return on Equity (ROE) for {formatted_company} in {year} is {roe:.2f}%."
            else:
                response = "Sorry, I couldn't understand your question. Try asking about revenue, net income, profit margin, ROA, or ROE."

        return render_template_string(HTML_TEMPLATE, response=response, company=formatted_company, query=formatted_query)

    return render_template_string(HTML_TEMPLATE, response=response, company=company, query=query)

if __name__ == '__main__':
    app.run(debug=True)
