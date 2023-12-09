# URUCHOMIENIE

# psql -h localhost -U postgres -W -d postgres

# ALTER USER postgres WITH PASSWORD 'coderslab';


# //////////////////// COMENDY

# \l listuje bazy danych
# CREATE DATABASE nazwa_bazy_danych_db ; - dodaje baze danych
# \c nazwa_bazy_danych_db - wyswietla baze danych
# \d - wyswietla tabele
# \d nazwa_tabeli - podglad tabeli


# //// TWORZENIE TABELI Z WIERSZAMI I OPISEM TYPU DANYCH

# CREATE TABLE products (
#     id SERIAL PRIMARY KEY,
#     name TEXT NOT NULL,
#     description TEXT,
#     price DECIMAL(5, 2) NOT NULL
# );
#
# CREATE TABLE orders (
#     id SERIAL PRIMARY KEY,
#     description TEXT
# );
#
#
#
# CREATE TABLE clients (
#     id SERIAL PRIMARY KEY,
#     name TEXT NOT NULL,
#     surname TEXT NOT NULL
# );
#
# CREATE TABLE cinemas (
#     id SERIAL PRIMARY KEY,
#     name text NOT NULL,
#     address TEXT NOT NULL
# );
#
# CREATE TABLE movies ( id SERIAL PRIMARY KEY, name TEXT NOT NULL, description TEXT NULL, rating INTEGER NOT NULL);
#
# CREATE TABLE tickets (
#     id SERIAL PRIMARY KEY,
#     quantity INT NOT NULL,
#     price DECIMAL(5, 2)
# );
#
# CREATE TABLE payments (
#     id SERIAL PRIMARY KEY,
#     type VARCHAR(20) NOT NULL,
#     date TIMESTAMP WITH TIME ZONE NOT NULL
# );

# /// DODAWANIE WIERSZY SO KOLUMN TU DO TABELI CLIENTS
#
# INSERT INTO clients (name, surname) VALUES ('Marian', 'Kowalski');
# INSERT INTO clients (name, surname) VALUES ('Anna', 'Nowak');
# INSERT INTO clients (name, surname) VALUES ('Fabian', 'Duda');
# INSERT INTO clients (name, surname) VALUES ('Arkadiusz', 'Czerepach');
# INSERT INTO clients (name, surname) VALUES ('Paweł', 'Kozioł');
# SELECT * FROM clients;
# SELECT * FROM clients ORDER BY name;
# SELECT * FROM clients ORDER BY name ASC;
# SELECT * FROM clients ORDER BY name DESC;
# 12:23
# INSERT INTO products (name, description, price) VALUES ('Smartfon', 'Xiaomi 12', 800);
# INSERT INTO products (name, description, price) VALUES ('Słuchawki', 'Marshal', 200.99);
# INSERT INTO products (name, description, price) VALUES ('Monitor', 'Samsung 32 cale', 699.99);
# INSERT INTO products (name, description, price) VALUES ('Podkładka pod mysz', NULL, 19.99);
# INSERT INTO products (name, price) VALUES ('Spray do czyszczenia klawiatury', 29.99);
# 12:26
#
# //// SELEKCJA - sposob wyswietlania
#
# SELECT * FROM products WHERE price > 500;
# SELECT * FROM products WHERE price < 500;
# SELECT * FROM products WHERE name LIKE '%y%';
# SELECT * FROM products WHERE name LIKE 'S%';
# 12:29
# INSERT INTO orders (description) VALUES ('Wysłać kurierem');
# INSERT INTO orders (description) VALUES ('Zamówienie dla organizacji charytatywnej - dać zniżkę 20%');
# INSERT INTO orders (description) VALUES (NULL);
# SELECT * FROM orders;
# SELECT * FROM orders WHERE description > 'X';
# SELECT * FROM orders WHERE description < 'X';

# zadanie 3 i 4 Podstawy sql - dodawanie i wybieranie danych
#
# dodanie kin :
#
# INSERT INTO cinemas (name, address) VALUES ('Nowe Horyzonty', 'Wrocław');
# INSERT INTO cinemas (name, address) VALUES ('Multikino', 'Warszawa');
# INSERT INTO cinemas (name, address) VALUES ('Cinema City', 'Kraków');

# INSERT INTO movies (name, description, rating) VALUES ('Star Wars', 'Starszy człowiek rekrutuje młodego rolnika do sekty', 8);
# INSERT INTO movies (name, description, rating) VALUES ('Star Trek', 'Jak Star Wars, ale bez mocy', 6);
# INSERT INTO movies (name, description, rating) VALUES ('Kevin sam w domu', NULL, 10);

# INSERT INTO tickets (quantity, price) VALUES (1, 19.5);
# INSERT INTO tickets (quantity, price) VALUES (1, 12.5);
# INSERT INTO tickets (quantity, price) VALUES (2, 25);

# INSERT INTO payments (type, date) VALUES ('visa', '2023-12-09 14:00');
# INSERT INTO payments (type, date) VALUES ('mastercard', NOW());

# Podstawy sql - zamiana i usuwanie danych
# ZAD 1 I 2

# DELETE FROM products;
# SELECT * FROM products;
# INSERT INTO products (name, description, price) VALUES ('Smartfon', 'Xiaomi 12', 800);
# INSERT INTO products (name, description, price) VALUES ('Słuchawki', 'Marshal', 200.99);
# INSERT INTO products (name, description, price) VALUES ('Monitor', 'Samsung 32 cale', 699.99);
# INSERT INTO products (name, description, price) VALUES ('Podkładka pod mysz', NULL, 19.99);
# INSERT INTO products (name, price) VALUES ('Spray do czyszczenia klawiatury', 29.99);
# SELECT * FROM products;
# DELETE FROM products WHERE id = 6;
# SELECT * FROM products;
#
# DELETE FROM products WHERE name LIKE 'S%';
# SELECT * FROM products;


# SELECT * FROM products;
# UPDATE products SET price=799.99;
# SELECT * FROM products;
# UPDATE products SET price=24.50 WHERE id=9;
# SELECT * FROM products;

# SELECT * FROM movies;
# UPDATE movies SET rating = 7 WHERE name LIKE 'S%';
# SELECT * FROM movies;
# UPDATE movies SET rating = 5, description = 'Młody psychopata broni swojego domu' WHERE id=3;
# SELECT * FROM movies;

# dodawanie kolumn i usuwanie

# ALTER TABLE products ADD rating DECIMAL(3, 2) NULL;
# SELECT * FROM products;
# UPDATE products SET rating = 8.5 WHERE id=8;
# SELECT * FROM products;
# ALTER TABLE products DROP COLUMN rating;
# SELECT * FROM products;
#
# ALTER TABLE products ADD rating DECIMAL(3, 2) NOT NULL;
# -- powyższe skończy się błędem!
#
# ALTER TABLE products ADD rating DECIMAL(3, 2) NOT NULL DEFAULT 7.77;
# -- powyższe zadziała
#
# exercises_db=# SELECT * FROM products;

# ALTER TABLE cinemas ADD seats INTEGER NULL;
# SELECT * FROM cinemas;
# UPDATE cinemas SET seats = 200 WHERE id IN (1, 3);
# UPDATE cinemas SET seats = 150 WHERE id = 2;
# SELECT * FROM cinemas;
#


