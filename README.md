# links on main repo: 

https://huggingface.co/spaces/pharma/CLIP-Interrogator
https://github.com/pharmapsychotic/clip-interrogator


This is project for simple and local clip-interrogator usage with RESTapi (FastApi). 

For simple run, usage this command:

* for gpu:
    > docker run --gpus all -p 3040:3040 clip-interrogator

* for cpu only:
    > docker run -p 3040:3040 clip-interrogator