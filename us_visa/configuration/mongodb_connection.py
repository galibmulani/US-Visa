import os
import sys
from us_visa.constants import MONGODB_URL_KEY,DATABASE_NAME
import pymongo
from us_visa.logger import logging
import certifi
from us_visa.exception import USVisaException
from dotenv import load_dotenv

ca = certifi.where()

load_dotenv()
class MongoDBClient:

    client=None
    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongodb_url_key = os.getenv(MONGODB_URL_KEY)
                if mongodb_url_key is None:
                    raise Exception(f'Environment Key: {MONGODB_URL_KEY} is not set')
                MongoDBClient.client = pymongo.MongoClient(mongodb_url_key,tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info('MongoDB connection successful.')
        except Exception as e:
            raise USVisaException(sys,e)
