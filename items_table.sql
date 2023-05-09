-- DROP TABLE IF EXISTS items

CREATE TABLE items(id SERIAL PRIMARY KEY, item_name TEXT NOT NULL, price INT NOT NULL, image TEXT, qty INT NOT NULL);


INSERT INTO items(item_name, price, image, qty) VALUES ('Tall Vase', 400, 'https://www.ikea.com/au/en/images/products/tidvatten-vase-clear-glass__0528106_pe645656_s5.jpg?f=xxxs', 25 );
INSERT INTO items(item_name, price, image, qty) VALUES ('Medium Vase', 300, 'https://www.ikea.com/au/en/images/products/viljestark-vase-clear-glass__0640433_pe699813_s5.jpg?f=xl', 20 );
INSERT INTO items(item_name, price, image, qty) VALUES ('Short Vase', 200, 'https://www.ikea.com/au/en/images/products/beraekna-vase-clear-glass__0639826_pe699591_s5.jpg?f=xl', 15 );

-- INSERT INTO items(item_name, price, image, qty) VALUES ();
-- INSERT INTO items(item_name, price, image, qty) VALUES ();
-- INSERT INTO items(item_name, price, image, qty) VALUES ();


-- psql -U postgres -p 5433 itemsforhire -f items_table.sql