CREATE DATABASE IF NOT EXISTS Ecommercedb;
CREATE USER IF NOT EXISTS 'aicha'@'localhost' IDENTIFIED BY 'aicha_admin';
GRANT ALL PRIVILEGES ON Ecommercedb .* TO 'aicha'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'aicha'@'localhost';
FLUSH PRIVILEGES;
