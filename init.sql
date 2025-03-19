CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    adress VARCHAR(100),
    dob Date
);
