CREATE TABLE customer (
   customer_id       SERIAL NOT NULL PRIMARY KEY,
   customer_name     VARCHAR(25)
);

CREATE TABLE ingredient (
   ingredient_name   VARCHAR(25) NOT NULL PRIMARY KEY,
   category          VARCHAR(15),
   quantity_on_hand  INT,
   price_per_serving FLOAT(2),
   CHECK
    ( category IN ('Nuts', 'Fruits', 'Chocolate', 'Baked', 'Milk', 'Mix-in', 'Base', 'Topping'))
);

CREATE TABLE recipe (
   recipe_id      SERIAL NOT NULL PRIMARY KEY,
   recipe_name    VARCHAR(25) NOT NULL,
   sizes          INT, 
   price          INT,
   CHECK
   ( sizes IN ('8', '12', '16'))
);

CREATE TABLE orders (
   tx_num            SERIAL NOT NULL PRIMARY KEY,
   order_date        DATE,
   customer_id       INT,
   employee          VARCHAR(25) NOT NULL,
   FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
   FOREIGN KEY(employee) REFERENCES employee(employee_name)
);


CREATE TABLE milkshake (
   shake_id          SERIAL NOT NULL PRIMARY KEY,
   recipe_id         INT, 
   tx_num            INT,
   employee          VARCHAR(25) NOT NULL,
   FOREIGN KEY(recipe_id) REFERENCES recipe(recipe_id),
   FOREIGN KEY(tx_num) REFERENCES orders(tx_num)
   FOREIGN KEY(employee) REFERENCES employee(employee_name)
);


CREATE TABLE customization (
   custom_id         SERIAL NOT NULL PRIMARY KEY,
   shake_id          INT,
   ingredient_name   VARCHAR(25),
   quantity          INT,
   FOREIGN KEY(shake_id) REFERENCES milkshake(shake_id),
   FOREIGN KEY(ingredient_name) REFERENCES ingredient(ingredient_name)
);

CREATE TABLE employee (
   employee_id    SERIAL NOT NULL PRIMARY KEY,
   employee_name  VARCHAR(25)
);

CREATE TABLE manager (
   manager_id       SERIAL NOT NULL PRIMARY KEY,
   employee_id      INT,
   manager_schedule  DATE,
   FOREIGN KEY(employee_id) REFERENCES employee(employee_id)
);

CREATE TABLE recipe_ingredient (
   in_recip       SERIAL NOT NULL PRIMARY KEY,
   recipe_id      INT,
   ingredient_id  VARCHAR(25),
   quantity       INT,
   FOREIGN KEY(recipe_id) REFERENCES recipe(recipe_id),
   FOREIGN KEY(ingredient_id) REFERENCES ingredient(ingredient_name)
);

CREATE TABLE staff (
   staff_id          SERIAL NOT NULL PRIMARY KEY,
   employee_id       INT,
   staff_role        VARCHAR(25),
   role_schedule     DATE,
   FOREIGN KEY(employee_id) REFERENCES employee(employee_id)
);