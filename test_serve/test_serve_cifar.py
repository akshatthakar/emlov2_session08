
from pathlib import Path
import requests, json
import unittest
import pytest
import torch

class TestServe(unittest.TestCase)

   @classmethod
    def setUpClass(cls):

        cls.host_name = ""

        print(f"using host_name={cls.host_name}\n\n")

        cls.image_paths = ["cat.png", "ship.png", "automobile.png", "dog.png"]


    @pytest.mark.parametrize("host_name", "")
    def test_mnist_datamodule(host_name):
  
        for image_path in self.image_paths:

            response: Response = requests.post(f"http://{self.host_name}:8080/predictions/cifar/1.0", files={'data': open(image_path, 'rb')})

            response_json = res.json()
    
            data = response.json()['data'][0]

            predicted_label = data['label']

            print(f"predicted label: {predicted_label}")

            self.assertEqual(image_path.split(".")[0], predicted_label)

            print(f"done testing: {image_path}")
            
if __name__ == '__main__':
    unittest.main()
