create database codinch;

use codinch;


create table customers(
	CustomerId int NOT NULL PRIMARY KEY,
    FirstName VARCHAR(15) NOT NULL,
    LastName VARCHAR(15) NOT NULL,
    Email VARCHAR(30),
    Address VARCHAR(50)
);
select* from customers;

create table products (
	productID int NOT NULL PRIMARY KEY,
	name varchar(30) not null,
	Description varchar(30),
	Price money,
	stockQuantity int not null
);
select * from products;

CREATE TABLE cart (
    cartId INT not null PRIMARY KEY,
    customerId int NOT NULL,
    productId INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (customerId) REFERENCES customers(CustomerId),
    FOREIGN KEY (productId) REFERENCES products(productID)
);
select * from cart;

create table orders(
	order_id int not null primary key,
	customer_id int not null,
	order_date date,
	total_price money,
	foreign key (customer_id) references customers(CustomerId)
);
select * from orders;

create table order_items(
	order_item_id int not null primary key,
	order_id int not null,
	product_id int not null,
	quantity int, 
	itemamount money,
	foreign key (order_id) references orders(order_id),
	foreign key (product_id) references products(productID)
);
select * from order_items;

INSERT INTO customers (CustomerId, FirstName, LastName, email, Address)
VALUES
(1, 'John', 'Doe', 'johndoe@example.com', '123 Main St, City'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '456 Elm St, Town'),
(3, 'Robert', 'Johnson', 'robert@example.com', '789 Oak St, Village'),
(4, 'Sarah', 'Brown', 'sarah@example.com', '101 Pine St, Suburb'),
(5, 'David', 'Lee', 'david@example.com', '234 Cedar St, District'),
(6, 'Laura', 'Hall', 'laura@example.com', '567 Birch St, County'),
(7, 'Michael', 'Davis', 'michael@example.com', '890 Maple St, State'),
(8, 'Emma', 'Wilson', 'emma@example.com', '321 Redwood St, Country'),
(9, 'William', 'Taylor', 'william@example.com', '432 Spruce St, Province'),
(10, 'Olivia', 'Adams', 'olivia@example.com', '765 Fir St, Territory');


INSERT INTO products (productID, name, Description, Price, stockQuantity)
VALUES
(1, 'Laptop', 'High-performance laptop', 1500.00, 5),
(2, 'Smartphone', 'Latest smartphone', 800.00, 10),
(3, 'Tablet', 'Portable tablet', 600.00, 15),
(4, 'Headphones', 'Noise-canceling', 300.00, 20),
(5, 'TV', '4K Smart TV', 150.00, 30),
(6, 'Coffee Maker', 'Automatic coffee maker', 900.00, 5),
(7, 'Refrigerator', 'Energy-efficient', 700.00, 10),
(8, 'Microwave Oven', 'Countertop microwave', 80.00, 15),
(9, 'Blender', 'High-speed blender', 70.00, 20),
(10, 'Vacuum Cleaner', 'Bagless vacuum cleaner', 120.00, 10);

INSERT INTO cart (cartId, customerId, productId, quantity)
VALUES
(1, 1, 1, 2),
(2, 1, 3, 1),
(3, 2, 2, 3),
(4, 3, 4, 4),
(5, 3, 5, 2),
(6, 4, 6, 1),
(7, 5, 1, 1),
(8, 6, 10, 2),
(9, 6, 9, 3),
(10, 7, 7, 2);

INSERT INTO orders (order_id, customer_id, order_date, total_price)
VALUES
(1, 1, '2023-01-05', 1200.00),
(2, 2, '2023-02-10', 900.00),
(3, 3, '2023-03-15', 300.00),
(4, 4, '2023-04-20', 150.00),
(5, 5, '2023-05-25', 1800.00),
(6, 6, '2023-06-30', 400.00),
(7, 7, '2023-07-05', 700.00),
(8, 8, '2023-08-10', 160.00),
(9, 9, '2023-09-15', 140.00),
(10, 10, '2023-10-20', 1400.00);

INSERT INTO order_items (order_item_id, order_id, product_id, quantity, itemamount)
VALUES
(1, 1, 1, 2, 1600.00),
(2, 1, 3, 1, 300.00),
(3, 2, 2, 3, 1800.00),
(4, 3, 5, 2, 1800.00),
(5, 4, 4, 4, 600.00),
(6, 4, 6, 1, 50.00),
(7, 5, 1, 1, 800.00),
(8, 5, 2, 2, 1200.00),
(9, 6, 10, 2, 240.00),
(10, 6, 9, 3, 210.00);


update products
set Price=800.00
where name='Refrigerator';

select * from products;


delete from cart where customerId = 3;
select * from cart;

Select * from products where Price<100;

Select * from products where stockQuantity>5;

select * from orders where total_price between 500 and 1000;

select * from products where name like '%r';

select * from cart where customerId = 5;

SELECT DISTINCT c.CustomerId, c.FirstName, c.LastName, c.Email
FROM customers c
JOIN orders o ON c.CustomerId = o.customer_id
WHERE YEAR(o.order_date) = 2023;


ALTER TABLE products
ADD category VARCHAR(30);

UPDATE products
SET category = CASE
    WHEN productID IN (1, 2, 3,4) THEN 'Electronics'
    WHEN productID IN (5, 6, 7) THEN 'Accessories'
    WHEN productID IN (8, 9, 10) THEN 'Appliances'
	END;
select * from products;


SELECT c.CustomerId, c.FirstName, c.LastName, SUM(o.total_price) AS TotalAmountSpent
FROM customers c
JOIN orders o ON c.CustomerId = o.customer_id
GROUP BY c.CustomerId, c.FirstName, c.LastName;


select customer_id, avg(total_price) as 'Average order amount' from orders group by customer_id;


SELECT customer_id, COUNT(*) as 'No. of Orders'
FROM orders
GROUP BY customer_id;

SELECT customer_id, MAX(total_price) AS max_order_amount
FROM orders
GROUP BY customer_id;


SELECT customer_id FROM orders
GROUP BY customer_id
HAVING SUM(total_price) > 1000;


SELECT * FROM products
WHERE productID NOT IN (SELECT productID FROM cart);


SELECT * FROM customers
WHERE CustomerId NOT IN (SELECT customer_id FROM orders);


SELECT name,
       (SELECT SUM(itemamount) FROM order_items WHERE product_id = p.productID) / 
       (SELECT SUM(itemamount) FROM order_items) * 100 AS revenue_percentage
FROM products p;


SELECT * FROM products
WHERE stockQuantity < (SELECT AVG(stockQuantity) FROM products);


select c.* from customers c
join orders o on c.CustomerId = o.customer_id
where o.total_price > (select avg (total_price) from orders);


