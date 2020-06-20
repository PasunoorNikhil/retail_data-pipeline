import sys
from config import DB_DETAILS
import read
def main():

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
    src_db_host,src_db_name,src_db_user,src_db_pass=src_db['DB_HOST'],src_db['DB_NAME'],src_db['DB_USER'],src_db['DB_PASS']
    trgt_db_host, trgt_db_name, trgt_db_user, trgt_db_pass = trgt_db['DB_HOST'], trgt_db['DB_NAME'], trgt_db['DB_USER'], \
                                                         trgt_db['DB_PASS']





if __name__=='__main__':
    main()
