import sys
from config import DB_DETAILS
import read
import process
import write

def main():
    """ Main function from which connection to Source Database is established then
        the data is is processed and stored in data frames and the processed data frames
        are written to Target Database"""
    if len(sys.argv)==1:
        print("No arguments Passed")
        print(" To run use command python app.py dev")
        sys.exit()
    elif sys.argv[1]!= 'dev' and sys.argv[1]!='testing':
        print(" To run use command python app.py dev or python app.py testing ")
        sys.exit()
    env=sys.argv[1]
    db_details=DB_DETAILS[env]
    src_db=db_details['SOURCE_DB']
    trgt_db=db_details['TARGET_DB']
    print("Intializing connection to Mysql Database")
    mysql_conn=read.get_mysqlconn(src_db)
    print('Connection established to Mysql Database')
    print('Starting processing the data ')
    df_products,df_customers,df_product_revenue_dly,df_revenue_dly=process.process_data(mysql_conn)
    print('Finished processing the data ')
    print('Starting writing the data to PostGres Database')
    write.transfer_data(df_products,df_customers,df_product_revenue_dly,df_revenue_dly, trgt_db)
    print('Completed writing to Postgres')




if __name__=='__main__':
    main()
