#customer

select 
	dto.id_transaction,
	dto.id_customer,
	dto.name_customer,
	dto.date_transaction,
	dto.product_kategory,
	dto.product_transaction, 
	dto.amount_transaction
from (
	select substr(x.date_transaction,0,8), x.id_customer, max(x.id_transaction) max_trans
	from dim_transaction_order  x
	group by substr(x.date_transaction,0,8), x.id_customer) xy
inner join dim_transaction_order dto 
on dto.id_transaction  = xy.max_trans;