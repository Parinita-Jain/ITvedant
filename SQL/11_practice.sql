create database prac;
use prac;

create table t1(
sid int not null,
sname varchar(20) not null,
ph_no varchar(15) not null,
email_id varchar(50) not null,
city varchar(15) default "Mumbai",
marks decimal(5,2),

constraint pk_sid primary key(sid),
constraint uq_ph_no unique(ph_no),
constraint uq_email unique(email_id),
constraint chk_marks check(marks>0));

create table t2
( cid int primary key,
 cname varchar(20),
 sid int,
 constraint fo_t1_t2_sid foreign key(sid) references t1(sid)
);

create table t3
( cid int primary key,
 cname varchar(20),
 sid int);
 
 alter table t3 
 add constraint fo_t1_t3_sid foreign key(sid) references t1(sid);
 
 