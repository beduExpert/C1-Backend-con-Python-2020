DROP DATABASE IF EXISTS Biblioteca;
CREATE DATABASE Biblioteca;
GRANT ALL PRIVILEGES ON Biblioteca.* TO Biblioteca@'%' IDENTIFIED BY 'Biblioteca';
GRANT ALL PRIVILEGES ON Biblioteca.* TO Biblioteca@'localhost' IDENTIFIED BY 'Biblioteca';
