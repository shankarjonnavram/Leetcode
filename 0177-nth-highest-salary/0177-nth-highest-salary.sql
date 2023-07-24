CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select distinct t1.salary from (
      select salary , DENSE_RANK() over (order by salary desc) as rn from Employee
  )t1 where t1.rn =N
  );
END