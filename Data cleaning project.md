# Data Cleaning & Reporting Automation

## Project Overview
This project automates data cleaning and reporting workflows using Python.  
The system processes raw sales data, handles missing values, removes duplicates, standardizes inconsistent data, and generates automated reports with charts.

---
<a href="https://github.com/AkulaNavyaSri08/Data-Cleaning-and-reporting/blob/main/sales_data.csv>dataset view</a>
## Features

- Remove duplicate records
- Handle missing values automatically
- Standardize inconsistent text data
- Generate automated Excel reports
- Create revenue visualization charts
- Export cleaned datasets

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Microsoft Excel

---
<a href="https://github.com/AkulaNavyaSri08/Data-Cleaning-and-reporting/blob/main/data_cleaning.pyhttps://github.com/AkulaNavyaSri08/Data-Cleaning-and-reporting/blob/main/data_cleaning.py>data cleaning</a>

## Project Structure

Data-Cleaning-Automation/
│
├── sales_data.csv
├── cleaned_sales_data.csv
├── sales_report.xlsx
├── revenue_by_region.png
├── data_cleaning.py
└── README.md

---

## Dataset Information

The dataset contains:
- Customer details
- Product information
- Region data
- Revenue values
- Payment methods
- Customer ratings

The dataset intentionally includes:
- Missing values
- Duplicate records
- Inconsistent text formatting

to demonstrate real-world data cleaning techniques.

---

## Data Cleaning Operations

### 1. Duplicate Removal
Removes repeated rows from the dataset.

### 2. Missing Value Handling
- Fills missing Revenue values
- Fills missing Customer Ratings
- Handles missing Payment Methods

### 3. Data Standardization
Converts inconsistent region names such as:
- south
- South
- EAST

into a standardized format.

### 4. Date Formatting
Converts OrderDate into proper datetime format.

---
<a href="https://github.com/AkulaNavyaSri08/Data-Cleaning-and-reporting/blob/main/cleaned_sales_data.csv>cleaned sales data</a>
## Report Generation

The project automatically generates:

- Revenue by Region Report
- Revenue by Product Report
- Cleaned Dataset Export
- Excel Summary Report
- Revenue Bar Chart

---
<a href="https://github.com/AkulaNavyaSri08/Data-Cleaning-and-reporting/blob/main/sales_report.xlsx>sales report</a>
<img width="640" height="480" alt="revenue_by_region" src="https://github.com/user-attachments/assets/885c96a2-a124-401e-9fbc-7419cd1eaf19" />

## Installation

### Install Required Libraries

```bash
pip install pandas matplotlib openpyxl
