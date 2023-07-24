# Write your MySQL query statement below

# with temp as(
select 
case
when id%2=0 then id-1 
when id=(select count(id) from seat) then id
else id+1
end as id , student 
from seat order by 1
# )

# select new as id , student from temp order by 1 

# # select count(id) from seat
