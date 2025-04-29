use ipl;
desc deliveries;
desc matches;
select * from deliveries;
select * from matches;
select count(*) from deliveries;
select count(*) from matches;
select count(id) from matches
where city="Delhi" and toss_decision="bat";

select distinct city from matches;

select distinct city from matches
where city like "%u%";
select distinct city from matches
where city like "%u_";

select substr("Rising Pune Supergiant",8,4) City;

select replace("Rising Pune Supergiant","Pune","Andheri") Team;

select min(win_by_runs),avg(win_by_runs),
max(win_by_runs) from matches;

select * from matches where win_by_runs=146;


select * from matches where win_by_runs=
   (select max(win_by_runs) from matches);

select count(coalesce(umpire3)) from matches;

select * from matches
where umpire3 is not null;

select min(win_by_runs),avg(win_by_runs),
max(win_by_runs) from matches;

select count(*) from matches where win_by_runs=14;
select count(*) from matches where win_by_runs<14;
select count(*) from matches where win_by_runs>14;

select id,win_by_runs,
case 
when win_by_runs>14 then "Won above average"
when win_by_runs=14 then "Won by average"
when win_by_runs>0 then "Won below average"
else "Tie"
end as Result
from matches;

select player_of_match,count(*) Awards_count
from matches
group by player_of_match
order by Awards_count desc
limit 5;
