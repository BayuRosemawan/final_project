#DB_queries

select  
	bt.id_transaction,
	bt.id_customer,
	bc.name_customer,
	bc.birthdate_customer,
	bc.gender_customer,
	bc.country_customer ,
	bt.date_transaction,
	bp."Product" product_kategory,
	bt.product_transaction product_transaction, 
	bt.amount_transaction 
from bigdata_transaction bt
left join bigdata_customer bc 
on bt.id_customer = bc.id_customer
left join bigdata_product bp 
on REPLACE( bp."Type", ' ', '')  = REPLACE(bt.product_transaction, ' ', '') ;