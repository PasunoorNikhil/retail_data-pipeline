import pandas as pd

def process_data(conn):
    """Method takes connection to MySql db and the data is processed and stored in data frames which are returned """


    df_products = pd.read_sql("SELECT CURRENT_TIMESTAMP()+0 AS 'batch_id',curdate() AS 'batch_date', product_id ,product_name,\
                                 product_price, category_id, category_name, department_id, department_name\
                                 FROM products p JOIN categories c ON p.product_category_id=c.category_id\
                                 JOIN departments d ON c.category_department_id=d.department_id",conn)

    df_customers = pd.read_sql("SELECT customer_id, customer_fname, customer_lname, customer_email,\
                                   customer_password, customer_street, customer_city, customer_state,\
                                   customer_zipcode, CURDATE() as batch_date,CURRENT_TIMESTAMP()+0  as batch_id FROM customers",
                                   conn)
    df_product_revenue_dly = pd.read_sql("SELECT DATE(order_date)+0 AS 'date_id',order_item_product_id as 'product_id',\
                              ROUND(SUM(CASE WHEN order_status in ('CLOSED','COMPLETE') THEN order_item_subtotal END),0) AS 'product_revenue',\
                              ROUND(SUM(CASE WHEN order_status in ('PROCESSING', 'PENDING','PENDING_PAYMENT') THEN order_item_subtotal END),0) AS'outstanding_revenue'\
                              FROM orders o JOIN order_items oi ON o.order_id=oi.order_item_order_id\
                              GROUP BY order_date,order_item_product_id", conn)
    df_revenue_col = pd.read_sql("SELECT DATE(order_date)+0 AS 'date_id',SUM(order_item_subtotal) AS 'revenue'\
                              FROM orders o JOIN order_items oi ON o.order_id=oi.order_item_order_id\
                              where order_status IN ('CLOSED','COMPLETE') GROUP BY order_date",conn)

    # Dataframe for rest of the columns in fact_revenue_dly table
    df_revenue_count_cols = pd.read_sql("SELECT DATE(order_date)+0 AS 'date_id',\
                        COUNT(order_id) AS'total_order_count',\
                        ROUND(SUM(order_status in ('CLOSED','COMPLETE')),0)AS 'revenue_order_cnt',\
                        ROUND(SUM(order_status='CANCELED'),0) AS'cancelled_order_cnt',\
                        ROUND(SUM(order_status in ('PROCESSING', 'PENDING','PENDING_PAYMENT')),0) AS 'outstanding_order_cnt'\
                        FROM orders GROUP BY order_date", conn)

    # Dataframe for fact_revenue_dly table(merging both revenue and counts)
    df_revenue_dly = pd.merge(df_revenue_col, df_revenue_count_cols,how='inner', on='date_id')

    return (df_products,df_customers,df_product_revenue_dly,df_revenue_dly)