import os
from datetime import date

DATABASE_NAME = 'US_VISA'
COLLECTION_NAME = 'visa_data'
MONGODB_URL_KEY = 'MONGODB_URL'
PIPELINE_NAME:str = 'usvisa'
ARTIFACT_DIR:str = 'artifact'
MODEL_FILE_NAME = 'model.pkl'
FILE_NAME:str = 'usvisa.csv' # load data file from mongodb and store filename as this file name
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'
 
'''Data Ingestion constants'''
DATA_INGESTION_COLLECTION_NAME:str ="visa_data"
DATA_INGESTION_DIR_NAME:str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR:str = 'feature_store'
DATA_INGESTION_INGESTED_DIR:str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

