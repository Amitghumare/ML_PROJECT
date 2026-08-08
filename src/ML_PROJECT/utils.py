import os
import sys
from src.ML_PROJECT.exception import CustomException
from src.ML_PROJECT.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")
def read_sql_data():
    logging.info("Reading database is started")
    try:
        mydb=pymysql.connect(host=host,user=user,password=password,db=db)
        logging.info("Connection establish:%s",mydb)
        df=pd.read_sql_query("select * from student",mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e,sys)