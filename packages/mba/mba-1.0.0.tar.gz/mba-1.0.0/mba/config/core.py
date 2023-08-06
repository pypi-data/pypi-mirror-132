from pathlib import Path
from typing import Dict, List, Sequence

from pydantic import BaseModel
from strictyaml import YAML, load

import mba

# Project Directories
PACKAGE_ROOT = Path(mba.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = ROOT / "data"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "models"


class AppConfig(BaseModel):
    """
    Application-level config.
    """

    package_name: str
    db_username: str
    db_password: str
    db_host: str
    db_port: str
    db_schema: str

class DataConfig(BaseModel):
    """
    All configuration relevant to the data
    """

    aisle_table: str
    department_table: str
    product_table: str
    transaction_table: str
    merged_table: str
    association_table: str

    transaction_id_column_name:  str
    product_id_column_name:  str
    product_name_column: str
    day_of_week: str
    hour_of_day: str
    user_id_column_name: str
    order_number_for_user: str
    department_name_column: str
    department_id_column: str
    aisle_name_column: str
    aisle_id_column: str



class ModelConfig(BaseModel):
    """
    All configuration relevant to model
    training and feature engineering.
    """

    count: str
    min_support: float


class Config(BaseModel):
    """Master config object."""

    app_config: AppConfig
    data_config: DataConfig
    model_config: ModelConfig


def find_config_file() -> Path:
    """Locate the configuration file."""
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f"Config not found at {CONFIG_FILE_PATH!r}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")


def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        app_config=AppConfig(**parsed_config.data),
        data_config=DataConfig(**parsed_config.data),
        model_config=ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()


