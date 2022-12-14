

______________________________________________________________________

<div align="center">

# Your Project Name

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: Hydra" src="https://img.shields.io/badge/Config-Hydra-89b8cd"></a>
<a href="https://github.com/ashleve/lightning-hydra-template"><img alt="Template" src="https://img.shields.io/badge/-Lightning--Hydra--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/paper/2020)

</div>

## Description

Torch Serve to scale serving with workers

## How to run

Model - resnet18 was used for training with hardware - 1 x g4dn.xlarge nodes 
Max Epochs reached - 25

Torch Serve commands-
```
docker run -it --rm --net=host -v `pwd`:/opt/src pytorch/torchserve:latest bash
cd /opt/src
torchserve --start --model-store model_store --models cifar=cifar_basic.mar --ts-config  config.properties
```

Run tests with command -
```

cd test_serve
python3 -m pytest --host 35.78.219.103 -s

```
Test Results- TORCHSERVE.md

Model Explainability for cat.png-

<img src="cat_integrated_gradient.png?raw=true">




