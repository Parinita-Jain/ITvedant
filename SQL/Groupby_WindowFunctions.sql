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
👉 Window Functions work on groups too, but they don’t reduce rows — instead, they add extra information to each row.

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