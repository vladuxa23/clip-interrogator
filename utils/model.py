from clip_interrogator import Config, Interrogator

config = Config(clip_model_name="ViT-L-14/openai", download_cache=True)

config.apply_low_vram_defaults()
config.caption_model_name = 'blip-large'
# config.cache_path = 'D:\\dev\\python\\project\\clip-interrogator\\cache\\clip'


interrogator = Interrogator(config)

if __name__ == '__main__':
    from PIL import Image

    image = Image.open("examples\\2.jpg").convert('RGB')
    image2 = Image.open("examples\\1.png").convert('RGB')

    print(interrogator.interrogate(image))
    print(interrogator.interrogate(image2))
