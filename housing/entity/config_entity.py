from collections import namedtuple


#Config required to collect data
DataIngestionConfig = namedtuple('DataIngestionConfig',
['dataset_download_url','tgz_download_dir','raw_data_dir','ingested_train_dir',
    'ingested_test_dir'])

#Data Validation - Checking for Null, Outliers, etc
DataValidationConfig = namedtuple('DataValidationConfig',
['schema_file_path'])


#Feature Engineering(preprocessed_object_file_path - pickle file for F.E done)
DataTransformationConfig = namedtuple('DataTransformationConfig',
['add_bedroom_per_room', 'transformed_train_dir',
    'transformed_test_dir', 'preprocessed_object_file_path'])


#Training
ModelTrainerConfig = namedtuple('ModelTrainerConfig',[
    'trained_model_file_path','base_accuracy'
])


#Evaluation
#model_evaluation_file_path - contains model in Production to be compared with the current trained model
ModelEvaluationConfig = namedtuple('ModelEvaluationConfig', [
    'model_evaluation_file_path', 'time_stamp'
])


#Push the model
ModelPusherConfig = namedtuple('ModelPusherConfig',['export_dir_path'])


TrainingPipelineConfig = namedtuple('TrainingPipelineConfig', ['artifact_dir'])