from us_visa.pipline.training_pipeline import TrainPipeline

train = TrainPipeline()
train.run_pipeline()

'''
## checking for adding api mongodb  
from us_visa.logger import logging
import os
from dotenv import load_dotenv
from us_visa.exception import USVisaException
import sys 


#logging.info("This is a demo script for US Visa project.")
load_dotenv()



mongodb_url = os.getenv('MONGODB_URL')
print(mongodb_url)

## handle exception check
try:
    a = 2/0
except Exception as e:
    raise USVisaException(e,sys)
'''