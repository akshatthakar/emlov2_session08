import torch
import sys
import requests
import numpy as np
import torchvision.transforms as T
from PIL import Image
from captum.attr import visualization as viz

host = sys.argv[1]
img_path = sys.argv[2]
res = requests.post(f"http://{host}:8080/explanations/cifar/1.0", files={'data': open(img_path, 'rb')})
ig = res.json()

img_prefix = img_path.split(".")[0] + "_"
inp_image = Image.open(img_path)
to_tensor = T.Compose([
	T.Resize(224),
	T.ToTensor()
])
inp_image = to_tensor(inp_image)
inp_image = inp_image.numpy()
attributions = np.array(ig)
inp_image, attributions = inp_image.transpose(1, 2, 0), attributions.transpose(1, 2, 0)

(plt,axis) = viz.visualize_image_attr(attributions, inp_image, method="blended_heat_map",sign="all", show_colorbar=True, title="Overlayed Integrated Gradients")
print(img_prefix)
plt.savefig(img_prefix+'integrated_gradient.png')
