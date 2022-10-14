select 
    bc.id_transaction,
	bc.id_customer,
	bc.name_customer,
	bc.birthdate_customer,
	bc.gender_customer,
	bc.country_customer ,
	bc.date_transaction,
	bc.product_kategory,
	bc.product_transaction, 
	bc.amount_transaction 
 from dim_transaction_order bc;