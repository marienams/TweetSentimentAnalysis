#/Users/{user}/.kaggle
import kaggle

api = kaggle.api
api.authenticate()

api.dataset_download_files('kazanova/sentiment140', path='.', unzip=True)