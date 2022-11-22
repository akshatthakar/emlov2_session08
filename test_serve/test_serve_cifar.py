
from pathlib import Path
import requests, json
import unittest
import pytest
import torch


def test_cifar_inference(host):
        print(host)
        image_paths = ["10044_cat.png","cat.png", "ship.png", "automobile.png", "dog.png","airplane.png","deer.png","frog.png","horse.png", "10054_automobile.png"]
        for image_path in image_paths:
            complete_path = "images/" + image_path
            response: Response = requests.post(f"http://{host}:8080/predictions/cifar/1.0", files={'data': open(complete_path, 'rb')})
            response_json = response.json()
            print("response: " +json.dumps( response.json()))
            predicted_label = list(response_json.keys())[0]
            print(f"predicted label: {predicted_label}")
            if "_" in image_path:
                expected = image_path.split("_")[1].split(".")[0]
            else:
                expected = image_path.split(".")[0]
            assert expected == predicted_label
            print(f"done testing: {image_path}")
            print("_____________________________________________________")
            
