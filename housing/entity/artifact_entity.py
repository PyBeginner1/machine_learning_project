from collections import namedtuple

'''This File is an output for each component'''

DataIngestionArtifact = namedtuple('DataIngestionArtifact',
['train_file_path','test_file_path','is_ingested','message'])