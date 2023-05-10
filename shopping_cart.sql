

CREATE TABLE shopping_cart (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL,
    user_id INTEGER REFERENCES users(id)
);



-- psql -U postgres -p 5433 itemsforhire -f shopping_cart.sql