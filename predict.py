#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os, torch
from torchvision import models, transforms
from PIL import Image

class Hardware_detection:
    def __init__(self):
        self.classes = {0: "Hardware",
                        1: "No hardware"
                       }
        self.num_classes = len(self.classes)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = models.squeezenet1_0()
        model.classifier[1] = torch.nn.Conv2d(512, self.num_classes, kernel_size=(1,1), stride=(1,1))
        best_model_wts = torch.load("hardware_pretrained_1.2.1.pt", map_location=self.device)
        model.load_state_dict(best_model_wts)
        model.to(self.device)
        model.eval()
        self.model = model
        self.transform = transforms.Compose([transforms.Resize((224,224)),
                                             transforms.ToTensor(),
                                            ])
        
    
    def predict(self, image_url):
        image = Image.open(image_url).convert('RGB')
        x = self.transform(image)
        x = x.unsqueeze(0)
        x = x.to(self.device)
        y = self.model(x)
        _, preds = torch.max(y, 1)
        return self.classes[int(preds)]
    


# In[6]:


def demo_run():
    HW = Hardware_detection()
    for file_name in os.listdir("images"):
        predict = HW.predict(os.path.join("images",file_name))
        print(f"File: {file_name}\tPrediction: {predict}")

if __name__ == "__main__":
    demo_run()


# In[ ]:




