import pandas as pd
import numpy as np

df = pd.read_csv("ecommerce.csv")

print("E-COMMERCE DATASET")
print(df)

df["Revenue"] = df["Price"] * df["Quantity"] * (1 - df["Discount"] / 100)

print("\nRevenue Added")
print(df)

total_revenue = df["Revenue"].sum()
print("\nTotal Revenue")
print(total_revenue)

print("\nMost Popular Products")
popular = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print(popular)

print("\nCategory Revenue")
category = df.groupby("Category")["Revenue"].sum()
print(category)

print("\nCustomer Spending")
customer = df.groupby("Customer_Name")["Revenue"].sum()
print(customer)

print("\nCustomer Segments")
for name, amount in customer.items():
    if amount >= 100000:
        segment = "Premium"
    elif amount >= 50000:
        segment = "Gold"
    else:
        segment = "Regular"
    print(name, "->", segment)

print("\nRepeat Customers")
repeat = df["Customer_Name"].value_counts()
print(repeat[repeat > 1])

print("\nRevenue by Discount")
discount = df.groupby("Discount")["Revenue"].sum()
print(discount)

print("\nTop Customers")
print(customer.sort_values(ascending=False).head())

print("\nStatistics")
print("Average Revenue:", np.mean(df["Revenue"]))
print("Maximum Revenue:", np.max(df["Revenue"]))
print("Minimum Revenue:", np.min(df["Revenue"]))
print("Median Revenue:", np.median(df["Revenue"]))
print("Standard Deviation:", np.std(df["Revenue"]))
