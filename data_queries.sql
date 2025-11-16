-- SQL Data Queries for Business Analysis
-- Demonstrates SQL skills for data querying and analysis

-- 1. Basic SELECT with filtering
SELECT * FROM sales_data 
WHERE sales > 1000 
ORDER BY date DESC;

-- 2. Aggregate functions for business intelligence
SELECT 
    product,
    COUNT(*) as transaction_count,
    AVG(sales) as average_sales,
    SUM(sales) as total_revenue
FROM sales_data 
GROUP BY product;

-- 3. Date-based analysis
SELECT 
    strftime('%Y-%m', date) as month,
    SUM(sales) as monthly_revenue
FROM sales_data 
GROUP BY month
ORDER BY month;
