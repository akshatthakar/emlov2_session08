
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

        cls.image_paths = ["cat.png", "ship.png", "automobile.png", "dog.png","airplane.png","bird.png","deer.png","frog.png","horse.png","truck.png”]


    @pytest.mark.parametrize("host_name", "")
    def test_mnist_datamodule():
  
        for image_path in self.image_paths:
                           
            complete_path = "images/" + image_path

            response: Response = requests.post(f"http://{self.host_name}:8080/predictions/cifar/1.0", files={'data': open(complete_path, 'rb')})

            response_json = res.json()
    
            data = response.json()['data'][0]

            predicted_label = data['label']

            print(f"predicted label: {predicted_label}")

            self.assertEqual(image_path.split(".")[0], predicted_label)

            print(f"done testing: {image_path}")
            
if __name__ == '__main__':
    unittest.main()
