Retail Sales Analysis: End-to-End Project (Python, SQL, Power BI)

An end-to-end analysis of the Superstore retail dataset (9,994 order lines, Jan 2011 to Dec 2014). The project covers data cleaning, exploratory analysis, SQL querying and a multi-page Power BI dashboard.

Dashboard Preview
Home (Sales Overview)	Sales Performance	Profit & Customers
Home	Sales Performance	Profit and Customers
Key Numbers
Metric	Value
Total Sales	$2.30M
Total Profit	$286.4K
Profit Margin	12.5%
Orders	5,009
Customers	793
Key Insights
Growth: Sales grew from $484K (2011) to $734K (2014). In 2014, sales were up about 20.6% and profit up about 14.4% compared with 2013.
Category: Technology earns the most profit ($145.5K). Furniture has $742K in sales but only $18.5K profit (about 2.5% margin).
Region: West leads with $108.4K profit. Central has the weakest margin (about 7.9%).
Loss-making products: Tables (-$17.7K), Bookcases (-$3.5K) and Supplies (-$1.2K) lose money overall.
Discounts: Orders with a discount of 30% or more are loss-making overall, so heavy discounting is hurting profit.
Project Workflow
Data cleaning (Python / pandas): checked nulls and duplicates, converted date columns, dropped Row ID, saved cleaned_sales_data.csv.
Statistics and visual analysis (Python / matplotlib): summary statistics, sales distribution, sales vs profit, profit by region, monthly trend.
SQL analysis (SQLite, DB Browser): loaded the cleaned data into retail_sales.db and queried it for sales and profit insights.
Dashboard (Power BI): 3-page report with page navigation, KPI cards with month-over-month and last-year comparison, and slicers.
Power BI Dashboard Features
Home: KPI cards (Sales, Profit, Orders, Avg Order Value, Customers) with MoM trend, Sales by Month, Category, Region, Top 5 Products and Sub-Category.
Sales Performance: Year-over-year monthly sales and profit, Ship Mode, Category and Sub-Category, Region and State slicers.
Profit & Customers: Total Customers, Profit, Profit %, Profit per Customer, Orders with last-year comparison, Top 5 Customers, Profit by Category and Sub-Category.
Custom DAX measures for MoM %, LY comparison, Profit %, New Customers.
Tech Stack

Python (pandas, matplotlib), SQL (SQLite), Power BI, DAX

Folder Structure
Retail-Sales-Analysis/
├── 01_Raw_Data/
│   └── Superstore.csv
├── 02_Python_Pandas/
│   ├── data_analysis.py
│   ├── statistics_analysis.py
│   ├── matplotlib_analysis.py
│   └── cleaned_sales_data.csv
├── SQL /
│   ├── retail_sales.db
│   └── sales_analysis_sql.sqbpro
├── 05_PowerBI/
│   └── dashboard.pbix
├── Images/
│   └── dashboard screenshots (.PNG)
└── Chart/
    └── retail_sales_dashboard.png
How to Run
Install dependencies: pip install pandas matplotlib
Run data_analysis.py to clean the raw data.
Run statistics_analysis.py and matplotlib_analysis.py for the analysis and charts.
Open retail_sales.db in DB Browser for SQLite to see the SQL queries.
Open dashboard.pbix in Power BI Desktop.
Data Source

Superstore sample dataset (public dataset, available on Kaggle).

Author
Amnan Zara LinkedIn:https://www.linkedin.com/in/aman-zara/
