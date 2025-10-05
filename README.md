🏦 Bank Risk Analytics Dashboard
Problem Statement

The goal of this project was to develop a fundamental understanding of risk analytics in banking and financial services. The objective was to explore how data can be used to minimize the risk of financial loss while lending to customers by identifying potential high-risk applicants through data-driven insights.

Solution

A series of interactive dashboards were created using Power BI to help banks make more informed lending decisions.
The dashboards analyze applicant profiles and risk factors to determine whether a customer is likely to repay a loan or default.
This allows the company to approve or reject loans confidently, based on key financial indicators such as income, credit card balance, risk weighting, and savings.

About the Dataset

The dataset contains detailed information about banking relationships and client demographics. It consists of multiple interlinked tables connected through primary and foreign keys, including:

Banking Relationship

Client-Banking

Gender

Investment Advisor

Period

The dataset covers a wide range of client and financial information, including:

Estimated income, savings, deposits, loans, and credit card balances

Occupation, nationality, loyalty classification, and risk weighting

Various account details such as checking, savings, and business lending accounts

Data Cleaning and Preparation

The dataset underwent comprehensive data cleaning and preprocessing before visualization:

Handled missing and inconsistent values to ensure data reliability.

Converted date columns like Joined Bank into proper datetime format for accurate analysis.

Created a new column called “Engagement Timeframe” in the Client-Banking table to measure how long each client has been associated with the bank.

Categorized customers into Income Bands (Low, Medium, High) based on their estimated income to make comparisons easier across different financial levels.

Removed unnecessary duplicates and ensured relationships between tables were properly mapped using primary and foreign keys.

Exploratory Data Analysis (EDA)

A detailed exploratory analysis was conducted to understand data distribution and relationships between variables.
Key insights were derived by analyzing:

Income Band Distribution and its relation to loan eligibility.

Risk Weighting Patterns across different occupations and nationalities.

Credit and Deposit Trends across gender and loyalty classifications.

Correlation Analysis to identify strong relationships between financial factors such as income, savings, and loan amounts.

These insights helped in identifying which customer segments were more likely to pose financial risks to the bank.

Power BI Dashboard

The cleaned and analyzed data was visualized through interactive dashboards in Power BI, featuring:

Risk segmentation by income and occupation.

Customer portfolio breakdown by gender, nationality, and loyalty classification.

Insights into deposits, loans, and savings distribution.

Visualization of high-risk vs low-risk customers.

Performance tracking of banking relationships over time.

These dashboards enable management to quickly assess customer risk, monitor financial health, and make data-driven lending decisions.

Tools & Technologies

Power BI – Dashboard creation and interactive visual analytics

Python (Pandas, NumPy, Matplotlib, Seaborn) – Data cleaning and exploratory data analysis

MySQL – Database management and relational modeling

Outcome

This project successfully demonstrates how data analytics can strengthen risk management in the banking sector.
By integrating Power BI with data-driven insights, the organization can now:

Identify potential high-risk applicants before loan approval.

Improve decision-making accuracy.

Reduce financial losses by leveraging predictive and visual insights.
