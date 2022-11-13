from pathlib import Path
import requests

import pytest
import torch

from src.datamodules.mnist_datamodule import MNISTDataModule


@pytest.mark.parametrize("host_name", "")
def test_mnist_datamodule(host_name):

    res = requests.post(f"http://{host_name}:8080/predictions/cifar/1.0", files={'data': open('0.png', 'rb')})

    response = res.json()

    assert not dm.data_train and not dm.data_val and not dm.data_test
    assert Path(data_dir, "MNIST").exists()
    assert Path(data_dir, "MNIST", "raw").exists()

    dm.setup()
    assert dm.data_train and dm.data_val and dm.data_test
    assert dm.train_dataloader() and dm.val_dataloader() and dm.test_dataloader()

    num_datapoints = len(dm.data_train) + len(dm.data_val) + len(dm.data_test)
    assert num_datapoints == 70_000

    batch = next(iter(dm.train_dataloader()))
    x, y = batch
    assert len(x) == batch_size
    assert len(y) == batch_size
    assert x.dtype == torch.float32
    assert y.dtype == torch.