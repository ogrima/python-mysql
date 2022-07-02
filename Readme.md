### A simple example using python and MySql

> pip install mysql-connector-python

#### Create DataBase and Tables

    

CREATE DATABASE e_commerce;
    
    CREATE USER 'e_commerce_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'THE_PASSWORD';
    GRANT ALL PRIVILEGES ON e_commerce.* TO 'e_commerce_user'@'localhost';           
    FLUSH PRIVILEGES;
    
    use e_commerce;    
    
    CREATE TABLE customers (
               customer_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
               first_name  VARCHAR(50),
               last_name  VARCHAR(50)    
           ) ENGINE = InnoDB;
           
    select * from customers;


### Running

> python ./src/index.py
