# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 16:38:10 2025

@author:DHRUV KAUSHIK
"""

import pandas as pd
import numpy as np

# Load the dataset
file_path = r"C:\Users\DELL\Desktop\data sets\ECOMMERCE\Ecommerc data set.csv" 
# Ensure this path is correct in your local environment
df = pd.read_csv(file_path)

# --- 1. CRITICAL TIME PARSING ---
# The format 'HH:MM.S' is unusual. We assume the first part is the hour (HH)
# which is crucial for analyzing peak demand.
df['Order Hour'] = df['Order Date & Time'].str.split(':').str[0].astype(int)

# --- 2. BINARY CONVERSION FOR DAX USE ---
# Convert 'Yes'/'No' string columns to binary (1/0) flags
df['Delay Flag'] = np.where(df['Delivery Delay'] == 'Yes', 1, 0)
df['Refund Flag'] = np.where(df['Refund Requested'] == 'Yes', 1, 0)

# --- 3. TEXT STANDARDIZATION ---
df['Product Category'] = df['Product Category'].str.title()
df['Customer Feedback'] = df['Customer Feedback'].str.strip()
 # Remove leading/trailing spaces
print(df)

# Save the cleaned dataset for Power BI
df.to_csv(r"C:\Users\DELL\Desktop\data sets\ECOMMERCE\ecom_cleaned_for_dashboard.csv", index=False)
print("\nCleaned data exported to 'ecom_cleaned_for_dashboard.csv'")
