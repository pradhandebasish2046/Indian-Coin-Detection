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
    source_URL: str
    local_data_file: Path
    unzip_dir: Path