create database BankingDB;
use BankingDB;
CREATE TABLE Customers
(
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(15)
);

describe Customers;

show tables;

#------------------------------------ 16-09-2026

CREATE TABLE Accounts (
    AccountID INT,
    AccountType VARCHAR(20),
    Balance DECIMAL(10,2)
);

CREATE TABLE Transactions (
    TransactionID INT,
    TransactionDate DATE,
    Amount DECIMAL(10,2),
    TransactionType VARCHAR(20)
);

CREATE TABLE Branches (
    BranchID INT,
    BranchName VARCHAR(100),
    BranchAddress VARCHAR(200),
    BranchPhone VARCHAR(15)
);

CREATE TABLE AccountBranches ( 
		AssignmentDate DATE
);

CREATE TABLE Loans (
    LoanID INT,
    LoanAmount DECIMAL(10,2),
    InterestRate DECIMAL(5,2),
    StartDate DATE,
    EndDate DATE
);

Describe Accounts;
Describe Transactions;
describe Branches;
describe AccountBranches;
describe Loans;

ALTER TABLE Customers
ADD DateOfBirth DATE;

describe Customers;

ALTER TABLE Customers
MODIFY Phone VARCHAR(20);

ALTER TABLE Accounts
ADD CONSTRAINT chk_MinBalance
CHECK (Balance >= 1000);

DROP TABLE AccountBranches;

ALTER TABLE Customers
ADD PRIMARY KEY (CustomerID);

ALTER TABLE Accounts
ADD CustomerID INT;
ALTER TABLE Accounts
ADD CONSTRAINT FK_Accounts_Customers
FOREIGN KEY (CustomerID)
REFERENCES Customers(CustomerID);

ALTER TABLE Customers
MODIFY FirstName VARCHAR(50) NOT NULL;

ALTER TABLE Customers
ADD CONSTRAINT uq_Email UNIQUE (Email);


#########################################
-- Add Primary Keys
ALTER TABLE Accounts
ADD CONSTRAINT PK_Accounts
PRIMARY KEY (AccountID);

ALTER TABLE Transactions
ADD CONSTRAINT PK_Transactions
PRIMARY KEY (TransactionID);

ALTER TABLE Branches
ADD CONSTRAINT PK_Branches
PRIMARY KEY (BranchID);

ALTER TABLE Loans
ADD CONSTRAINT PK_Loans
PRIMARY KEY (LoanID);

-- Add Required Columns


ALTER TABLE Transactions
ADD AccountID INT;

ALTER TABLE Loans
ADD CustomerID INT;


ALTER TABLE Transactions
ADD CONSTRAINT FK_Transactions_Accounts
FOREIGN KEY (AccountID)
REFERENCES Accounts(AccountID);

ALTER TABLE Loans
ADD CONSTRAINT FK_Loans_Customers
FOREIGN KEY (CustomerID)
REFERENCES Customers(CustomerID);

ALTER TABLE Accounts
ADD BranchID INT;

ALTER TABLE Accounts
ADD CONSTRAINT FK_Accounts_Branches
FOREIGN KEY (BranchID)
REFERENCES Branches(BranchID);

INSERT INTO Customers
(CustomerID, FirstName, LastName, Email, Phone, DateOfBirth)
VALUES
(101,'Rahul','Sharma','rahul@gmail.com','9876543210','1998-04-15');

INSERT INTO Accounts
(AccountID, CustomerID, AccountType, Balance)
VALUES
(201,101,'Savings',25000);

SELECT * FROM ACCOUNTS;

UPDATE Customers
SET Phone='9999999999'
WHERE CustomerID=101;

select * from customers;

UPDATE Customers
SET Email='rahul.sharma@gmail.com'
WHERE CustomerID=101;

-- Insert 4 Records into Customers Table
INSERT INTO Customers
(CustomerID, FirstName, LastName, Email, Phone, DateOfBirth)
VALUES
(102, 'Priya', 'Patil', 'priya@gmail.com', '9988776655', '2000-09-20'),
(103, 'Amit', 'Patel', 'amit.patel@gmail.com', '9876500001', '1995-06-18'),
(104, 'Sneha', 'Joshi', 'sneha.joshi@gmail.com', '9876500002', '1997-09-12'),
(105, 'Rohan', 'Kulkarni', 'rohan.k@gmail.com', '9876500003', '1993-11-25');

-- Insert 4 Records into Accounts Table
INSERT INTO Accounts
(AccountID, CustomerID, AccountType, Balance)
VALUES
(202, 102, 'Current', 40000),
(203, 103, 'Savings', 35000),
(204, 104, 'Current', 60000),
(205, 105, 'Savings', 45000);

-- Insert 5 Records into Transactions Table
INSERT INTO Transactions
(TransactionID, AccountID, TransactionDate, Amount, TransactionType)
VALUES
(301, 201, '2025-05-10', 5000, 'Deposit'),
(302, 202, '2025-05-11', 2500, 'Withdraw'),
(303, 203, '2025-05-12', 10000, 'Deposit'),
(304, 204, '2025-05-13', 3000, 'Withdraw'),
(305, 205, '2025-05-14', 7000, 'Deposit');

-- Insert 5 Records into Branches Table
INSERT INTO Branches
(BranchID, BranchName, BranchAddress, BranchPhone)
VALUES
(1, 'Mumbai Branch', 'Andheri, Mumbai', '0221111111'),
(2, 'Pune Branch', 'Shivaji Nagar, Pune', '0202222222'),
(3, 'Nashik Branch', 'College Road, Nashik', '0253222222'),
(4, 'Nagpur Branch', 'Sitabuldi, Nagpur', '0712333333'),
(5, 'Navi Mumbai Branch', 'Vashi, Navi Mumbai', '0224444444');



-- Insert 5 Records into Loans Table
INSERT INTO Loans
(LoanID, LoanAmount, InterestRate, StartDate, EndDate, CustomerID)
VALUES
(301, 500000, 8.50, '2025-01-15', '2030-01-15', 101),
(302, 300000, 9.25, '2025-02-10', '2028-02-10', 102),
(303, 750000, 8.75, '2025-03-20', '2032-03-20', 103),
(304, 250000, 10.00, '2025-04-05', '2029-04-05', 104),
(305, 1000000, 7.95, '2025-05-12', '2035-05-12', 105);

show tables;

#----------------------------------------------------------
/*
1.give me firstname , lastname ,email ,phone of customers
2.all the details of account type savings from accounts table
3.Give me all the accounts with balance > 25000
4.Give me all the trassactions with amount fromm 5000-20000
5.give me all customer details of customer id 101,102 and 103
6.Give me customers whose firstname starts with R
7. Arrange customer names by firstname in ascending order
8. Give different acount types in account table
9. From accounts table give top 3 balances
10. From transaction - skip top 2 and then give 5 rows
11. give all the details of customers whose phone numbers 
are null
12. give all the details of customers whose email id is not 
null.
13. from accounts table give accountid, balance and categorize 
balance  >=50000 then Premium Account,
25000 to 50000 - Standard Account , otherwise Basic Account
*/

#------------------------------------------

/*
14. Give me those customers name whose firstname
starts with A.
15. Those customers whose email id has gmail in it.
16. Customers having lastname ending with kar
17. All the details from accounts table whose 
account type is savings or current.
18.All the details from transactions table 
where transaction type is deposit or withdrawal.
19. All the customers with lastname arranged in 
ascending order.
20. Balance from accounts table arranged in 
descending order.
21. Transaction Date from transaction table
arranged in descending order.
22. Top 5 balance holders in Accounts table.
23. Skip top 3 transactions from transactions 
table and give next 5. 
24. From accounts table give savings account type
balance in descending order.
25. Give 5 customers whose firstname starts 
with S.
26. Give deposit or withdrawal transactions 
order by there transaction date in descending 
order.
*/

SELECT *
FROM Customers
WHERE FirstName LIKE 'A%';

SELECT *
FROM Customers
WHERE Email LIKE '%gmail%';

SELECT *
FROM Customers
WHERE LastName LIKE '%kar';

SELECT *
FROM Accounts
WHERE AccountType IN ('Savings', 'Current');

SELECT *
FROM Transactions
WHERE TransactionType IN ('Deposit', 'Withdrawal');

SELECT *
FROM Customers
WHERE CustomerID IN (101,102,105);

SELECT *
FROM Customers
ORDER BY LastName ASC;

SELECT *
FROM Accounts
ORDER BY Balance DESC;

SELECT *
FROM Transactions
ORDER BY TransactionDate DESC;

SELECT *
FROM Accounts
ORDER BY Balance DESC
LIMIT 5;

SELECT *
FROM Customers
LIMIT 3;

SELECT *
FROM Transactions
LIMIT 5 OFFSET 3;

SELECT *
FROM Accounts
WHERE AccountType = 'Savings'
ORDER BY Balance DESC;

SELECT *
FROM Customers
WHERE FirstName LIKE 'S%'
LIMIT 5;

SELECT *
FROM Transactions
WHERE TransactionType IN ('Deposit','Withdrawal')
ORDER BY TransactionDate DESC;











#----------------------------------

# functions in sql

select * from customers;

select 
upper(FirstName) as upper_case,
lower(LastName) as lower_case,
length(FirstName) as length_firstname,
concat(firstname," ",lastname) as full_name
from customers;

select firstname,
left(firstname,3) as left_3,
right(firstname,3) as right_3,
substring(firstname,2,3) as from_2ndindex_3_letters
from customers;

#-- mathematical functions

select * from loans;
#---- aggregate function
select max(interestRate) max_interestRate,
min(interestRate) min_interestRate,
sum(LoanAmount) total_loan_given,
avg(LoanAmount) average_loan_given,
count(loanAmount) count_of_loan_given
from loans;

select round(1125.51);
select ceil(1125.01), floor(1125.51);
select abs(-255);
select mod(25,7) Remainder;

#------ date functions---------
select curdate(),now();

select * from customers;

select customerid,
dateofbirth,
year(dateofbirth) birthyear,
month(dateofbirth) birthmonth,
day(dateofbirth) birthday
from customers;

select customerid,
datediff(curdate(),dateofbirth) days
from customers;

select customerid,
timestampdiff(year,dateofbirth,curdate()) age
from customers;

# categorize customer into adult or young
# born after 1995 then young otherwise adult

select customerid,
dateofbirth,
if (year(dateofbirth)>1995,"Young","Adult")
from customers;

select * from customers;

select customerid,
ifnull(phone,"Not Available")
from customers;

select * from loans;

select greatest(5,10,15,20),
least(5,10,15,20);

#--------------------- 28-09---------------


select sum(balance),
avg(balance),
max(balance),
min(balance),
count(balance)
from accounts;

select * from accounts;

select accounttype,sum(balance)
from accounts
group by accounttype;

select accounttype,sum(balance)
from accounts
group by accounttype
having sum(balance)>100000;

select loanid,customerid,loanamount,
rank() over(order by loanamount desc),
dense_rank() over(order by loanamount desc),
sum(loanamount) over(order by loanamount desc) running_total,
lag(loanamount) over(order by loanamount desc),
lead(loanamount) over(order by loanamount desc)
from loans;



select * from loans;

#--------------------- subquery-------

#----------------- join-------------

select t.transactionid,
t.transactiondate,t.amount,a.accountid,t.transactiontype,
a.accounttype from transactions t inner join accounts a
on t.accountid=a.accountid;

select t.transactionid,
t.transactiondate,t.amount,a.accountid,
a.accounttype from transactions t natural join accounts a;

select t.transactionid,
t.transactiondate,t.amount,a.accountid,
a.accounttype from accounts a left join transactions t
on t.accountid=a.accountid;

select * from transactions;
select * from accounts;
select a.accountid,
a.accounttype, t.transactionid,
t.transactiondate,t.amount,t.transactiontype
 from transactions t inner join accounts a
on t.accountid=a.accountid
where t.transactiontype="Deposit";

select a.accountid,
a.accounttype, t.transactionid,
t.transactiondate,a.balance,t.amount,t.transactiontype
 from transactions t inner join accounts a
on t.accountid=a.accountid
where a.balance>30000
order by a.balance desc;

#----------------
create view high_balance_Accounts as 
select Accountid,accounttype,balance,customerid
from accounts
where balance>30000;

describe high_balance_Accounts;

show tables;

show full tables where table_type="VIEW";

select * from high_balance_Accounts;
create or replace view high_balance_Accounts as 
select a.accountid,
a.accounttype, t.transactionid,
t.transactiondate,a.balance,t.amount,t.transactiontype
from transactions t inner join accounts a
on t.accountid=a.accountid;
select * from high_balance_Accounts;
select h.accountid,
h.accounttype, h.transactionid,
h.transactiondate,h.balance,h.amount,h.transactiontype
from high_balance_Accounts h
where h.balance>30000 order by h.balance desc;
show tables;

select a.*,t.*
from transactions t inner join accounts a
on t.accountid=a.accountid;
