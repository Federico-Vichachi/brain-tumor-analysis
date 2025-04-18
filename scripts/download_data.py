import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    dataset = "miadul/brain-tumor-dataset"
    path = "data/"
    
    if not os.path.exists(path):
        os.makedirs(path)

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=path, unzip=True)
    
if __name__ == "__main__":
    download_dataset()