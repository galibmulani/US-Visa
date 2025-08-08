import os
import sys
from us_visa.exception import USVisaException
from us_visa.data_access.usvisa_data import USVisaData
from us_visa.logger import logging
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from pandas import DataFrame
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise USVisaException(e,sys)
        
    def export_data_into_feature_store(self)->DataFrame:
        try:
            logging.info('Exporting data from mongodb')
            usVisa = USVisaData()
            dataframe = usVisa.export_collections_as_dataframe(collection_name=self.data_ingestion_config.collection_name)

            logging.info(f'Shape of DataFrame: {dataframe.shape}')
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f'Saving exported data into feature store path :{feature_store_file_path}')
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        
        except Exception as e:
            raise USVisaException(e,sys)
        
    def split_data_into_train_test(self,dataframe:DataFrame)->None:
        try:
            train_set,test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info('Performed train test split on the dataframe')
            logging.info(
                "Existed split_data_into_train_test on the dataframe"
            )
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info(f'Exporting train and test file path')
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info(f'Exported train and test file path')

        except Exception as e:
            raise USVisaException(e,sys) from e
        

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        logging.info('Entered initiate_data_ingestion method of Data_Ingestion class')

        try:
            dataframe = self.export_data_into_feature_store()

            logging.info('Got the data from mongodb')

            self.split_data_into_train_test(dataframe)

            logging.info('Performed train test split on the dataset')

            logging.info(
                'Exited initiate_Data_ingestion of Data_Ingestion class'
            )

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)

            logging.info(f'Data Ingestion Artifact:{data_ingestion_artifact}')
            return data_ingestion_artifact;
    
        except Exception as e:
            raise USVisaException(e,sys)