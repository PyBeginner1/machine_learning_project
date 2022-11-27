from housing.pipeline.pipeline import  Pipeline
from flask import Flask
from housing.logger import logging
from housing.config.configuration import Configuration

def main():
    try:
        data_val = Configuration().get_data_validation_config()
        print(data_val)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == '__main__':
    main()