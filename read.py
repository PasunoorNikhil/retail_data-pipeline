import mysql.connector as mc
from mysql.connector import errorcode as ec

def get_mysqlconn(db_host,db_name,db_user,db_pass):
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
    else:
        connection.close()

    return connection


