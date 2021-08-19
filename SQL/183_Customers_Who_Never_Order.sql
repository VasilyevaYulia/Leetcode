#Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

select Name as Customers from Customers
left join Orders 
on Orders.CustomerId = Customers.id 
where CustomerId is NULL;
