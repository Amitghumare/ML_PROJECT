from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("The execution has Started")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e,sys)