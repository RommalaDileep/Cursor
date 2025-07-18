#!/usr/bin/env python3
"""
Examples of creating tables in Python using different methods
"""

# Method 1: Using pandas DataFrame (most common for data analysis)
import pandas as pd

def create_pandas_table():
    """Create a table using pandas DataFrame"""
    print("=== Method 1: Pandas DataFrame ===")
    
    # Create table from dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'London', 'Tokyo', 'Paris'],
        'Salary': [50000, 60000, 75000, 55000]
    }
    
    df = pd.DataFrame(data)
    print(df)
    print("\nWith custom index:")
    df.index = ['Employee1', 'Employee2', 'Employee3', 'Employee4']
    print(df)
    return df

# Method 2: Using tabulate library for formatted tables
from tabulate import tabulate

def create_tabulate_table():
    """Create a formatted table using tabulate"""
    print("\n=== Method 2: Tabulate Library ===")
    
    # Table data as list of lists
    table_data = [
        ['Alice', 25, 'New York', 50000],
        ['Bob', 30, 'London', 60000],
        ['Charlie', 35, 'Tokyo', 75000],
        ['Diana', 28, 'Paris', 55000]
    ]
    
    headers = ['Name', 'Age', 'City', 'Salary']
    
    # Different table formats
    print("Grid format:")
    print(tabulate(table_data, headers=headers, tablefmt='grid'))
    
    print("\nFancy grid format:")
    print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))
    
    print("\nMarkdown format:")
    print(tabulate(table_data, headers=headers, tablefmt='pipe'))

# Method 3: Using basic Python data structures
def create_basic_table():
    """Create a table using basic Python lists and dictionaries"""
    print("\n=== Method 3: Basic Python Structures ===")
    
    # Table as list of dictionaries
    table = [
        {'Name': 'Alice', 'Age': 25, 'City': 'New York', 'Salary': 50000},
        {'Name': 'Bob', 'Age': 30, 'City': 'London', 'Salary': 60000},
        {'Name': 'Charlie', 'Age': 35, 'City': 'Tokyo', 'Salary': 75000},
        {'Name': 'Diana', 'Age': 28, 'City': 'Paris', 'Salary': 55000}
    ]
    
    # Print table with basic formatting
    print(f"{'Name':<10} {'Age':<5} {'City':<10} {'Salary':<10}")
    print("-" * 40)
    for row in table:
        print(f"{row['Name']:<10} {row['Age']:<5} {row['City']:<10} {row['Salary']:<10}")
    
    return table

# Method 4: Using PrettyTable library
from prettytable import PrettyTable

def create_pretty_table():
    """Create a table using PrettyTable"""
    print("\n=== Method 4: PrettyTable Library ===")
    
    # Create table object
    table = PrettyTable()
    
    # Add columns
    table.field_names = ["Name", "Age", "City", "Salary"]
    
    # Add rows
    table.add_row(["Alice", 25, "New York", 50000])
    table.add_row(["Bob", 30, "London", 60000])
    table.add_row(["Charlie", 35, "Tokyo", 75000])
    table.add_row(["Diana", 28, "Paris", 55000])
    
    print(table)
    
    # Customize appearance
    table.align = "l"  # Left align
    table.border = True
    table.header = True
    
    print("\nCustomized table:")
    print(table)

# Method 5: Create table with calculations
def create_calculated_table():
    """Create a table with calculated columns"""
    print("\n=== Method 5: Table with Calculations ===")
    
    # Base data
    employees = [
        {'name': 'Alice', 'hourly_rate': 25, 'hours_worked': 40},
        {'name': 'Bob', 'hourly_rate': 30, 'hours_worked': 35},
        {'name': 'Charlie', 'hourly_rate': 35, 'hours_worked': 45},
        {'name': 'Diana', 'hourly_rate': 28, 'hours_worked': 38}
    ]
    
    # Calculate total pay and create DataFrame
    for emp in employees:
        emp['total_pay'] = emp['hourly_rate'] * emp['hours_worked']
        emp['overtime_hours'] = max(0, emp['hours_worked'] - 40)
        emp['overtime_pay'] = emp['overtime_hours'] * emp['hourly_rate'] * 1.5
    
    df = pd.DataFrame(employees)
    print(df)
    
    # Add summary statistics
    print(f"\nTotal payroll: ${df['total_pay'].sum():,.2f}")
    print(f"Average hourly rate: ${df['hourly_rate'].mean():.2f}")
    print(f"Total overtime pay: ${df['overtime_pay'].sum():,.2f}")

if __name__ == "__main__":
    # Install required packages first
    print("Creating tables in Python - Multiple Methods\n")
    
    try:
        # Method 1: Pandas (most common)
        df = create_pandas_table()
        
        # Method 2: Tabulate
        create_tabulate_table()
        
        # Method 3: Basic Python
        basic_table = create_basic_table()
        
        # Method 4: PrettyTable
        create_pretty_table()
        
        # Method 5: Calculated table
        create_calculated_table()
        
        print("\n=== Additional DataFrame Operations ===")
        print("Filtering (Age > 30):")
        print(df[df['Age'] > 30])
        
        print("\nSorting by Salary:")
        print(df.sort_values('Salary', ascending=False))
        
        print("\nGrouping and Statistics:")
        print(f"Average age: {df['Age'].mean():.1f}")
        print(f"Total salary: ${df['Salary'].sum():,}")
        
    except ImportError as e:
        print(f"Missing required package: {e}")
        print("To install required packages, run:")
        print("pip install pandas tabulate prettytable")