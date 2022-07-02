

CREATE DATABASE e_commerce;

CREATE USER 'e_commerce_user'@'localhost' IDENTIFIED WITH mysql_native_password BY '123789';
GRANT ALL PRIVILEGES ON e_commerce.* TO 'e_commerce_user'@'localhost';           
FLUSH PRIVILEGES;

use e_commerce;

show tables;


CREATE TABLE customers (
           customer_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
           first_name  VARCHAR(50),
           last_name  VARCHAR(50)    
       ) ENGINE = InnoDB;
       
       
       
select * from customers;