import pandas as pd

try:
    df = pd.read_csv("sales_data.csv")
    print("Sales data loaded successfully!\n")
except FileNotFoundError:
    print("sales_data.csv not found! Please make sure it is in the same folder.")
    exit()

print("First 5 Rows of Data:")
print(df.head(), "\n")

print("Dataset Info:")
print(df.info(), "\n")

print("Missing Values:")
print(df.isnull().sum(), "\n")

print("Summary Statistics:")
print(df.describe())


print("\nCleaning & Formatting Data...\n")

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df.dropna(subset=['Date', 'Region', 'Product', 'Sales', 'Quantity'])

df = df.drop_duplicates()

df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

df = df.dropna(subset=['Sales', 'Quantity'])

df.reset_index(drop=True, inplace=True)

print("Data cleaned successfully!")
print(f"Total rows after cleaning: {len(df)}")
print("\nSample of Cleaned Data:")
print(df.head())


print("\n📊 ANALYZING SALES DATA...\n")

total_sales = df['Sales'].sum()
total_quantity = df['Quantity'].sum()
print(f"💰 Total Sales: {total_sales}")
print(f"📦 Total Quantity Sold: {total_quantity}\n")

print("🏙️ Sales by Region:")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales, "\n")

print("🍎 Sales by Product:")
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print(product_sales, "\n")

print("📅 Daily Sales Trend:")
daily_sales = df.groupby('Date')['Sales'].sum()
print(daily_sales, "\n")

top_product = product_sales.idxmax()
top_product_sales = product_sales.max()
print(f"🏆 Top Product: {top_product} with Sales: {top_product_sales}\n")

df.to_csv("cleaned_sales_data.csv", index=False)
print("✅ Cleaned data exported to 'cleaned_sales_data.csv'")