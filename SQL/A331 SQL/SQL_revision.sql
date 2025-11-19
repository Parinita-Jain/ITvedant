show databases;
use new_data_gh;
show tables;

create table stud
( id int , 
  name varchar(20),
  marks int
);
desc stud;
insert into stud(id,name,marks) values
(1,"Apple",10),
(2,"Ram",20),
(3,"Tom",30),
(4,"Jerry",40);



select avg(marks) from stud;
select id, name from stud where 
id in (select id from stud where marks >25);
select id from stud where marks >25;

update stud set
name="Tommy" where name="Tom";

create table cource
( c_id int,
  c_name varchar(20),
  id int
);
insert into cource(c_id,c_name,id)
values
(10,"english",1),
(20,"science",1),
(30,"maths",3),
(40,"hindi",3);
alter table stud
add constraint c check(marks>=0);
insert into stud(id,name,marks) values
(5,"Harry",-10);

alter table stud
add constraint primary key(id);

desc stud;

alter table cource
add constraint for_k 
foreign key(id) references stud(id);

desc cource;

select * from 
stud,cource
where stud.id=cource.id
and (cource.c_name="English" or cource.c_name="Maths");

select cource.id,stud.name from 
stud,cource
where stud.id=cource.id
and cource.c_name in ("English","Maths");

select cource.id,stud.name from 
stud natural join cource
where cource.c_name in ("English","Maths");

select cource.id,stud.name from 
stud inner join cource on
stud.id=cource.id
and cource.c_name in ("English","Maths");


