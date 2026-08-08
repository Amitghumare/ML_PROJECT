from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.exception import CustomException
from src.ML_PROJECT.components.data_ingestion import DataIngestion
from src.ML_PROJECT.components.data_ingestion import DataIngestionConfig

import sys


if __name__=="__main__":
    logging.info("The execution has Started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e,sys)