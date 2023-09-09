# Entity is the return type of the function

from dataclasses import dataclass
from pathlib import Path

# Creating the entity class

"""
frozen=True argument means that 
instances of this class will be 
immutable, meaning their attributes 
cannot be changed once they are created.
"""
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    unzip_dir: Path
    bucket_name: str
    file_name: str

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_dir: Path
    yolo_config_file_path: Path
    params_epochs: int
    params_image_size: list