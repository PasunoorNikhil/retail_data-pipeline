import mysql.connector as mc
from mysql.connector import errorcode as ec

def get_mysqlconn(src_db):
    """ Method used to establish connection to Mysql database
        Takes arguments as Mysql host, db name, db user , db pass and establishes
        a connection and returns that connection"""
    db_host, db_name, db_user, db_pass=src_db['DB_HOST'],src_db['DB_NAME'],src_db['DB_USER'],src_db['DB_PASS']
    try:
        connection = mc.connect(user=db_user,
                                password=db_pass,
                                host=db_host,
                                db=db_name
                                )


    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        else:
            print(error)


    return connection


