

CREATE DATABASE e_commerce;

CREATE USER 'e_commerce_user'@'localhost' IDENTIFIED WITH mysql_native_password BY '123789';
GRANT ALL PRIVILEGES ON e_commerce.* TO 'e_commerce_user'@'localhost';           
FLUSH PRIVILEGES;

use e_commerce;

show tables;