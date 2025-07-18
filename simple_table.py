#!/usr/bin/env python3
"""
Simple table creation in Python using only built-in features
No external dependencies required
"""

def create_simple_table():
    """Create a simple table using basic Python"""
    
    # Sample data
    data = [
        ['Name', 'Age', 'City', 'Salary'],
        ['Alice', '25', 'New York', '$50,000'],
        ['Bob', '30', 'London', '$60,000'],
        ['Charlie', '35', 'Tokyo', '$75,000'],
        ['Diana', '28', 'Paris', '$55,000']
    ]
    
    # Calculate column widths
    col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]
    
    # Print table with borders
    def print_separator():
        print('+' + '+'.join('-' * (width + 2) for width in col_widths) + '+')
    
    def print_row(row):
        print('|' + '|'.join(f' {str(item):<{col_widths[i]}} ' for i, item in enumerate(row)) + '|')
    
    # Print the table
    print_separator()
    print_row(data[0])  # Header
    print_separator()
    for row in data[1:]:  # Data rows
        print_row(row)
    print_separator()

def create_dict_table():
    """Create a table using list of dictionaries"""
    
    employees = [
        {'name': 'Alice', 'age': 25, 'department': 'Engineering', 'salary': 75000},
        {'name': 'Bob', 'age': 30, 'department': 'Marketing', 'salary': 65000},
        {'name': 'Charlie', 'age': 35, 'department': 'Sales', 'salary': 70000},
        {'name': 'Diana', 'age': 28, 'department': 'HR', 'salary': 60000}
    ]
    
    # Print header
    print(f"{'Name':<10} {'Age':<5} {'Department':<12} {'Salary':<10}")
    print("-" * 42)
    
    # Print data
    for emp in employees:
        print(f"{emp['name']:<10} {emp['age']:<5} {emp['department']:<12} ${emp['salary']:<9,}")
    
    # Calculate and print summary
    total_salary = sum(emp['salary'] for emp in employees)
    avg_age = sum(emp['age'] for emp in employees) / len(employees)
    
    print("-" * 42)
    print(f"{'Total':<28} ${total_salary:,}")
    print(f"Average Age: {avg_age:.1f}")

def create_matrix_table():
    """Create a multiplication table as an example of numeric tables"""
    
    size = 10
    print(f"Multiplication Table ({size}x{size}):")
    print()
    
    # Print header
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()
    print("   " + "-" * (size * 4))
    
    # Print table rows
    for i in range(1, size + 1):
        print(f"{i:2}|", end="")
        for j in range(1, size + 1):
            print(f"{i*j:4}", end="")
        print()

def create_csv_style_table():
    """Create a table that can be easily exported to CSV"""
    
    import csv
    import io
    
    # Sample data
    data = [
        ['Product', 'Category', 'Price', 'In Stock'],
        ['Laptop', 'Electronics', 999.99, True],
        ['Book', 'Education', 29.99, True],
        ['Chair', 'Furniture', 149.99, False],
        ['Phone', 'Electronics', 699.99, True]
    ]
    
    # Display as table
    print("Product Inventory:")
    for i, row in enumerate(data):
        if i == 0:  # Header
            print(" | ".join(f"{str(cell):<12}" for cell in row))
            print("-" * 60)
        else:
            formatted_row = []
            for j, cell in enumerate(row):
                if j == 2:  # Price column
                    formatted_row.append(f"${cell:<11.2f}")
                elif j == 3:  # Stock column
                    formatted_row.append(f"{'Yes' if cell else 'No':<12}")
                else:
                    formatted_row.append(f"{str(cell):<12}")
            print(" | ".join(formatted_row))
    
    # Show how to write to CSV
    print("\nCSV format:")
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    print(output.getvalue())

if __name__ == "__main__":
    print("Python Table Examples (No External Dependencies)\n")
    
    print("1. Simple Table with Borders:")
    create_simple_table()
    
    print("\n2. Dictionary-based Table:")
    create_dict_table()
    
    print("\n3. Numeric Matrix Table:")
    create_matrix_table()
    
    print("\n4. CSV-style Table:")
    create_csv_style_table()