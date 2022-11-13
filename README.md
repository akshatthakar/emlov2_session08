

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

What it does

## How to run

Model - vit_base_patch32_224 was used for training with hardware - 4 x g4dn.xlarge nodes and trainer as - FSDP
Max Epochs reached - 39

NVidia-smi dumps for 4 nodes available in github repo folder-

nvidia-smi


TensorBoard Url-
https://tensorboard.dev/experiment/roBN68p4TXyLJ0h2kJou1w

S3 Location for Best Model run-
https://s3.console.aws.amazon.com/s3/buckets/emlov2session6?region=ap-northeast-1&prefix=run_logs/&showversions=false

Install dependencies

```bash
# Commands to run on each GPU node

mkdir /home/ubuntu/build
cd /home/ubuntu/build
git clone https://github.com/akshatthakar/EML20_session06_assignment-.git
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
python3 -m pip install awscli
cd /home/ubuntu/build/EML20_session06_assignment-
python3 -m pip install -r requirements.txt


```
Commands run on each of the 4 nodes as per sequence/rank

```bash
# train on CPU

MASTER_PORT=29500 MASTER_ADDR='master node' WORLD_SIZE=4 NODE_RANK=0 nohup python3 src/train.py experiment=cifar trainer=fsdp trainer.devices=1 trainer.num_nodes=4 &

MASTER_PORT=29500 MASTER_ADDR='master node'  WORLD_SIZE=4 NODE_RANK=1 nohup python3 src/train.py experiment=cifar trainer=fsdp trainer.devices=1 trainer.num_nodes=4 &

MASTER_PORT=29500 MASTER_ADDR='master node'  WORLD_SIZE=4 NODE_RANK=2 nohup python3 src/train.py experiment=cifar trainer=fsdp trainer.devices=1 trainer.num_nodes=4 &

MASTER_PORT=29500 MASTER_ADDR='master node'  WORLD_SIZE=4 NODE_RANK=3 nohup python3 src/train.py experiment=cifar trainer=fsdp trainer.devices=1 trainer.num_nodes=4 &


```

