CREATE TABLE opinions (
    opinion_id SERIAL PRIMARY KEY,
    description TEXT,
    product_id int NOT NULL,
    FOREIGN KEY(product_id)
        REFERENCES products(id)
        ON DELETE CASCADE
);

INSERT INTO opinions(description, product_id) VALUES
    ('Fatalny produkt', 3),
    ('Smaczne', 4);

CREATE TABLE Comments (
    content_id SERIAL PRIMARY KEY,
    content TEXT,
    movie_id int NOT NULL ,

    FOREIGN KEY(movie_id)
        REFERENCES movies(id)
        ON DELETE CASCADE


CREATE TABLE ClientAddress (
        clients_address_id SERIAL PRIMARY KEY,
        city VARCHAR(64),
        street VARCHAR(255),
        house_nr VARCHAR(16),
        client_id int NOT NULL UNIQUE,
        FOREIGN KEY(client_id)
            REFERENCES clients(id)
            ON DELETE CASCADE
        );

INSERT INTO ClientAddress(client_id, city, street, house_nr) VALUES
         (1, 'Warszawa' , 'Okopowa' , '15'),
         (2, 'London' , 'Bakerstreet' , '30');

ALTER TABLE payments
    ADD ticket_id int NOT NULL UNIQUE ,
    ADD FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE;


ALTER TABLE payments
    ADD ticket_id int UNIQUE,
    ADD FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE;

 ALTER TABLE payments ALTER  ticket_id SET NOT NULL;

DROP TABLE payments;

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    ticket_id int NOT NULL UNIQUE,
    FOREIGN KEY(ticket_id)
        REFERENCES tickets(id)
        ON DELETE CASCADE
);


CREATE TABLE products_orders(
    id SERIAL PRIMARY KEY,
    order_id int NOT NULL,
    product_id int NOT NULL ,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE products_orders (
    id SERIAL PRIMARY KEY,
    order_id int NOT NULL REFERENCES orders(id),
    product_id int NOT NULL REFERENCES products(id)
);

INSERT INTO products_orders(order_id , product_id) VALUES
                                                       (3,1);


CREATE TABLE screening (
    id SERIAL PRIMARY KEY ,
    cinema_id int NOT NULL REFERENCES cinemas(id),
    movie_id int NOT NULL REFERENCES movies(id),
                       datetime timestamp
);

INSERT INTO screening(cinema_id, movie_id, datetime) VALUES (1, 2, '2023-01-01 18:05');

pip install psycopg2-binary

