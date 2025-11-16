"""
Soda Click Data Automation Project
Author: Dania Al Ghanemi

This script automates data processing tasks similar to those performed
during my internship at Soda Click. It demonstrates data cleaning,
analysis, and report generation using Python.
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def load_and_clean_data(filename):
    """Load and clean the raw dataset"""
    print("📊 Loading and cleaning data...")
    
    # Read the CSV file
    df = pd.read_csv(filename)
    
    # Data cleaning steps
    df.drop_duplicates(inplace=True)  # Remove duplicates
    df.dropna(inplace=True)  # Remove empty rows
    df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime
    
    print("✅ Data cleaning completed")
    return df

def analyze_data(df):
    """Perform basic data analysis"""
    print("🔍 Analyzing data...")
    
    # Basic analysis
    total_sales = df['Sales'].sum()
    average_sales = df['Sales'].mean()
    top_product = df.groupby('Product')['Sales'].sum().idxmax()
    
    print(f"📈 Total Sales: £{total_sales:,.2f}")
    print(f"📊 Average Daily Sales: £{average_sales:,.2f}")
    print(f"🏆 Top Performing Product: {top_product}")
    
    return {
        'total_sales': total_sales,
        'average_sales': average_sales,
        'top_product': top_product
    }

def generate_report(df, analysis):
    """Generate a summary report"""
    print("📄 Generating report...")
    
    # Create a simple text report
    report = f"""
    SODA CLICK SALES REPORT
    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
    ==========================================
    
    SUMMARY STATISTICS:
    - Total Sales: £{analysis['total_sales']:,.2f}
    - Average Daily Sales: £{analysis['average_sales']:,.2f}
    - Top Performing Product: {analysis['top_product']}
    
    DATA OVERVIEW:
    - Period Covered: {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}
    - Number of Transactions: {len(df):,}
    - Products Tracked: {df['Product'].nunique()}
    """
    
    # Save report to file
    with open('sales_report.txt', 'w') as f:
        f.write(report)
    
    print("✅ Report saved as 'sales_report.txt'")
    return report

def create_simple_dashboard(df):
    """Create basic visualizations"""
    print("📈 Creating dashboard visualizations...")
    
    # Sales by product
    product_sales = df.groupby('Product')['Sales'].sum()
    
    plt.figure(figsize=(10, 6))
    product_sales.plot(kind='bar', color='skyblue')
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Sales (£)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sales_by_product.png')
    plt.close()
    
    print("✅ Dashboard saved as 'sales_by_product.png'")

def main():
    """Main function to run the data automation pipeline"""
    print("🚀 Starting Soda Click Data Automation...")
    
    try:
        # Step 1: Load and clean data
        df = load_and_clean_data('sample_data.csv')
        
        # Step 2: Analyze data
        analysis = analyze_data(df)
        
        # Step 3: Generate report
        report = generate_report(df, analysis)
        
        # Step 4: Create visualizations
        create_simple_dashboard(df)
        
        print("🎉 Data automation completed successfully!")
        
    except FileNotFoundError:
        print("❌ Error: sample_data.csv file not found.")
        print("Please make sure the data file exists in the same folder.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
