import requests
from omegaconf import OmegaConf

conf = OmegaConf.load('request_config.yaml')

resp = requests.post(f"http://{conf['host']}:{conf['port']}/predict",
                     files={"file": open(conf['image_path'],'rb')})

print(resp.json()['class_name'])
