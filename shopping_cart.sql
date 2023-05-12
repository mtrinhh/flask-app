

CREATE TABLE shopping_cart(
    id SERIAL PRIMARY KEY, 
    item_id INT REFERENCES items(id) ON DELETE CASCADE,
    quantity INT NOT NULL);

INSERT INTO shopping_cart(item_id, quantity) VALUES (1, 5);
INSERT INTO shopping_cart(item_id, quantity) VALUES (2, 10);

-- psql -U postgres -p 5433 itemsforhire -f shopping_cart.sql