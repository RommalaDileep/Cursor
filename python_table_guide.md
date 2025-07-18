# Python Table Creation Guide

This guide demonstrates various methods to create tables in Python, from simple built-in approaches to powerful data analysis libraries.

## Quick Start (No Dependencies)

The simplest way to create a table in Python uses only built-in features:

```python
# Simple table with formatting
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Tokyo']
]

# Print with basic formatting
for row in data:
    print(f"{row[0]:<10} {row[1]:<5} {row[2]:<10}")
```

## Method 1: Built-in Python (No Dependencies)

### Basic Table with Borders

```python
def create_table_with_borders(data):
    # Calculate column widths
    col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]
    
    # Print separator
    def print_separator():
        print('+' + '+'.join('-' * (width + 2) for width in col_widths) + '+')
    
    # Print row
    def print_row(row):
        print('|' + '|'.join(f' {str(item):<{col_widths[i]}} ' for i, item in enumerate(row)) + '|')
    
    # Print the table
    print_separator()
    print_row(data[0])  # Header
    print_separator()
    for row in data[1:]:  # Data rows
        print_row(row)
    print_separator()
```

### Dictionary-Based Tables

```python
employees = [
    {'name': 'Alice', 'age': 25, 'department': 'Engineering'},
    {'name': 'Bob', 'age': 30, 'department': 'Marketing'},
    {'name': 'Charlie', 'age': 35, 'department': 'Sales'}
]

# Print formatted table
print(f"{'Name':<10} {'Age':<5} {'Department':<12}")
print("-" * 30)
for emp in employees:
    print(f"{emp['name']:<10} {emp['age']:<5} {emp['department']:<12}")
```

## Method 2: Pandas DataFrame (Recommended for Data Analysis)

Pandas is the most popular library for data manipulation and analysis in Python.

### Installation
```bash
pip install pandas
```

### Basic Usage

```python
import pandas as pd

# Create from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Tokyo', 'Paris'],
    'Salary': [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)
print(df)
```

### Advanced Operations

```python
# Filtering
young_employees = df[df['Age'] < 30]

# Sorting
df_sorted = df.sort_values('Salary', ascending=False)

# Grouping and aggregation
avg_salary_by_city = df.groupby('City')['Salary'].mean()

# Adding calculated columns
df['Salary_USD'] = df['Salary'] * 1.1  # 10% bonus

# Summary statistics
print(df.describe())
```

## Method 3: Tabulate Library (Pretty Formatting)

The `tabulate` library provides excellent table formatting options.

### Installation
```bash
pip install tabulate
```

### Usage

```python
from tabulate import tabulate

table_data = [
    ['Alice', 25, 'New York', 50000],
    ['Bob', 30, 'London', 60000],
    ['Charlie', 35, 'Tokyo', 75000]
]

headers = ['Name', 'Age', 'City', 'Salary']

# Different formats
print("Grid format:")
print(tabulate(table_data, headers=headers, tablefmt='grid'))

print("Fancy grid format:")
print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))

print("Markdown format:")
print(tabulate(table_data, headers=headers, tablefmt='pipe'))

print("LaTeX format:")
print(tabulate(table_data, headers=headers, tablefmt='latex'))
```

## Method 4: PrettyTable Library

### Installation
```bash
pip install prettytable
```

### Usage

```python
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City", "Salary"]

table.add_row(["Alice", 25, "New York", 50000])
table.add_row(["Bob", 30, "London", 60000])
table.add_row(["Charlie", 35, "Tokyo", 75000])

print(table)

# Customize appearance
table.align = "l"  # Left align
table.border = True
table.header = True
table.sortby = "Age"
print(table)
```

## Method 5: Creating Tables for Web (HTML)

```python
def create_html_table(data, headers):
    html = "<table border='1'>\n"
    
    # Add header
    html += "  <tr>\n"
    for header in headers:
        html += f"    <th>{header}</th>\n"
    html += "  </tr>\n"
    
    # Add data rows
    for row in data:
        html += "  <tr>\n"
        for cell in row:
            html += f"    <td>{cell}</td>\n"
        html += "  </tr>\n"
    
    html += "</table>"
    return html

# Usage
data = [['Alice', 25, 'New York'], ['Bob', 30, 'London']]
headers = ['Name', 'Age', 'City']
html_table = create_html_table(data, headers)
```

## Method 6: CSV Tables

```python
import csv
import io

def create_csv_table(data, headers):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    writer.writerows(data)
    return output.getvalue()

# Usage
data = [['Alice', 25, 'New York'], ['Bob', 30, 'London']]
headers = ['Name', 'Age', 'City']
csv_content = create_csv_table(data, headers)
print(csv_content)
```

## Advanced Examples

### 1. Financial Table with Calculations

```python
import pandas as pd

# Sample financial data
investments = [
    {'stock': 'AAPL', 'shares': 100, 'price': 150.00, 'dividend_yield': 0.02},
    {'stock': 'GOOGL', 'shares': 50, 'price': 2500.00, 'dividend_yield': 0.01},
    {'stock': 'MSFT', 'shares': 75, 'price': 300.00, 'dividend_yield': 0.015}
]

df = pd.DataFrame(investments)

# Calculate additional columns
df['total_value'] = df['shares'] * df['price']
df['annual_dividend'] = df['total_value'] * df['dividend_yield']

# Format for display
pd.options.display.float_format = '${:,.2f}'.format
print(df)

# Summary
print(f"\nTotal Portfolio Value: ${df['total_value'].sum():,.2f}")
print(f"Total Annual Dividends: ${df['annual_dividend'].sum():,.2f}")
```

### 2. Time Series Table

```python
import pandas as pd
from datetime import datetime, timedelta

# Create time series data
dates = [datetime.now() - timedelta(days=x) for x in range(7, 0, -1)]
sales = [1200, 1350, 1100, 1450, 1600, 1300, 1500]

df = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})

df['Day'] = df['Date'].dt.strftime('%A')
df['Running_Total'] = df['Sales'].cumsum()
df['Daily_Change'] = df['Sales'].pct_change() * 100

print(df.to_string(index=False))
```

### 3. Pivot Table

```python
import pandas as pd

# Sample data
sales_data = [
    {'Region': 'North', 'Product': 'A', 'Quarter': 'Q1', 'Sales': 100},
    {'Region': 'North', 'Product': 'B', 'Quarter': 'Q1', 'Sales': 150},
    {'Region': 'South', 'Product': 'A', 'Quarter': 'Q1', 'Sales': 120},
    {'Region': 'South', 'Product': 'B', 'Quarter': 'Q1', 'Sales': 180},
    {'Region': 'North', 'Product': 'A', 'Quarter': 'Q2', 'Sales': 110},
    {'Region': 'North', 'Product': 'B', 'Quarter': 'Q2', 'Sales': 160},
]

df = pd.DataFrame(sales_data)

# Create pivot table
pivot = pd.pivot_table(df, 
                      values='Sales', 
                      index='Region', 
                      columns='Product', 
                      aggfunc='sum',
                      fill_value=0)

print(pivot)
```

## Best Practices

1. **Choose the right tool:**
   - Use pandas for data analysis and manipulation
   - Use tabulate for quick, pretty formatting
   - Use built-in methods for simple, dependency-free solutions

2. **Data formatting:**
   - Always format numbers appropriately (currency, percentages)
   - Handle missing data gracefully
   - Use consistent column widths for readability

3. **Performance:**
   - For large datasets, pandas is highly optimized
   - Avoid rebuilding tables repeatedly in loops
   - Consider chunking very large datasets

4. **Export options:**
   - CSV for data exchange
   - HTML for web display
   - LaTeX for academic papers
   - Excel for business reports

## Running the Examples

1. **Simple examples (no dependencies):**
   ```bash
   python3 simple_table.py
   ```

2. **Full examples (with dependencies):**
   ```bash
   pip install pandas tabulate prettytable
   python3 create_table_examples.py
   ```

This guide covers the most common and effective ways to create tables in Python, from simple console output to sophisticated data analysis tables.