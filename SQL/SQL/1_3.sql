show databases;
create database constraints;
use constraints;
create table abc
(id int,
name varchar(20));
show tables;
desc abc;
insert into abc(id,name) values
(1,"April"),(2,"Apple");
select * from abc;
insert into abc(name,id) values
("Bob",2),
("Charlie",3);
select * from abc;
insert into abc(name) values
("Scott"),("Jerry");
select * from abc;


/*
Constraints - 
data integrity consistency and reliability ensuring 
*/
# not null
create table n_n
(id int not null,
name varchar(20));
desc n_n;
insert into n_n(name) values
("April"),
("Apple");
select * from n_n;
# not null -
insert into n_n(id,name) values(1,"Bob"),
(2,"Jerry"),(3,null);
select * from n_n;

create table u
(id int unique,
name varchar(20));
insert into u(id,name) values(1,"Bob"),
(2,"Jerry"),(null,"Harry"),(null,"Potter");
select * from u;
insert into u(id,name) values(5,"Parrot");
select * from u;

create table nn_u(
id int not null unique,
name varchar(20));
desc u;
desc nn_u;
# primary key constarint=not null+unique
insert into nn_u(id,name) values(null,"April");
select * from nn_u;
insert into nn_u(id,name) values(0,"April");
select * from nn_u;
insert into nn_u(id,name) values(0,"Bob");
select * from nn_u;

create table pri
(id int primary key,
name varchar(20));
desc pri;

create table p
(id int primary key,
aadhar bigint unique not null,
pan_card varchar(20) not null unique,
name varchar(20));

desc p;
/* rtytuhn */

create table ch(
id int , 
name varchar(20),
age int,
check(age>=18));
desc ch;
insert into ch(id,name,age) values
(1,"April",14);
select * from ch;
insert into ch(id,name,age) values
(1,"April",24);
select * from ch;
insert into ch(id,name,age) values
(2,"April",18);
select * from ch;
show create table ch;

drop table ch;

create table ch(
id int , 
name varchar(20),
age int check(age>=18));
show create table ch;

show tables;

create table d
(id int ,
name varchar(20),
age int default 18,
city varchar(20) default "Mumbai");

desc d;

insert into d(id,name,age,city) values
(1,"Apple",25,"Pune");
select * from d;

insert into d(id,name,age,city) values
(1,"Apple",25,null);
select * from d;

insert into d(id,name) values
(1,"Apple");
select * from d;

# foreign key
create table customers
( id int primary key,
  name varchar(20)
);

create table orders
(o_id int primary key,
 c_id int,
 foreign key(c_id) references customers(id)
);
desc customers;
desc orders;
select * from customers;
insert into orders(o_id,c_id) values
(23,1);
insert into customers(id,name) values
(1,"April");
insert into orders(o_id,c_id) values
(23,1);
insert into orders(o_id,c_id) values
(22,1),(24,1),(25,1);
select * from orders;

delete from customers where id=1;

delete from orders where c_id=1;
select * from orders;
delete from customers where id=1;
select * from customers;

#---------------------------------------------------------

# alter table

create table product_demo
( id int,
  name varchar(20),
  price decimal(6,2)
);
desc product_demo;
show tables;
alter table product_demo rename to product;
show tables;
desc product;
alter table product modify price int;
desc product;
alter table product modify name varchar(50);
desc product;
alter table product add constraint chk check(price>0);
show create table product;
alter table product modify name varchar(50) default "Harry";
desc product;

alter table product modify name varchar(50) not null default "Harry";
desc product;

alter table product add column email_id varchar(50) after id;
desc product;

alter table product drop column email_id;
desc product;

alter table product change column id pid int;
desc product;

alter table product add constraint primary key(pid);
desc product;

alter table product drop primary key;
desc product;
insert into product(pid,name,price) values
(null,"Saj",123);
alter table product modify pid int;
insert into product(pid,name,price) values
(null,"Saj",123);
alter table product drop constraint chk;

use dql;
show tables;
select * from student_demo;

drop database if exists dql;
create database dql;
use dql;
create table student_demo(
roll int, subject varchar(20),addr varchar(20),marks int);
insert into student_demo values
(1,"Python","Pune",56),
(2,"Java","Mumbai",95),
(3,"HTML","Nasik",85),
(4,"C","Pune",56),
(5,"Python","Nasik",50),
(6,"Django","Andheri",99),
(7,"JavaScript","Banglore",85),
(8,null,"Pune",null);
select * from student_demo;
insert into student_demo(roll,addr) values(9,"Delhi"),
(10,"Mumbai");
select * from student_demo;
insert into student_demo values
(11,"Django","Andheri",78),
(12,"JavaScript","Banglore",45),
(13,"Python","Andheri",16),
(14,"Python","Pune",96);

select * from student_demo;

select roll,marks from student_demo;

select * from student_demo where roll=5;

select subject,marks from student_demo where roll=7;

# Roll and  number of those students whose marks are less than 90
select roll,marks from student_demo
where marks<90;
select roll,marks from student_demo
where marks<90 and marks>50;

select roll,marks from student_demo
where marks>=50 and marks<=90;

#between
select roll,marks from student_demo
where marks between 50 and 90; #>=

select roll,marks from student_demo
where marks between 90 and 50;

select roll,marks,
      case when marks between 75 and 100 then "very good"
		   when marks between 60 and 74 then "good"
		   when marks between 35 and 59 then "ok"
           else "fail"
      end as Comments
from student_demo;

select * from student_demo
where roll=1 or roll=7;

select * from student_demo
where roll=7 or roll=1;

select * from student_demo
where roll in (1,7);

select * from student_demo
where roll in (7,1);

select * from student_demo
where roll not in (1,7);

select distinct addr from student_demo;


select distinct addr from student_demo
where addr like "%i";

select distinct addr from student_demo
where addr like "_u%";

select distinct addr from student_demo
where addr like "_u__";

select distinct addr from student_demo
where addr not like "_u%";

select roll,marks from student_demo;

select roll,marks from student_demo
order by marks desc
limit 3;

select roll,marks from student_demo
where marks is not null
order by marks;

select roll,marks from student_demo
order by marks desc
limit 1,2;
#-------------------
create database func;
use func;

select current_date(); # year-month-day

select date_format(current_time(),"%H");

SELECT DATE_ADD(current_date(), INTERVAL 31 DAY),
       DATE_ADD(current_date(), INTERVAL 2 Month),
       date_sub(current_date(), INTERVAL 2 Year);

select if(Month(current_date())>6,"Second Half","First Half");

select Month(current_date());

select 
case
 when Month(current_date()) between 1 and 3 then "Q1"
 when Month(current_date()) between 4 and 6 then "Q2"
 when Month(current_date()) between 7 and 9 then "Q3"
 else "Q4"
end as Quarter;

select current_time();

select now();

select dayofweek(now()); # sunday 1

select last_day(now());

select extract(year from now()),
	   extract(month from now()),
       extract(day from now()),
       extract(hour from now());

#-----------------------------------------------------
use new_data_gh;
show tables;

select * from cust_gh;

select distinct country from cust_gh;

select * from cust_gh;

select count(*) from cust_gh
where country="USA";


select count(*) from cust_gh
where country="U";

select country,count(*),avg(age),min(age),max(age) from cust_gh
group by country;

select country,count(*),avg(age),min(age),max(age) from cust_gh
group by country
having avg(age)>25;

select country,count(*),avg(age),min(age),max(age) from cust_gh
group by country
having avg(age)>25 and count(age)>1;

select country,count(*),avg(age),min(age),max(age) from cust_gh
group by country
having avg(age)>25
order by avg(age) desc;

use window_fun;
show tables;
select * from employee;

/*
*/
#--------------------------------------- 17-09
use window_fun;

# Find the highest salary given in each department.
SELECT DEPT_NAME, MAX(SALARY) AS max_salary
FROM employee
GROUP BY DEPT_NAME;
/*
Admin	5000
Finance	6500
HR	8000
IT	11000
*/
SELECT emp_ID,emp_Name,DEPT_NAME, salary,
MAX(SALARY) over (Partition by dept_name) 
from employee;

SELECT emp_ID,emp_Name,DEPT_NAME, salary,
MAX(SALARY) over (Partition by dept_name) as Max_salary,
Min(SALARY) over (Partition by dept_name) as Min_salary,
Avg(SALARY) over (Partition by dept_name)    
from employee;

SELECT emp_ID,emp_Name,DEPT_NAME, salary,
MAX(SALARY) over (Partition by dept_name) ,
row_number() over (Partition by dept_name order by salary desc),
dense_rank() over (Partition by dept_name order by salary desc),
rank() over (Partition by dept_name order by salary desc)
from employee;
#-------------------------------------------------
use new_data_gh;

show tables;

select * from employee_sq;
select * from employee_copy;

desc employee_sq;
desc employee_copy;

# give me the name of employee earning highest salary

select max(emp_salary) from employee_sq;
select * from employee_sq;

select emp_name,max(emp_salary) from employee_sq;

select emp_name from employee_sq
where emp_salary=113000;


select emp_name from employee_sq
where emp_salary=(select max(emp_salary)
				  from employee_sq);
                  
select * from employee_sq
order by emp_salary desc limit 1;

select avg(emp_salary) from employee_sq; # 88333.3333

select * from employee_sq;
delete from employee_sq where emp_id=106;

select avg(emp_salary) from employee_sq; # 89400.0000
delete from employee_sq where emp_id in (109,110);
select * from employee_sq
where emp_salary>88333.3333;

select avg(emp_salary) from employee_sq; #93000.0000

select * from employee_sq;

select * from employee_sq
where emp_salary>(select avg(emp_salary) from employee_sq);

select * from employee_copy;

select emp_id,emp_age from employee_copy;

select * from employee_copy
where emp_age>(select min(emp_age) from employee_copy);

select avg(emp_age) from employee_copy;
 
select * from employee_copy
where emp_age>(select avg(emp_age) from employee_copy);

update employee_sq 
set emp_salary=emp_salary+3000
where emp_age>(select avg(emp_age) from employee_copy);
 
select * from employee_sq;

#-----------------------------
use window_fun;
show tables;

# emp_name , dept_name , salary of employees.
select emp_name, dept_name,salary,
(select avg(salary) from employee) Average_Salary
from employee;

# emp_name, dept_name,salary
       
select avg(salary) from employee; # 5791.6667
select * from employee;

select * from employee
where salary>(select avg(salary) from employee);

#------------------------------------------------------------------------------

select dept_name,avg(salary) from employee
group by dept_name;


select emp_name,dept_name,salary
from employee where dept_name in 
(select dept_name from employee
group by dept_name
having avg(salary)>5000);

select dept_name,avg(salary) from employee
group by dept_name
having avg(salary)>(select avg(salary) from employee);

# in clause

select dept_name from employee
group by dept_name
having avg(salary)>5000;

show tables;

# Any, All, Exist
#--
select distinct salary from employee where dept_name="HR";
/*
3000
7000
3500
8000
*/
select emp_id,salary from employee; 

select emp_id,salary from employee
where salary>Any(select distinct salary from employee where dept_name="HR");

select emp_id,salary from employee
where salary>All(select distinct salary from employee where dept_name="HR");

# from clause query

# maximum salary from each dept

select dept_name,max(salary) 
from employee
group by dept_name
having max(salary) between 5000 and 10000;
# less flexible 

select dept_name,m_max 
from (select dept_name,max(salary) m_max
	  from employee
	  group by dept_name
) dept_max_salary
where m_max between 5000 and 10000; # dept_max_salary is a temporary table

#------
select dept_name , emp_name,salary
from employee where dept_name="IT"
order by salary desc; # HR	Preet	7000 , IT	Komal	10000

select e.dept_name , e.emp_name,salary
from employee e
where salary = (select salary
                from employee
                where dept_name=e.dept_name
                order by salary desc
                limit 1,1);

# window function
select second_highest.dept_name , second_highest.emp_name,
second_highest.salary
from ( select dept_name , emp_name, salary,
       dense_rank() over(partition by 
        dept_name order by salary desc) as rnk
        from employee
   ) second_highest
where rnk=2;

select dept_name , emp_name, salary,
       dense_rank() over (partition by 
        dept_name order by salary desc) as rnk
        from employee;

#_______________________________________________
use new_data_gh;
show tables;

select * from employee_j;
/*
emp_no,emp_name,emp_add
1	ram	delhi
2	varun	chandigarh
3	ravi	chandigarh
4	amrit	delhi
*/
select * from department_j;
/*
dept,dept_name,emp_no
d1	HR	1
d2	IT	2
d3	Marketing	4
select * from employee_j,department_j;
select * from employee_j cross join department
*/
select dept_name from department_j
where dept="d3";

select emp_add from employee_j
where emp_name="Varun";

# give me the name of the employee working in "HR" department

select emp_name from employee_j
where emp_no in (
	select emp_no from department_j
	where dept_name="HR");
    
select * from employee_j,department_j;

/*
empno			dept
1	ram	delhi	d1	HR	1
1	ram	delhi	d2	IT	2
1	ram	delhi	d3	Marketing	4
2	varun	chandigarh	d1	HR	1
2	varun	chandigarh	d2	IT	2
2	varun	chandigarh	d3	Marketing	4
3	ravi	chandigarh	d1	HR	1
3	ravi	chandigarh	d2	IT	2
3	ravi	chandigarh	d3	Marketing	4
4	amrit	delhi	d1	HR	1
4	amrit	delhi	d2	IT	2
4	amrit	delhi	d3	Marketing	4

*/

select * from employee_j cross join department_j
where employee_j.emp_no=department_j.emp_no
and department_j.dept_name="HR";

select * from employee_j,department_j
where employee_j.emp_no=department_j.emp_no
and department_j.dept_name="HR";

select * from employee_j natural join department_j;

select * from employee_j natural join department_j
where department_j.dept_name="HR";

# inner join
select * from employee_j inner join department_j
on employee_j.emp_no=department_j.emp_no 
and department_j.dept_name="HR";

# left(outer) join
select * from employee_j left join department_j
on employee_j.emp_no=department_j.emp_no ;

select * from department_j left join employee_j
on employee_j.emp_no=department_j.emp_no ;

select * from employee_j right join department_j
on employee_j.emp_no=department_j.emp_no ;

select * from department_j right join employee_j
on employee_j.emp_no=department_j.emp_no ;

#-------- self join ----
select * from student_j;
# s1 -- why ? different c_id, same s_id

select distinct t1.s_id from student_j as t1,student_j as t2
where t1.s_id=t2.s_id and t1.c_id<>t2.c_id;
