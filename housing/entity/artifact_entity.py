from collections import namedtuple

'''This File is an output for each component'''

DataIngestionArtifact = namedtuple('DataIngestionArtifact',
['train_file_path','test_file_path','is_ingested','message'])

DataValidationArtifact = namedtuple('DataValidationArtifact',
['schema_file_path','report_file_path','report_page_file_path','is_validated','message'])