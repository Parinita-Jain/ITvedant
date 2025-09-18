use window_fun;
#Q1. Find the number of employees in each department.

SELECT DEPT_NAME, COUNT(*) AS emp_count
FROM employee
GROUP BY DEPT_NAME;

#Q2. Find the total salary of each department.

SELECT DEPT_NAME, SUM(SALARY) AS total_salary
FROM employee
GROUP BY DEPT_NAME;

#Q3. Find the average salary of each department.

SELECT DEPT_NAME, AVG(SALARY) AS avg_salary
FROM employee
GROUP BY DEPT_NAME;

#Q4. Find departments where total salary > 20,000.

SELECT DEPT_NAME, SUM(SALARY) AS total_salary
FROM employee
GROUP BY DEPT_NAME
HAVING SUM(SALARY) > 20000;

#Q5. Find departments where average salary < 5,000.

SELECT DEPT_NAME, AVG(SALARY) AS avg_salary
FROM employee
GROUP BY DEPT_NAME
HAVING AVG(SALARY) < 5000;

#Q6. Find highest salary in each department.

SELECT DEPT_NAME, MAX(SALARY) AS max_salary
FROM employee
GROUP BY DEPT_NAME;

#Find departments having more than 4 employees.

SELECT DEPT_NAME, COUNT(*) AS emp_count
FROM employee
GROUP BY DEPT_NAME
HAVING COUNT(*) > 4;

#Find employees who earn more than the average salary of their department.

SELECT emp_NAME, DEPT_NAME, SALARY
FROM employee e
WHERE SALARY > (
    SELECT AVG(SALARY)
    FROM employee
    WHERE DEPT_NAME = e.DEPT_NAME
);

#List departments in descending order of their total salary.

SELECT DEPT_NAME, SUM(SALARY) AS total_salary
FROM employee
GROUP BY DEPT_NAME
ORDER BY total_salary DESC;

#Find departments where maximum salary is at least twice the minimum salary.

SELECT DEPT_NAME, MAX(SALARY) AS max_salary, MIN(SALARY) AS min_salary
FROM employee
GROUP BY DEPT_NAME
HAVING MAX(SALARY) >= 2 * MIN(SALARY);

#Q1. Find employees who earn the maximum salary in their department.


SELECT emp_NAME, DEPT_NAME, SALARY
FROM employee e
WHERE SALARY = (
    SELECT MAX(SALARY)
    FROM employee
    WHERE DEPT_NAME = e.DEPT_NAME
);

#Q3. Find departments whose average salary is higher than the company’s average salary.
# Kids compare group averages with global average.

SELECT DEPT_NAME, AVG(SALARY) AS avg_salary
FROM employee
GROUP BY DEPT_NAME
HAVING AVG(SALARY) > (SELECT AVG(SALARY) FROM employee);

#Q4. Find the second highest salary in each department.
# Kids see subquery + aggregate.

SELECT DEPT_NAME, MAX(SALARY) AS second_highest
FROM employee e
WHERE SALARY < (
    SELECT MAX(SALARY)
    FROM employee
    WHERE DEPT_NAME = e.DEPT_NAME
)
GROUP BY DEPT_NAME;

#Find departments where the difference between max and min salary is more than 4000.
# Learning HAVING with condition.

SELECT DEPT_NAME, MAX(SALARY) - MIN(SALARY) AS salary_diff
FROM employee
GROUP BY DEPT_NAME
HAVING (MAX(SALARY) - MIN(SALARY)) > 4000;

#Find employees who earn the minimum salary in each department.
# Mirror of Q1 (now MIN instead of MAX).

SELECT emp_NAME, DEPT_NAME, SALARY
FROM employee e
WHERE SALARY = (
    SELECT MIN(SALARY)
    FROM employee
    WHERE DEPT_NAME = e.DEPT_NAME
);

#List employees who are the only ones in their department with that salary.
#👉 Teaches GROUP BY + COUNT + subquery.

SELECT emp_NAME, DEPT_NAME, SALARY
FROM employee e
WHERE 1 = (
    SELECT COUNT(*)
    FROM employee
    WHERE DEPT_NAME = e.DEPT_NAME
      AND SALARY = e.SALARY
);

#Find departments that have at least one employee with salary > 9000.
#Good training for EXISTS.

SELECT DISTINCT DEPT_NAME
FROM employee e
WHERE EXISTS (
    SELECT 1
    FROM employee
    WHERE DEPT_NAME = e.DEPT_NAME
      AND SALARY > 9000
);

#----------------------------------

/*
What is a Window Function?

👉 GROUP BY works on groups and reduces rows.
👉 Window Functions work on groups too, but they don’t reduce rows — instead, they add extra information 
to each row.

💡 Think of it like this:

GROUP BY = “Tell me how much the whole class scored on average.” (class summary, fewer rows)

Window Function = “Tell me each student’s marks, but also tell me their rank/position in the class.” (row-wise + extra info)

2. Example Dataset (IT Department Only)
emp_NAME	SALARY
Dheeraj	11000
Komal	10000
Melinda	8000
Ibrahim	8000
Vikram	8000
Vasudha	7000
Sanjay	6500
Chandni	4500
Mohan	4000
Akbar	4000
*/
#ROW_NUMBER(), RANK(), DENSE_RANK()

/*
Using GROUP BY
SELECT DEPT_NAME, MAX(SALARY) AS max_salary
FROM employee
GROUP BY DEPT_NAME;


📌 Output (only summaries):

DEPT_NAME	max_salary
Admin	5000
Finance	6500
HR	8000
IT	11000

⚠️ Notice: You don’t see individual employees anymore, just department-level data.

2. Using Window Function
SELECT emp_NAME, DEPT_NAME, SALARY,
       MAX(SALARY) OVER (PARTITION BY DEPT_NAME) AS dept_max_salary
FROM employee;


📌 Output (all employees + dept max):

emp_NAME	DEPT_NAME	SALARY	dept_max_salary
Mohan	Admin	4000	5000
Monica	Admin	5000	5000
Gautham	Admin	2000	5000
Rajkumar	HR	3000	8000
Cory	HR	8000	8000
Akbar	IT	4000	11000
Dheeraj	IT	11000	11000
*/

#Let’s rank employees inside their department by salary.

SELECT emp_ID, emp_NAME, DEPT_NAME, SALARY,
       ROW_NUMBER() OVER (PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS row_num,
       RANK() OVER (PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS rnk,
       DENSE_RANK() OVER (PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS dense_rnk
FROM employee
ORDER BY DEPT_NAME, SALARY DESC;
/*
Explanation:

PARTITION BY DEPT_NAME → restart ranking for each department.

ORDER BY SALARY DESC → highest salary first.

ROW_NUMBER() → unique serial no. per dept.

RANK() → gaps if salaries tie.

DENSE_RANK() → no gaps.
*/

/*
1. RANK()

Gives ranking with gaps when there are ties.

Example: If two employees share the same salary, they get the same rank, but the next rank is skipped.

👉 Use RANK() when you want competition-style ranking (like sports positions).

SELECT emp_NAME, DEPT_NAME, SALARY,
       RANK() OVER (PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS rnk
FROM employee
WHERE DEPT_NAME = 'IT';

emp_NAME	SALARY	RANK
Dheeraj	11000	1
Komal	10000	2
Melinda	8000	3
Ibrahim	8000	3
Vikram	8000	3
Vasudha	7000	6

⚠️ Notice how rank 4 and 5 are skipped.

📌 2. DENSE_RANK()

Gives ranking without gaps when there are ties.

Example: If three employees tie, they all get the same rank, and the next rank continues in sequence.

👉 Use DENSE_RANK() when you want compact rankings (no skipping).

SELECT emp_NAME, DEPT_NAME, SALARY,
       DENSE_RANK() OVER (PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS dense_rnk
FROM employee
WHERE DEPT_NAME = 'IT';

emp_NAME	SALARY	DENSE_RANK
Dheeraj	11000	1
Komal	10000	2
Melinda	8000	3
Ibrahim	8000	3
Vikram	8000	3
Vasudha	7000	4

✅ No gaps.

📌 3. ROW_NUMBER() (for contrast)

Just gives a unique number to each row, even if salaries tie.

Useful when you want a serial number (like picking "top 1 employee per dept").

🎯 Simple Rule of Thumb

RANK() → Use when you want ranking like sports medals (1, 2, 2, 4).

DENSE_RANK() → Use when you want continuous ranks (1, 2, 2, 3).

ROW_NUMBER() → Use when you just need row numbering (no ties).
*/

/*
Aggregate as Window Function (vs GROUP BY)

👉 Difference between GROUP BY and Window Function.

-- With GROUP BY (summary, loses rows)*/
SELECT DEPT_NAME, MAX(SALARY) AS max_salary
FROM employee
GROUP BY DEPT_NAME;

-- With Window Function (keeps all rows + extra info)
SELECT emp_NAME, DEPT_NAME, SALARY,
       MAX(SALARY) OVER (PARTITION BY DEPT_NAME) AS dept_max_salary
FROM employee;

/* Explanation
💡 GROUP BY = only one row per department.
💡 Window Function = shows every employee + their dept topper’s salary.
*/

#-------------------------------------

/*
1. Retrieve all customer records
SELECT * 
FROM Customers;

2. Get details of customers from the UK
SELECT * 
FROM Customers
WHERE country = 'UK';

3. Get customers older than 25 and from either the USA or UK
SELECT * 
FROM Customers
WHERE age > 25 
  AND country IN ('USA', 'UK');

4. Find customers aged between 22 and 28
SELECT * 
FROM Customers
WHERE age BETWEEN 22 AND 28;

5. Get customers from either USA or UAE
SELECT * 
FROM Customers
WHERE country IN ('USA', 'UAE');

6. Find customers whose first name starts with 'Jo'
SELECT * 
FROM Customers
WHERE first_name LIKE 'Jo%';

7. List distinct countries from the Customers table
SELECT DISTINCT country 
FROM Customers;

8. Get the top 3 highest value orders
SELECT * 
FROM Orders
ORDER BY amount DESC
LIMIT 3;

9. Select orders where amount is not null
SELECT * 
FROM Orders
WHERE amount IS NOT NULL;

10. Show each customer’s name and a category based on age
SELECT first_name, last_name, age,
       CASE 
           WHEN age < 25 THEN 'Youth'
           WHEN age BETWEEN 25 AND 30 THEN 'Adult'
           ELSE 'Senior'
       END AS age_group
FROM Customers;

11. Show each customer’s full name in format LASTNAME, firstname
SELECT UPPER(last_name) || ', ' || LOWER(first_name) AS formatted_name
FROM Customers;


(For MySQL: use CONCAT instead of ||.)

12. Round off order amounts
SELECT order_id, amount,
       ROUND(amount, -2) AS rounded_amount,
       CEIL(amount) AS ceiling_amount,
       FLOOR(amount) AS floor_amount
FROM Orders;

13. Compare each order’s amount to the average
SELECT order_id, amount,
       CASE 
           WHEN amount > (SELECT AVG(amount) FROM Orders) THEN 'Above Average'
           ELSE 'Below Average'
       END AS comparison_result
FROM Orders;

14. Total, average, min, max amount
SELECT SUM(amount) AS total_amount,
       AVG(amount) AS average_amount,
       MIN(amount) AS minimum_amount,
       MAX(amount) AS maximum_amount
FROM Orders;

15. Customers with more than 1 order
SELECT customer_id, COUNT(*) AS total_orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(*) > 1;

16. Customers with >1 order, sorted
SELECT customer_id, COUNT(*) AS total_orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY total_orders DESC;

17. Total amount spent per customer (if > 500)
SELECT customer_id, SUM(amount) AS total_spent
FROM Orders
GROUP BY customer_id
HAVING SUM(amount) > 500
ORDER BY customer_id;

18. Mouse/Keyboard orders (if > 1)
SELECT customer_id, COUNT(*) AS total_orders
FROM Orders
WHERE item IN ('Mouse', 'Keyboard')
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY total_orders DESC;

19. Customers with orders > average order amount (Subquery)
SELECT * 
FROM Customers
WHERE customer_id IN (
    SELECT customer_id 
    FROM Orders
    WHERE amount > (SELECT AVG(amount) FROM Orders)
);

20. Subquery in SELECT clause (Order + customer name)
SELECT order_id, item, amount,
       (SELECT first_name 
        FROM Customers c 
        WHERE c.customer_id = o.customer_id) AS customer_name
FROM Orders o;

21. Subquery with IN – Customers with Delivered shipment
SELECT first_name, last_name
FROM Customers
WHERE customer_id IN (
    SELECT customer 
    FROM Shippings
    WHERE status = 'Delivered'
);

22. Customers who placed at least 1 order
SELECT * 
FROM Customers
WHERE customer_id IN (SELECT DISTINCT customer_id FROM Orders);

23. Customers who never placed any order
SELECT * 
FROM Customers c
WHERE c.customer_id NOT IN (SELECT DISTINCT customer_id FROM Orders);

🔗 Joins
24. Customer names and their ordered items
SELECT c.first_name, c.last_name, o.item
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id;

25. All customers and their orders (if any)
SELECT c.first_name, c.last_name, o.item
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id;

26. Customer names and items > ₹500
SELECT c.first_name, o.item, o.amount
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.amount > 500;

27. Order details with customer country
SELECT o.order_id, o.item, o.amount, c.country
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id;

28. Customers with pending shipment
SELECT c.first_name, c.last_name, s.status
FROM Customers c
JOIN Shippings s ON c.customer_id = s.customer
WHERE s.status = 'Pending';

29. Customers who placed both Mouse & Keyboard (self-join)
SELECT DISTINCT c.first_name, c.last_name
FROM Orders o1
JOIN Orders o2 ON o1.customer_id = o2.customer_id
JOIN Customers c ON o1.customer_id = c.customer_id
WHERE o1.item = 'Mouse' AND o2.item = 'Keyboard';

30. Customers who haven’t received any delivery
SELECT c.first_name, c.last_name
FROM Customers c
WHERE c.customer_id NOT IN (
    SELECT customer FROM Shippings WHERE status = 'Delivered'
);

31. All customers and their order amount (if none, 0)
SELECT c.customer_id, c.first_name, c.last_name,
       COALESCE(o.amount, 0) AS order_amount
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id;

32. Shipping priority
SELECT s.shipping_id, s.status, c.first_name, o.amount,
       CASE 
           WHEN s.status = 'Delivered' THEN 'Low'
           WHEN s.status = 'Pending' AND o.amount > 1000 THEN 'High'
           ELSE 'Medium'
       END AS shipping_priority
FROM Shippings s
LEFT JOIN Customers c ON s.customer = c.customer_id
LEFT JOIN Orders o ON c.customer_id = o.customer_id;

33. Customers who ordered items above average amount
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, c.age, c.country
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.amount > (SELECT AVG(amount) FROM Orders);

34. Unique items ordered, sorted alphabetically, limit 5
SELECT DISTINCT item
FROM Orders
ORDER BY item ASC
LIMIT 5;

Key Insights

Majority of customers are from USA & UK.

Only 1 customer (David Robinson) made a high-value order above average.

Customer 4 (John Reinhardt) is the most frequent buyer.

About 40% of customers (2/5) still have pending shipments.

The order distribution is highly skewed (Monitor = ₹12,000 vs others <₹500).

*/

#------------------------ Subqueries-----------------------

use window_fun;

#Subquery Guide (with Employee Table)
# 1. Subquery in SELECT (Scalar subquery)

# Adds an extra calculated column.

SELECT emp_NAME, DEPT_NAME, SALARY,
       (SELECT AVG(SALARY) FROM employee) AS company_avg_salary
FROM employee;


# Insight: Every row shows employee info + company-wide average salary.

# 2. Subquery in WHERE

# Filters rows using another query.

-- Employees earning more than average salary
SELECT emp_NAME, DEPT_NAME, SALARY
FROM employee
WHERE SALARY > (SELECT AVG(SALARY) FROM employee);

# 3. Subquery in HAVING

# Works after GROUP BY.

-- Departments with avg salary above company average
SELECT DEPT_NAME, AVG(SALARY) AS avg_sal
FROM employee
GROUP BY DEPT_NAME
HAVING AVG(SALARY) > (SELECT AVG(SALARY) FROM employee);

# 4. Subquery in FROM (Derived table)

# Used like a temporary table.

SELECT dept_name, avg_salary
FROM (
    SELECT DEPT_NAME, AVG(SALARY) AS avg_salary
    FROM employee
    GROUP BY DEPT_NAME
) t;

# 5. IN with Subquery

# Checks if value belongs to a list.

-- Employees in departments where avg salary > 6000
SELECT emp_NAME, DEPT_NAME, SALARY
FROM employee
WHERE DEPT_NAME IN (
    SELECT DEPT_NAME
    FROM employee
    GROUP BY DEPT_NAME
    HAVING AVG(SALARY) > 6000
);

# 6. ANY with Subquery

# Condition is true if it matches at least one row.

-- Employees earning more than ANY salary in HR dept
SELECT emp_NAME, SALARY
FROM employee
WHERE SALARY > ANY (
    SELECT SALARY FROM employee WHERE DEPT_NAME = 'HR'
);


# Means: salary > the lowest HR salary.

# 7. ALL with Subquery

# Condition must be true for all rows.

-- Employees earning more than ALL HR salaries
SELECT emp_NAME, SALARY
FROM employee
WHERE SALARY > ALL (
    SELECT SALARY FROM employee WHERE DEPT_NAME = 'HR'
);


# Means: salary > highest HR salary.

# 8. EXISTS with Subquery

# True if inner query returns any row.

-- Employees in departments that have at least one person earning > 10000
SELECT emp_NAME, DEPT_NAME, SALARY
FROM employee e
WHERE EXISTS (
    SELECT 1
    FROM employee
    WHERE DEPT_NAME = e.DEPT_NAME
      AND SALARY > 10000
);

# 9. Correlated Subquery

# Inner query depends on outer query.

-- Employees who have max salary in their department
SELECT emp_NAME, DEPT_NAME, SALARY
FROM employee e
WHERE SALARY = (
    SELECT MAX(SALARY)
    FROM employee
    WHERE DEPT_NAME = e.DEPT_NAME
);


#e.DEPT_NAME makes it correlated → compares within each dept.

/*
IN → "in this list?"

ANY / SOME → "better than at least one?"

ALL / EVERY → "better than everyone?"

EXISTS → "does this situation exist?"

Scalar subquery → "single number for all rows"

Correlated → "compare row-by-row inside dept/team"
*/