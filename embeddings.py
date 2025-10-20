import subprocess
import kagglehub
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

path = kagglehub.dataset_download("sawarn69/glove6b100dtxt")
subprocess.run(["mv", f"{path}/", f"{dir_path}/data/embeddings"])