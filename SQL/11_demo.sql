show databases;
create database a351_day;
show databases;

use a351_day;

create table student
( sid int,
  sname varchar(30),
  smarks decimal(5,2),
  dob date
);
show tables;
describe student;

insert into student(sid,sname,smarks,dob)
values
(1,"Tom",23,"2023-12-23");

select * from student;

insert into student(sid,sname,smarks,dob)
values
(2,"Jerry",23,"2023-12-22"),
(3,"Ariel",23,"2022-12-12"),
(null,"Harry",null,"2023-12-24");

select * from student;

insert into student(sname,smarks,dob,sid)
values
("Potter",24,null,5);

select * from student;

insert into student(sname,smarks)
values
("Hermoine",24);

select * from student;

show databases;
show tables;

#------------------- constraint 

/*
 hi my name
is 
jdfn
*/
# applying contraints
create table employee
( id int primary key,
  sname varchar(30) not null,
  phn_no varchar(15) unique,
  city varchar(30) default "Mumbai",
  age int check(age>18)
);

describe employee;

show tables;

select * from employee;

insert into employee(id,sname,phn_no,city,age)
values
(1,"Ariel","9090909090","Mumbai",35);

select * from employee;

update employee
set city="Delhi"
where id=1;

select * from employee;

delete from employee
where id=1;

select * from employee;

#-------- guess whether record will be inserted or not

insert into employee(id,sname,phn_no,city,age)
values
(1,null,"9090909090","Mumbai",35); # no,null failed

insert into employee(id,sname,phn_no,city,age)
values
(1,"Ariel","9090909090","Mumbai",5); # no, check failed

insert into employee(id,sname,phn_no,city,age)
values
(1,"Ariel","9090909090","Delhi",25); # yes

insert into employee(id,sname,phn_no,city,age)
values
(1,"Ariel","9090909090","Delhi",25); # no, duplicate

select * from employee;

insert into employee(id,sname,phn_no,city,age)
values
(2,"Ariel","9090909090","Delhi",25); # no, duplicate

insert into employee(id,sname,phn_no,age)
values
(2,"Ariel","9898989898",25);

select * from employee; # default applied

#-----------------------
insert into employee(id,sname,phn_no,age,city)
values
(3,"Ariel",null,25,null);

select * from employee;

#------------------------

show tables;

describe student;

# alter

select * from student;

alter table student 
add constraint primary key(sid); # not applied

delete from student;

select * from student;

#------- 
 # rename table
 alter table student
 rename to students;

show tables;

# applying primary key 
alter table students
add constraint primary key(sid);

describe students;

alter table students
modify column sname varchar(50) not null; # added not null

describe students;

alter table students
modify column sname varchar(50); # removed not null

describe students;

alter table students
add column email varchar(50) after sname;

describe students;

alter table students
rename column email to semail;

describe students;

alter table students
add constraint unq_email unique(semail);

describe students;

alter table students
drop constraint unq_email;

describe students;

alter table students
add constraint chk_marks 
check(smarks>0.00 and smarks<100.00);

describe students;

show create table students;

alter table students
alter column dob
set default "2023-12-23";

describe students;

alter table students
alter column dob drop default;

describe students;

# foreign key constraint

create table departments
( dept_id int primary key,
 dept_name varchar(20) not null,
 sid int,
 constraint for_sid
 foreign key(sid) references students(sid)
);
describe students;

describe departments;

select * from students;
select * from departments;

insert into departments(dept_id,dept_name,sid)
values
(100,"Electronics",1);
# parent not there so child cannot be inserted.
select * from departments;

# so 1st insert parent then child
insert into students(sid,sname,semail,smarks,dob)
values
(1,"Abhi","abc123@gmail.com",78,"2012-12-01");

insert into departments(dept_id,dept_name,sid)
values
(100,"Electronics",1);
#--------------

delete from students 
where sid=1;

# first delete child, then delete parent

delete from departments
where sid=1;

delete from students 
where sid=1;

#--------------

alter table departments
drop constraint for_sid;

insert into departments(dept_id,dept_name,sid)
values
(200,"Electronics",3);

truncate table departments;
select * from departments;
alter table departments
add constraint for_sid
foreign key(sid) references students(sid);

#-------------------------

show databases;

use dql;

show tables;

select * from student_demo;

desc student_demo;
# all data of roll number 5 
select * from student_demo
where roll=5;

select * from student_demo;

select * from student_demo
where roll=5 or roll=7;

select * from student_demo
where roll in (5,7);

select roll,addr from student_demo
where roll not in (5,7);

select roll,marks from student_demo
where marks<90;

#---------------------------------- 18-9-2026
select * from student_demo;

select roll,marks from student_demo
where marks>50 and marks<90;

select roll,marks from student_demo
where marks between 50 and 90;

select roll,marks from student_demo
where marks<90 and marks>50;

select roll,marks from student_demo
where marks between 90 and 50; #ghggj

select roll,marks from student_demo;

select roll,marks,
case 
 when marks between 75 and 100 then "A"
 when marks between 60 and 74 then "B"
 when marks between 35 and 59 then "C"
 else "F"
end as  Grade # as is optional
from student_demo;

select addr from student_demo;

select distinct addr from student_demo;

select distinct addr from student_demo
where addr like "%i";

select distinct addr from student_demo
where addr like "_u%";

select distinct addr from student_demo
where addr like "_u__";

select roll,marks from student_demo;

select roll,marks as old_marks,
marks+10 as increased_marks from student_demo;

select roll,marks from student_demo;

describe student_demo;

select roll,marks,
if(marks>75,"Yes","No") JobReady
from student_demo;

select roll,marks from student_demo
where marks is not null
order by marks; # ascending

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
limit 4 offset 3;


#------------------------------- 22-09-2026

show databases;

use window_fun;

show tables;

select * from employee;

select dept_name as department,count(dept_name) as count
from employee
group by dept_name;

# find the total salary of each department
# find the average salary of each department
select dept_name as department,
sum(salary) as TotalSalary,
avg(salary) as AverageSalary
from employee
group by dept_name;

# department names with total salary > 20000
select dept_name as department,
sum(salary) as TotalSalary
from employee
group by dept_name
having TotalSalary>20000; # sum(salary)>20000

select dept_name as department,
sum(salary) as TotalSalary
from employee
group by dept_name
having TotalSalary>20000
order by TotalSalary desc;

# find highest salary in each department
# find departments with more than 4 employees

select dept_name as department,
max(salary) as MaxSalary
from employee
group by dept_name
order by MaxSalary desc;

select dept_name as department,
count(emp_id) as CountEmp
from employee
group by dept_name
having CountEmp>4
order by CountEmp;

select dept_name as department,
count(emp_id) as CountEmp
from employee
where dept_name in ("HR","Finance")
group by dept_name
having CountEmp>4
order by CountEmp;

#-------------------------------

# windows functions

select dept_name as Department,
emp_id, emp_name,salary,
max(salary) over(partition by dept_name order by salary desc) as MaxSalary,
row_number() over(partition by dept_name order by salary desc) as rowNumber,
rank() over(partition by dept_name order by salary desc) as rank_,
dense_rank() over(partition by dept_name order by salary desc) as denseRank_,
lag(salary) over(partition by dept_name order by salary desc) as lag_,
lead(salary) over(partition by dept_name order by salary desc) as lead_
from employee; 

#--------------------

select dept_name as Department,
emp_id, emp_name,salary,
row_number() over(order by salary desc) as rowNumber,
lead(salary) over(order by salary desc) as lead1_
from employee; 

select * from employee;

#------------------------ Subquery
use dql;
show tables;
select * from student_demo;

select * from student_demo
where marks>(select avg(marks) from student_demo);

select * from student_demo
where marks>69.18;

# give me students list who live in the 
# same city as roll no 1.

select * from student_demo
where addr in (
select addr from student_demo
where roll=1);

# give me details of all the students
# who lives in the city where python is taught.
select * from student_demo where
addr in(
select distinct addr from student_demo
where subject="Python");

# total number of rows in a table
select count(*) from student_demo;
describe student_demo; #number of columns and types

# give me details of all the students
# who doesnot live in the city where python is taught.

select * from student_demo where
addr not in(
select distinct addr from student_demo
where subject="Python") ;

# give me all the details of students
# who have scored higher than any student of pune
/*
56
99
96
*/
select * from student_demo where
marks > ( select min(marks) from
student_demo where addr="Pune"
);
select * from student_demo where
marks > Any( select marks from
student_demo where addr="Pune" and marks is not null
);
# give me all the details of students
# who have scored higher than every student of pune

select * from student_demo where
marks > ( select max(marks) from
student_demo where addr="Pune"
);

select * from student_demo where
marks > All( select marks from
student_demo where addr="Pune" and marks is not null
);

select marks,addr from student_demo
order by marks desc;

# exists
select *from student_demo
where exists(
select 1 from student_demo
where addr="Gurgaon");

#-------------

show databases;

use new_data_gh;

show tables;

select * from employee_j;

select * from department_j;

# give me the name of department d3
select dept_name from department_j
where dept="d3";

# give me address of varun.
select emp_add from employee_j
where emp_name="varun";

# give me the name of employee who works in HR dept
select emp_name from employee_j
where emp_no=(
select emp_no from department_j
where dept_name="HR");

# aliases 

select * from 
employee_j,department_j; # cross join

select * from 
employee_j cross join department_j;

select d.emp_no,e.emp_name from 
employee_j e inner join department_j d
on e.emp_no=d.emp_no;

select e.emp_no,e.emp_name,e.emp_add,
d.dept,d.dept_name,d.emp_no from 
employee_j e left join department_j d
on e.emp_no=d.emp_no;

select e.emp_no,e.emp_name,e.emp_add,
d.dept,d.dept_name,d.emp_no from 
employee_j e right join department_j d
on e.emp_no=d.emp_no;

select * from 
employee_j e natural join department_j d
where d.dept_name="HR";

select e.emp_name from 
employee_j e inner join department_j d
on e.emp_no=d.emp_no and
d.dept_name="HR";

select * from student_j;

select distinct t1.s_id from 
student_j t1 cross join student_j t2
where t1.s_id=t2.s_id and
t1.c_id<>t2.c_id; #!=

select distinct t1.s_id from 
student_j t1 inner join student_j t2
on t1.s_id=t2.s_id and
t1.c_id<>t2.c_id;

#---------- 05-10-- casestudy
CREATE DATABASE icecreamshop;
USE icecreamshop;

CREATE TABLE category (
id INT PRIMARY KEY,
name VARCHAR(50) NOT NULL
);



