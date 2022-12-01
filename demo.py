from housing.pipeline.pipeline import  Pipeline
from flask import Flask
from housing.logger import logging
from housing.config.configuration import Configuration

def main():
    try:
        c = Configuration().get_data_transformation_config()
        print(c)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == '__main__':
    main()