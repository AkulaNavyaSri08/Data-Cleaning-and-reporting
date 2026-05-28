import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# =====================================
# DISPLAY ORIGINAL DATA
# =====================================

print("========== ORIGINAL DATA ==========")
print(df)

# =====================================
# DATA CLEANING
# =====================================

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Revenue values
df['Revenue'] = df['Revenue'].fillna(
    df['Quantity'] * df['UnitPrice']
)

# Fill missing Customer Rating values
df['CustomerRating'] = df['CustomerRating'].fillna(
    df['CustomerRating'].mean()
)

# Fill missing Payment Method values
df['PaymentMethod'] = df['PaymentMethod'].fillna("Unknown")

# Standardize Region names
df['Region'] = df['Region'].str.upper()

# Convert OrderDate column to datetime format
df['OrderDate'] = pd.to_datetime(
    df['OrderDate'],
    dayfirst=True
)

# =====================================
# DISPLAY CLEANED DATA
# =====================================

print("\n========== CLEANED DATA ==========")
print(df)

# =====================================
# SAVE CLEANED DATA
# =====================================

df.to_csv("cleaned_sales_data.csv", index=False)

# =====================================
# REPORT GENERATION
# =====================================

# Revenue by Region
region_report = df.groupby('Region')['Revenue'].sum()

print("\n========== REVENUE BY REGION ==========")
print(region_report)

# Revenue by Product
product_report = df.groupby('Product')['Revenue'].sum()

print("\n========== REVENUE BY PRODUCT ==========")
print(product_report)

# Save reports into Excel file
with pd.ExcelWriter("sales_report.xlsx") as writer:
    
    # Cleaned data sheet
    df.to_excel(writer,
                sheet_name="Cleaned_Data",
                index=False)

    # Region report sheet
    region_report.to_excel(writer,
                           sheet_name="Region_Report")

    # Product report sheet
    product_report.to_excel(writer,
                            sheet_name="Product_Report")

# =====================================
# CHART CREATION
# =====================================

# Bar chart for Revenue by Region
region_report.plot(kind='bar')

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

# Save chart image
plt.savefig("revenue_by_region.png")

# Display chart
plt.show()

print("\nAutomation Completed Successfully!")