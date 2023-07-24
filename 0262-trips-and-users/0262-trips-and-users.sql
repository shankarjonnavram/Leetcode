# Write your MySQL query statement below


# unbanned clients and drivers 

with temp as(
select id,client_id,driver_id,city_id,status,request_at 
from trips t join users u on t.client_id = u.users_id 
join users u2 on t.driver_id = u2.users_id
and u.banned='No' and u.role='client' and u2.banned='No' and u2.role='driver')

# select * from temp

select request_at as Day, round(sum(completed)/(sum(tot)+sum(completed)),2) as 'Cancellation Rate' from (
select 
case when status!='completed' then 1 else 0 end as completed,
case when status ='completed' then 1 else 0 end as tot,
request_at
from temp ) t1 where request_at between '2013-10-01' and '2013-10-03' group by 1

