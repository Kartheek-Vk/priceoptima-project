import pandas as pd
import numpy as np

print("=== BASIC PANDAS OPERATIONS DEMONSTRATION ===\n")

# 1. Create a simple dataset
print("1. CREATING A SAMPLE DATASET")
data = {
    'Product_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 
                    'Webcam', 'Tablet', 'Smartphone', 'Printer', 'Speaker'],
    'Price': [999.99, 25.50, 75.00, 299.99, 89.99, 45.00, 399.99, 699.99, 149.99, 79.99],
    'Quantity_Sold': [45, 120, 85, 30, 95, 65, 55, 75, 40, 60],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 
                'Audio', 'Accessories', 'Electronics', 'Electronics', 'Office', 'Audio']
}

# Create DataFrame
df = pd.DataFrame(data)
print("DataFrame created successfully!")
print(f"Shape of DataFrame: {df.shape}\n")

# 2. Using head() method
print("2. USING head() METHOD")
print("First 5 rows using head():")
print(df.head())
print("\nFirst 3 rows using head(3):")
print(df.head(3))

# 3. Using tail() method
print("\n3. USING tail() METHOD")
print("Last 5 rows using tail():")
print(df.tail())
print("\nLast 3 rows using tail(3):")
print(df.tail(3))

# 4. Basic DataFrame information
print("\n4. BASIC DATAFRAME INFO")
print("DataFrame columns:")
print(df.columns)
print("\nData types:")
print(df.dtypes)
print("\nBasic statistics:")
print(df.describe())

# 5. Accessing specific columns
print("\n5. ACCESSING COLUMNS")
print("Product names column:")
print(df['Product_Name'].head())
print("\nPrice column:")
print(df['Price'].head())

# 6. Basic filtering
print("\n6. BASIC FILTERING")
print("Electronics products:")
electronics = df[df['Category'] == 'Electronics']
print(electronics.head())

# 7. Sorting operations
print("\n7. SORTING OPERATIONS")
print("Sorted by Price (ascending):")
print(df.sort_values('Price').head())
print("\nSorted by Quantity_Sold (descending):")
print(df.sort_values('Quantity_Sold', ascending=False).head())

print("\n" + "="*50)
print("BASIC PANDAS OPERATIONS COMPLETED SUCCESSFULLY!")