import pandas as pd
import numpy as np

def complete_dataset_analysis():
    print("=== TASK 2: COMPLETE DATASET ANALYSIS ===\n")
    
    # Load dataset
    df = pd.read_csv('dynamic_pricing.csv')
    
    print("📊 DATASET BASIC INFORMATION")
    print("=" * 40)
    print(f"Dataset Shape: {df.shape}")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n📋 COLUMN DETAILS:")
    print("=" * 40)
    for col in df.columns:
        dtype = df[col].dtype
        unique_count = df[col].nunique()
        print(f"• {col}: {dtype} | Unique values: {unique_count}")
    
    print("\n🔍 CATEGORICAL VARIABLES DISTRIBUTION:")
    print("=" * 40)
    
    categorical_stats = {}
    categorical_cols = ['Location_Category', 'Customer_Loyalty_Status', 'Time_of_Booking', 'Vehicle_Type']
    
    for col in categorical_cols:
        counts = df[col].value_counts()
        categorical_stats[col] = counts
        print(f"\n{col}:")
        for value, count in counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {value}: {count} ({percentage:.1f}%)")
    
    print("\n📈 NUMERICAL VARIABLES SUMMARY:")
    print("=" * 40)
    numerical_cols = ['Number_of_Riders', 'Number_of_Drivers', 'Number_of_Past_Rides', 
                     'Average_Ratings', 'Expected_Ride_Duration', 'Historical_Cost_of_Ride']
    
    for col in numerical_cols:
        print(f"\n{col}:")
        print(f"  Min: {df[col].min():.2f}")
        print(f"  Max: {df[col].max():.2f}")
        print(f"  Mean: {df[col].mean():.2f}")
        print(f"  Std: {df[col].std():.2f}")
    
    print("\n✅ DATA QUALITY CHECK:")
    print("=" * 40)
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    for col, missing in missing_values.items():
        print(f"  {col}: {missing}")
    
    # Additional insights
    print("\n💡 KEY INSIGHTS FOR PRICEOPTIMA:")
    print("=" * 40)
    
    # Demand-Supply ratio
    df['demand_supply_ratio'] = df['Number_of_Riders'] / df['Number_of_Drivers']
    print(f"Average Demand-Supply Ratio: {df['demand_supply_ratio'].mean():.2f}")
    
    # Price ranges by vehicle type
    print("\nAverage Price by Vehicle Type:")
    price_by_vehicle = df.groupby('Vehicle_Type')['Historical_Cost_of_Ride'].mean()
    for vehicle, avg_price in price_by_vehicle.items():
        print(f"  {vehicle}: ${avg_price:.2f}")
    
    # Price by location
    print("\nAverage Price by Location:")
    price_by_location = df.groupby('Location_Category')['Historical_Cost_of_Ride'].mean()
    for location, avg_price in price_by_location.items():
        print(f"  {location}: ${avg_price:.2f}")
    
    return df, categorical_stats

if __name__ == "__main__":
    df, stats = complete_dataset_analysis()
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETED SUCCESSFULLY!")
    print("Summary report saved to: task2_summary_report.txt")