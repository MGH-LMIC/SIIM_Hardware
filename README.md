# SIIM_Hardware
Binary classification (hardware / No hardware) of fluoroscopy or X-ray images

## Prerequisites

- Python 3.7.+
- PyTorch 1.5.0+
- Torchvision 0.6.0+
- Pillow 7.1.2+
- Python Packages: ./requirements

## Demo

### 1. Docker installation
Follow the instrunction (https://docs.docker.com/).



### 2. Build image
$ git clone https://github.com/MGH-LMIC/SIIM_Hardware.git

$ cd SIIM_Hardware

$ sudo docker build . -t hardware_detection:1.0 -f docker_config/Dockerfile



### 3. Run demo
$ sudo docker run --name hardware_detection  -it hardware_detection:1.0 /bin/bash

$ python predict.py

OR

$ python predict.py "image_file_what_you_want_to_use"

