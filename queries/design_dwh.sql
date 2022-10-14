#design_DWH

DROP TABLE IF EXISTS dim_transaction_order;
CREATE TABLE dim_transaction_order (
	id_transaction INT NOT NULL,
	id_customer INT NOT NULL,
	name_customer VARCHAR(100),
	birthdate_customer VARCHAR(100),
	gender_customer VARCHAR(100),
	country_customer VARCHAR(100),
	date_transaction VARCHAR(100), 
	product_kategory VARCHAR(100),
	product_transaction VARCHAR(100),
	amount_transaction INT
	);