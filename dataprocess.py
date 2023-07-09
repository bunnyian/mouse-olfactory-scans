

## Imports and initializations
import pyrfume
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
import matplotlib.pyplot as plt # for plotting
import torch.optim as optim
from torch.utils.data import Dataset

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

## Data Processing
# transform 256x256 images to tensors
data_transformation = transforms.Compose([transforms.Resize((256,256)), transforms.ToTensor()])

dataset = datasets.ImageFolder(root='/Users/ianwu/Documents/GitHub/mouse-olfactory-scans/OlfactoryScans', transform=data_transformation)

# remove unecessary channels (as it is grayscale, but currenty has 3 channels)
for image, label in dataset:
    image = image[0,:,:]

print(image.shape)
plt.imshow(image)


# replace all labels with 0 or 1, depending on if it is toxic or not
# 0 = non-toxic, 1 = toxic
# current labels are PubChem CID numbers, match with the Pyrfume GRAS dataset to get toxicity
manifest = pyrfume.load_manifest("gras") # load the manifest of the GRAS dataset
safe_molecules = pyrfume.load_data("gras/molecules.csv") # molecules that are safe

safe_count = 0
i = 0
for image, label in dataset:
    cid = label
    if cid in safe_molecules.iloc[i]['IUPACName']:
        label = 0
        safe_count += 1
    i += 1
        
print(safe_count, "out of", len(dataset), "molecules are safe")