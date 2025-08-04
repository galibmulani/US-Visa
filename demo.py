from us_visa.logger import logging
from us_visa.exception import USVisaException
import sys 

logging.info("This is a demo script for US Visa project.")


try:
    a = 2/0
except Exception as e:
    raise USVisaException(e,sys)