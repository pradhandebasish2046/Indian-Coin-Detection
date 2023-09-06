from Indian_Coin_Detection.constants import *
from Indian_Coin_Detection.utils.common import read_yaml, create_directories
from Indian_Coin_Detection.entity.config_entity import (DataIngestionConfig,
                                                        TrainingConfig)

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        params = self.params # all the parameters present inside params.yaml file
        yolo_config_file_path_ = self.config.training.yolo_config_file_path
        create_directories([
            Path(training.root_dir)
        ])
        create_directories([training.trained_model_dir])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_dir=Path(training.trained_model_dir),
            yolo_config_file_path=Path(yolo_config_file_path_),
            params_epochs=params.EPOCHS,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config