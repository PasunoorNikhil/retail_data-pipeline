import pandas as pd
import psycopg2

from sqlalchemy import create_engine

def transfer_data(df_products,df_customers,df_product_revenue_dly,df_revenue_dly,trgt_db):
    """Method takes the target database details and also the data frames to be loaded to database
        and loads the data frames into the PostGres Database"""
    db_host, db_name, db_user, db_pass=trgt_db['DB_HOST'], trgt_db['DB_NAME'], trgt_db['DB_USER'], \
    trgt_db['DB_PASS']
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}')
    df_products.to_sql('dim_products', engine, if_exists='replace', index=False)
    df_customers.to_sql('dim_customer', engine, if_exists='replace', index=False)
    df_product_revenue_dly.to_sql('fact_product_revenue_dly', engine, if_exists='replace', index=False)
    df_revenue_dly.to_sql('fact_revenue_dly', engine, if_exists='replace', index=False)
    return