import os

path = os.path.join(os.getcwd(), 'cache')
os.environ['HF_HOME'] = path
os.environ['TRANSFORMERS_OFFLINE'] = 'True'
os.environ['HF_DATASETS_CACHE'] = path
os.environ['TRANSFORMERS_CACHE'] = path
os.environ['TORCH_HOME '] = path
os.environ['HUGGINGFACE_HUB_CACHE  '] = path
os.environ['OPEN_CLIP_CACHE'] = path
