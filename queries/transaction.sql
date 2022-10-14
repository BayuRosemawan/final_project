#transaction_  

select 
    dto.id_transaction,
	dto.id_customer,
	dto.name_customer,
	dto.date_transaction,
	dto.product_kategory,
	dto.product_transaction, 
	dto.amount_transaction
 from dim_transaction_order dto;