show databases;
create database a325;
show databases;
use a325;
create table student_info(
roll_no tinyint,
attendance bit,
pocket_money smallint);
show tables; # for showing the tables inside the selected database
/*for showing 
the tables inside 
the selected database
*/
#describe student_info; # gives metadata or schema i.e. data about data
desc student_info;
insert into student_info values(1,1,1000);
select * from student_info;
insert into student_info values(255,2,32767),
(256,2,32768),
(746898,8798376,698809);
select * from student_info;

create table product_d(
id int, pho_nu bigint,price decimal(5,2));
desc product_d;
create table fp_datatype(id float, re real);
desc fp_datatype;
insert into fp_datatype values(93788972509.746786798536,476843568376873687.853769873598);
select * from fp_datatype;
#-----
use a325;
create table employee_details
(id int, salary int ,work_hours decimal(2,1));

insert into employee_details values
(1, 20000,2.9),
(2,60000,4.6),
(3,50000,7.8),
(4,30000,3.2);
select * from employee_details;

create table dt(
dt date, ti time, dt_ti datetime);
insert into dt values('2025-04-16','09:48:48',"2025-04-16 09:48:48");
#give date in format yyyy-mm-dd
/*
*/
select * from dt;

create table student_c(
sname char(10), svname varchar(10));
desc student_c;
insert into student_c values
("ABC","DEF");
select * from student_c;
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
select roll,addr from student_demo;
select * from student_demo where roll=5;
select subject,marks from student_demo where roll=7;
select roll,marks from student_demo where marks<90;
select roll,marks from student_demo where marks>=50 and marks<=90;
select roll,marks from student_demo where marks between 50 and 90;
select roll,marks from student_demo where marks<=90 and marks>=50;
select roll,marks from student_demo where marks between 90 and 50;
# between works only in ascending order range
# case
select roll,
case when marks>=75 and marks<=100 then "very good"
     when marks>=60 and marks<75 then "good"
     when marks>=35 and marks<60 then "ok"
     else "Fail"
end Result # aliasing
from student_demo;

select * from student_demo where roll=1 or roll=2;
select * from student_demo where roll in (1,2);

select * from student_demo where roll not in (1,2);
select * from student_demo where roll<>1 and roll<>2;

select addr from student_demo;
select distinct addr from student_demo;

select distinct addr from student_demo
where addr like "%i";

select distinct addr from student_demo
where addr like "_u__";

select distinct addr from student_demo
where addr like "_u%";

select distinct addr from student_demo
where addr like "M%";

select distinct addr from student_demo
where addr like "____i";

select distinct addr from student_demo
where addr not like "____i";

select roll,marks from student_demo;

select roll,marks from student_demo
order by marks desc limit 3;

select roll,marks from student_demo
where marks is null;

select roll,marks from student_demo
where marks is not null
order by marks limit 5;

select roll,marks from student_demo
order by marks desc limit 3;
select roll,marks from student_demo
order by marks desc limit 1,2; 

# 

#constarints-------------------------------
/*
jhhf
hfjg
*/
show tables;
create table c(id int);
insert into c values("A");
insert into c values(1);
#-----------------------------------
create table u(id int unique,name varchar(30));
desc u;
insert into u values(1,"Harry");
select * from u;
insert into u values(1,"Tom");
insert into u values(2,"Harry");
select * from u;
insert into u values(null,"Harry");
select * from u;
insert into u values(null,"Harry");
select * from u;
insert into u values(0,"Harry");
select * from u;
insert into u values(0,"Harry");
select * from u;

create table n(id int not null,name varchar(30));
desc n;   
insert into n values(0,"Harry");
select * from n;
insert into n values(0,"Harry");
select * from n;
insert into n values(null,"Harry");
select * from n;
insert into n values(0,null);
select * from n;

# adhaar card number

create table u_n(id int unique not null,name varchar(30));
desc u_n;
create table p(id int primary key,name varchar(30));
desc p;
# 
create table po(an int primary key,
	pn varchar(20) unique not null,
	passport int unique not null);
desc po; 
drop table po;
create table po(an int unique not null,
	pn varchar(20) unique not null,
	passport int unique not null);
desc po; 

create table a(id int primary key auto_increment,name varchar(20));
desc a;
insert into a values(100,"Harry");
insert into a(name) values("Tom"),("Jerry"),("Potter"),("Sherry");
select * from a;

create table ch(id int primary key ,
			   age int,
               name varchar(20),
               check (age>18));
desc ch;
insert into ch values(1,16,"Harry");
select * from ch;
insert into ch values(1,19,"Harry");
select * from ch;
drop table ch;
create table ch(id int primary key ,
			   age int,
               name varchar(20),
               constraint check_age check (age>18));
drop table ch;
create table ch(id int primary key ,
			   age int check (age>18),
               name varchar(20));
drop table ch;
create table ch(id int,
			   age int,
               name varchar(20),
               check (age>18),
               primary key(id));
show create table ch;

create table d(id int , 
               name varchar(20),
			   city varchar(20) default "Mumbai");
desc d;   
insert into d values(1,"Harry","Pune");
select * from d;
insert into d values(1,"Harry",null);
select * from d;
insert into d(id,name) values(1,"Harry");
select * from d;
#-----
create table customers(
			id int primary key,
            name varchar(20));

create table orders(
			o_id int primary key,
            c_id int,
            constraint fo foreign key(c_id) references customers(id));
desc customers;
desc orders;
# child table insertion
insert into orders values(10,1); # error 
insert into customers values(1,"Harry");
insert into orders values(10,1);
select * from customers;
select * from orders;
# parent table deletion
delete from customers where id=1; # error
delete from orders where c_id=1;
delete from customers where id=1;
select * from customers;
insert into customers values(2,"Harry");
delete from customers where id=2;

#--------------
create table product_demo(
id int,
name varchar(20),
price int
);
desc product_demo;
show tables;
alter table product_demo rename to product1;
desc product_demo;
desc product1;
alter table product1 modify name varchar(50);
desc product1;
alter table product1 modify name varchar(50) not null;
desc product1;
alter table product1 add constraint chk_price check(price>0);
desc product1;
alter table product1 modify name varchar(50) default "Ariel";
desc product1;
alter table product1 modify price decimal(5,2) not null default 100.00;
desc product1;
alter table product1 add column email_1 varchar(100) after id;
desc product1;
alter table product1 drop column email_1;
desc product1;
alter table product1 drop column email;
desc product1;
alter table product1 change column id pid int;
desc product1;
alter table product1 change column price product_price int;
desc product1;
alter table product1 drop check chk_price;
alter table product1 add constraint primary key(pid);
desc product1;
alter table product1 drop primary key;
desc product1;
insert into product1 values(null,"April",234.78);
alter table product1 modify pid int;
desc product1;
insert into product1 values(null,"April",234.78);

create table course_p(
id int primary key,
sname varchar(20)
);
create table stud_p(
sid int primary key,
cid int);
alter table stud_p add constraint stud_p_f
foreign key(cid) references course_p(id);
desc course_p;
desc stud_p;
insert into stud_p values(1,10); # error
insert into course_p values(10,"April");
insert into stud_p values(1,10);
insert into stud_p values(1,20); # error
select * from stud_P;
select * from course_P;
delete from course_p where id=10; # error
delete from stud_p where cid=10;
delete from course_p where id=10;      

alter table stud_p drop constraint stud_p_f;
desc stud_p;
insert into stud_p values(1,20);
select * from course_p;
#---------------------------------------
create table str_demo(f_name varchar(20),l_name varchar(20));
insert into str_demo values("Tom","jeRRy"),("hArry","pOTTer");
select * from str_demo;
select concat(f_name," ",l_name) Name from str_demo;
select upper(f_name),lower(l_name),length(f_name) from str_demo;

select replace("Let us earn SQL","earn","learn") Replacement;
select substr("Let us earn SQL",8,4); # sub string

# maths functions
select round(1234.68579879,2);
select round(1234.68579879,-3);
select truncate(1234.68579879,2);
select truncate(1234.68579879,-2);
select floor(123.0);
select ceil(123.00000000000001);
select pow(2,5),sqrt(81),mod(29,3);
# 2*2*2*2*2, pow(2,64)
select pow(2,64);
select isnull(1*1),isnull(0*1),isnull(1/0),isnull(0/1);
select coalesce(null,null,null,null,10,null,null,20,30);
select coalesce(null,null,null,null,null,null);
create table aggregate_functions(i int);
insert into aggregate_functions values(1),(2),(3),(4),(5);
select max(i),min(i),count(i),avg(i),sum(i) 
from aggregate_functions;

select count(*) from aggregate_functions;
select greatest(1,2,56,78),least(1,2,56,78);

#-----------------------------------------
select current_date();

select date_format(current_date(),"%Y-%M-%D") as Formatted_date;

select current_date() as Today,
       Date_Add(current_date(),Interval 7 day) as Exam_Date,
       date_sub(current_date(),Interval 1 month) as last_month_date;

select datediff(current_date(),"2024-04-20"); # date difference

select case
	   when current_date>"2025-05-01" then "Quarter 2"
       else "Quarter1"
       end as Quarter_Comparison;
select current_time(),now();
select dayofweek(current_date()); #1- Sunday
select last_day(current_date());

select extract(Year from now()) Year,
       extract(Month from now()) Month,
       extract(Day from now()) Day,
       extract(Hour from now()) Hour,
       extract(Minute from now()) Minute,
       extract(Second from now()) Second;

select extract(Year from "2025-04-03") Year,
       year("2025-04-03"),
       month("2025-04-03"),
       day("2025-04-03");

select sysdate();
#---------------------------- group by having ---------
show databases;
use new_data_gh;
show tables;
desc cust_gh;
select * from cust_gh;

select distinct country from cust_gh;

select country,count(*) from cust_gh
group by country;

select * from cust_gh group by country;
select country,avg(age),min(age),max(age),count(age),sum(age) from cust_gh
group by country;

select country,avg(age)from cust_gh
group by country
having avg(age)>25;
select country,avg(age)from cust_gh
group by country
having avg(age)>25 and count(*)>2;

select country,avg(age)from cust_gh
group by country
having avg(age)>25
order by avg(age);

select country,avg(age)from cust_gh
where country like "U%"
group by country
having avg(age)>25
order by avg(age);

select * from cust_gh
where country like "U%";

#------------------------------------------------------------------
show tables;
desc employee_copy;
desc employee_sq;
select * from employee_copy;
select * from employee_sq;

select emp_salary from employee_sq 
order by emp_salary desc limit 1;

select max(emp_salary) from employee_sq;

select * from employee_sq where emp_salary=113000;

select * from employee_sq where emp_salary=max(emp_salary);
insert into employee_sq(emp_id,emp_name,emp_age,gender,emp_doj,
emp_dept,emp_city,emp_salary) values
(112,"Ammy",35,"F","2014-12-20","IT","Seatle",830000);

# subquery
select * from employee_sq 
where emp_salary=(select max(emp_salary) 
				  from employee_sq);

update employee_sq set emp_salary=900000 where emp_id=112;
select * from employee_sq;
select avg(emp_salary) from employee_sq;
delete from employee_sq where emp_id=112;

select avg(emp_salary) 
from employee_sq;

select * from employee_sq 
where emp_salary>(select avg(emp_salary) 
				  from employee_sq);

select * from employee_sq 
where emp_age>(select min(emp_age) 
				  from employee_sq);
select * from employee_sq 
where emp_id in (106,107,108,110,111);

select * from employee_sq 
where emp_id=106 or emp_id=107 or emp_id=108 or emp_id=110 or emp_id=111;

select * from employee_sq 
where emp_id in (select emp_id from employee_sq 
				 where emp_age>(select min(emp_age) 
				 from employee_sq));
                 
update employee_sq set emp_salary=emp_salary+3000
where emp_id in (select emp_id from employee_copy where emp_age>28);

update employee_sq set emp_salary=emp_salary+3000
where emp_id in (select emp_id from employee_sq where emp_age>28);

select * from employee_sq 
where emp_id in (select emp_id from employee_sq 
				 where emp_age>(select min(emp_age) 
				 from employee_sq));
delete from employee_sq 
where emp_id in (select emp_id from employee_copy where emp_age>28);

select * from products;
select * from orders;

select prod_id from products where prod_price>1000;

insert into orders 
select prod_id,prod_name,prod_price from products 
where prod_id in (select prod_id from products where prod_price>1000);

select * from teacher;
select * from student;

select age from teacher where age > all(select sage from student);

select age from teacher where age > any(select sage from student);

select age from teacher where not exists (select sage from student where sage>31);
#--------------------------------------------
show tables;
select * from employee_j;
select * from department_j;

select dept_name from department_j where dept="d3";

select dept_name from department_j where dept in ("d3");

select emp_add from employee_j where emp_name="varun";

# give the name of an employee working in HR department

select * from employee_j,department_j;
select * from employee_j cross join department_j;

select employee_j.emp_name from employee_j,department_j
where employee_j.emp_no=department_j.emp_no
and dept_name="HR";

select employee_j.emp_name from employee_j cross join department_j
where employee_j.emp_no=department_j.emp_no
and dept_name="HR";

select * from employee_j,department_j
where employee_j.emp_no=department_j.emp_no;

select * from employee_j natural join department_j
where department_j.dept_name="HR";

select * from employee_j inner join department_j
on employee_j.emp_no=department_j.emp_no
and dept_name="HR";

# left outer join
select * from employee_j left outer join department_j
on employee_j.emp_no=department_j.emp_no;
select * from employee_j right outer join department_j
on employee_j.emp_no=department_j.emp_no;

select * from employee_j left outer join department_j
on employee_j.emp_no=department_j.emp_no
union all
select * from employee_j right outer join department_j
on employee_j.emp_no=department_j.emp_no;

# self-join
show tables;
select * from student_j;

select distinct t1.s_id from student_j as t1,student_j as t2
where t1.s_id=t2.s_id and t1.c_id<>t2.c_id;