
from pathlib import Path
import requests, json
import unittest
import pytest
import torch

class TestServe(unittest.TestCase):

   @pytest
   def test_cifar_inference(host_name):
        image_paths = ["cat.png", "ship.png", "automobile.png", "dog.png","airplane.png","bird.png","deer.png","frog.png","horse.png","truck.png"]
        for image_path in image_paths:
            complete_path = "images/" + image_path
            response: Response = requests.post(f"http://{host_name}:8080/predictions/cifar/1.0", files={'data': open(complete_path, 'rb')})
            response_json = res.json()
            predicted_label = list(response_json.keys())[0]
            print(f"predicted label: {predicted_label}")
            self.assertEqual(image_path.split(".")[0], predicted_label)
            print(f"done testing: {image_path}")
            
if __name__ == '__main__':
    unittest.main()
