import os

save_dir                    = '/home/ubuntu/data/CloserLookFewShot/'
data_dir = {}
data_dir['CUB']             = './filelists/CUB/' 
data_dir['miniImagenet']    = './filelists/miniImagenet/' 
data_dir['omniglot']        = './filelists/omniglot/' 
data_dir['emnist']          = './filelists/emnist/'


os.makedirs(save_dir, exist_ok=True)
