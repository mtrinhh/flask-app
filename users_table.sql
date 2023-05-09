DROP TABLE IF EXISTS users

CREATE TABLE users(id SERIAL PRIMARY KEY, full_name TEXT NOT NULL, mobile INT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL);


INSERT INTO users(full_name, mobile, email, password) VALUES ('Michael Trinh', 34635564, 'example@example.com', 'user_password');
INSERT INTO users(full_name, mobile, email, password) VALUES ('David Sott', 34635564, 'example@example.com', 'user_password');
INSERT INTO users(full_name, mobile, email, password) VALUES ('Lauren James ', 34635564, 'example@example.com', 'user_password');

-- INSERT INTO users(full_name, mobile, email, password) VALUES ();
-- INSERT INTO users(full_name, mobile, email, password) VALUES ();
-- INSERT INTO users(full_name, mobile, email, password) VALUES ();


-- psql -U postgres -p 5433 itemsforhire -f users_table.sql