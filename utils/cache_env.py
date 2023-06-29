import os

os.environ['HF_HOME'] = f'{os.getcwd()}\\cache'
os.environ['TRANSFORMERS_OFFLINE'] = 'True'
os.environ['HF_DATASETS_CACHE'] = f'{os.getcwd()}\\cache'
os.environ['TRANSFORMERS_CACHE'] = f'{os.getcwd()}\\cache'
os.environ['TORCH_HOME '] = f'{os.getcwd()}\\cache'
os.environ['HUGGINGFACE_HUB_CACHE  '] = f'{os.getcwd()}\\cache'
os.environ['OPEN_CLIP_CACHE'] = f'{os.getcwd()}\\cache'
