show databases;
drop database a338;
create database a338;
show databases;
use a338;
create table student
( rollNo int,
  name varchar(20),
  date_of_birth date,
  branch varchar(10),
  percentage decimal(5,2)
);

show tables;
describe student;

insert into 
student(rollNo,
name,date_of_birth,branch,percentage)
values
(1,"Sumit","19-03-02","Extc",76.38);
select * from student;

insert into 
student(rollNo,
name,date_of_birth,branch,percentage)
values
(2,"Bhagyashree","20-08-04","Comp",67.92),
(3,"Pranjali","12-12-04","Mech",55.62);
select * from student;
insert into student(date_of_birth) values
("2004-08-20");
select * from student;
insert into student(date_of_birth) values
(str_to_date("19-Mar-02","%d-%b-%y"));
select * from student;

/*
%d -- day(01-31)
%b -- short month (Jan,Feb)
%M -- Full month (January)
%y -- 2-digit year
%Y -- 4-digit year
# Mysql internally store date as YYYY-MM-DD
*/
#-------------------
show tables;
desc student;
select * from student;
insert into 
student(rollNo,
name,date_of_birth,branch,percentage)
values
(1,234,"19-03-02","Extc",76.38);
select * from student;
select * from student;
# constraints
delete from student 
where rollNo=1;
select * from student;
update student set 
percentage=percentage+10
where rollNo=3;
select * from student;

update student set
percentage=100;

select * from student;

update student set name="April"
where rollNo=2;
select * from student;

delete from student
where date_of_birth<"2020-08-04";

select * from student;

delete from student;
select * from student;


#_----------------------
# Constraints
drop table employees;
create table employees
( emp_id varchar(20) unique,
  emp_name varchar(20)  not null,
  emp_number varchar(20) primary key,
  emp_pan varchar(20) not null unique,
  emp_adhard varchar(20) not null unique
);
desc employees;
insert into employees(emp_id,emp_name,
emp_number,emp_pan,emp_adhard) values
("","apie","bdei","1734g","8059");
select * from employees;

#-----------------
create table employee
( empid int primary key,
  fname varchar(20) not null,
  lname varchar(20) unique,
  course varchar(20) default "DSDA",
  salary decimal(7,2) check(salary>10000),
  emp_email varchar(40) unique not null
);
insert into employee values
(1,"a","b","FSD",19000,"abc@");
select * from employee;
insert into employee(empid,fname,lname,salary,
emp_email) values (2,"t","v",17000,"axd");

create table customers
( cid int ,
  cname varchar(20),
  primary key(cid)
);
desc customers;
create table orders
( oid int primary key,
  oname varchar(20),
  cid int ,
  constraint for_key
  foreign key(cid) references customers(cid)
);
desc orders;
select * from customers;
insert into orders(oid,oname,cid) values
(10,"Apple",1); # error
select * from orders;
insert into customers(cid,cname) values (1,"Tom");
insert into orders(oid,oname,cid) values
(10,"Apple",1);
delete from customers where cid=1; # error
delete from orders where cid=1;
delete from customers where cid=1;

#--------------------

# alter 
desc customers;

alter table customers
add column cpan varchar(20) ;
desc customers;
alter table customers drop column cpan;
desc customers;
alter table customers add column cpan varchar(20) after cid;
desc customers;
# modify - datatype change, not null default
alter table customers
modify cpan varchar(50) not null default("ABCD");
desc customers;

#Rename table "old_table_name" to "new_table_name"

alter table orders drop primary key;
desc orders;
alter table orders add constraint primary key(oid);
desc orders;
#--------------
show databases;
use dql;
show tables;
desc student_demo;
select * from student_demo;
select roll,marks from student_demo;
# roll, subject and marks of roll number 5
select roll,subject,marks from student_demo
where roll=5;
# roll, subject and marks of roll number 5 and roll 7
select roll,subject,marks from student_demo
where roll=5 or roll=7;
select roll,subject,marks from student_demo
where roll in (5,7);
select roll,subject,marks from student_demo
where roll!=5 and roll!=7;
select roll,subject,marks from student_demo
where roll not in (5,7);
#marks less than or equal to 90
select roll,marks from student_demo
where marks<=90;
# * 50-90
select * from student_demo
where marks>=50 and marks<=90;
select * from student_demo
where marks<=90 and marks>=50;

select * from student_demo
where marks between 50 and 90;
select * from student_demo
where marks between 90 and 50; # no output

select roll,marks,
 case when marks between 75 and 100 then "A"
      when marks between 60 and 74 then "B"
      when marks between 35 and 60 then "C"
      else "F"
      end as Grade 
from student_demo;

select addr from student_demo;
select distinct addr from student_demo; 
select distinct addr from student_demo
where addr like "%i";

select distinct addr from student_demo
where addr like "_u%";

select distinct addr from student_demo
where addr like "__n_";

select roll,marks from student_demo;

select roll as ID, 
marks as Original_Marks,
marks+1 as Increased_marks
from student_demo;

select roll ,
if(marks>75,"More than 75","Less than 75") as Job_ready
from student_demo;

select roll,marks from student_demo;

select roll,marks from student_demo 
where marks is not null
order by marks;

select roll,marks from student_demo 
where marks is not null
order by marks desc;

select roll,marks from student_demo 
where marks is not null
order by marks desc
limit 3;

select roll,marks from student_demo 
where marks is not null
order by marks desc
limit 2 offset 1; # limit row_count offset number_of_rows_to_skip

select roll,marks from student_demo 
where marks is null;

#-------------------
create database func;
use func;
select current_date(),current_time(),
current_timestamp(),now();

select date_format(current_date(),"%d-%M-%Y, %W");
select date_add(current_date(),interval 1 month);

select 
if(month(current_date())>6,"Second half","First half");

select extract(year from current_date()),
extract(month from current_date());

#----------- string functions
use dql;
select concat(roll," ",addr) from student_demo;
select length(addr) from student_demo;
select upper(addr),lower(addr)
from student_demo;

#---------------------
show tables;
select substring("SQL is fun to learn",15,5);

select replace("SQL is fun to learn fun fun","fun","great");

#-----------------
use dql;
show tables;
desc student_demo;
select * from student_demo;
select sum(marks),avg(marks),
min(marks),max(marks)
from student_demo;

select count(*),count(subject),
count(marks),count(roll) 
from student_demo;

select distinct subject
from student_demo;

select sum(marks),avg(marks)
from student_demo
where subject="Python";

select sum(marks),avg(marks)
from student_demo
where subject="Java";

select subject,sum(marks),avg(marks)
from student_demo
group by subject;
/*Here the rows are first grouped on the basis
of different subjects after that the sum and avg 
of different groups is calculated.
*/

select subject,sum(marks),avg(marks)
from student_demo
group by subject
having sum(marks)>100;
/*

*/
select subject,sum(marks),avg(marks)
from student_demo
group by subject
order by sum(marks) desc;

select subject,sum(marks),avg(marks)
from student_demo
group by subject
having sum(marks)>100
order by avg(marks) desc
limit 2 offset 1;

# give me only those students data who are from
# Pune and Nasik
select * from student_demo
where addr in ("Pune","Nasik");
# give me addr and avg marks
# of pune and nasik students only 
select addr,avg(marks) from student_demo
where addr in ("Pune","Nasik")
group by addr;
# show subjects and their highest marks
# for students not in delhi, filter students with max marks > 70,
# and sort highest to lowest 

select subject,max(marks) as Topper,
round(avg(marks),2)
from student_demo
where addr != "Delhi"
group by subject
having Topper>70
order by Topper desc;

#----------------------
# find students who scored more than average marks
# Scalar subquery
select * from student_demo
where marks>(select avg(marks) from student_demo);
# subquery
select avg(marks) from student_demo;

select * from student_demo;
# give me all the details of 
# students who lives in the same city as roll 1.

select * from student_demo
where addr=
(select addr from student_demo
where roll=1);
update student_demo set addr="Nasik"
where roll=1;
select * from student_demo
where addr=
(select addr from student_demo
where roll=1);

# Multi row subquery - returns a list of values
# used with operators - in, not in , all, any 
# find students who are in the same cities 
# where Python is taught.
select * from student_demo
where addr in
(select distinct addr from student_demo where
subject="Python");

select distinct addr from student_demo where
subject="Python";

#>Any
# find students who scored higher than at least 
# 1 person from Pune

select * from student_demo;
# any learner's marks greater than the minimum scored 
# marks of learner's from Pune.
select * from student_demo
where marks >Any(
select marks from student_demo
where addr="Pune" and marks is not null);
select marks from student_demo
where addr="Pune";
/*
56
56

96
*/
# all learner's marks greater than the maximum scored 
# marks of learner's from Pune.
select * from student_demo
where marks >All(
select marks from student_demo
where addr="Pune" and marks is not null);
select marks from student_demo
where addr="Pune";

# exists 
select * from student_demo
where exists( select *
from student_demo
where marks>=100);

select *
from student_demo
where marks>=99;

# correlated subquery (reference to the outer query)

select *
from student_demo s1
where marks > (select avg(marks)
from student_demo s2
where s1.subject=s2.subject);

select subject,avg(marks)
from student_demo
group by subject;
/*
Python	54.5000
Java	95.0000
HTML	85.0000
C	56.0000
Django	88.5000
JavaScript	65.0000
*/
select * from student_demo;
# Window function

select subject,avg(marks)
from student_demo
group by subject;
# here we cannot see individual student's marks anymore
# instead only see the grouped results.
/*
Syntax :
windows_function_name(expression) over
([partition by partition_expression,..]
 [order by order_by_expression[ASC/DESC],..]
 [window_frame_clause])
 ROW_NUMBER(),RANK(),LAG(),LEAD(),SUM(),AVG()
 expression is the column function operates on.
 OVER()
 PARTITION BY 
 ORDER BY
 window_frame_clause ROWS or RANGE UNBOUNDED PRECEDING etc.
*/
select * from student_demo;
select roll,marks,addr,subject,
avg(marks) 
over(partition by subject) as Avg_Marks_By_Subject
from student_demo
where marks is not null;
# rows are intact even though aggrgate operations are applied

# row_number
select roll,marks,addr,subject,
row_number() over(order by marks desc) as rank_number
from student_demo
where marks is not null;

select * from 
(select roll,marks,addr,subject,
row_number() over(order by marks desc) as rank_number
from student_demo
where marks is not null) s1
where rank_number in (2,3);

# rank - 
select roll,marks,addr,subject,
rank() over(order by marks desc) as rank_value
from student_demo
where marks is not null;
# dense_rank - same rank for ties but no gap
select roll,marks,addr,subject,
dense_rank() over(order by marks desc) as rank_value
from student_demo
where marks is not null;