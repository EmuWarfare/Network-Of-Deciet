import json
import pandas as pd
import numpy as np
import os
import torch
from torch import nn
from trainModel import BertClassifier, ModelHelper
from transformers import BertTokenizer, BertModel
from torch.optim import Adam
from tqdm import tqdm


class UseModel(ModelHelper):
    def __init__(self, model_path, tokinizer_path):
        self.model = torch.load(model_path)
        # self.model.load_state_dict(torch.load(model_path))
        #self.model.eval()
        self.tokenizer = BertTokenizer.from_pretrained(tokinizer_path)
    


    def testScentence(self, scentence):
        self._set_device()
        tokinized_text = self._tokinize_text(self.tokenizer, scentence)
        
        self.model.to(self.device)

        with torch.no_grad():
            tokinized_text, mask, input_id, token_id = self._prep_input(tokinized_text)
            output = self.model(input_id, mask, token_id)

            print(output)
            print(f'{"Stereotype" if output.argmax(dim=1).item() == 0 else "Not stereotype"}')

cwd = os.getcwd()
# um = UseModel(f'{cwd}/stereotype_detection_model.pt', f'{cwd}/bert-base-uncased')
um = UseModel(f'{cwd}/pickledModel.pickle', f'{cwd}/bert-base-uncased')

#um.testScentence("Many people live in Ethiopia.The people are very thin and good at distance running.")
um.testScentence("Hispanic people love beans and are all from mexico.")
um.testScentence("Bitches ain't shit.")
um.testScentence("Women are bad drivers, and can't do math.")
um.testScentence("Women are bad drivers.")
print()

um.testScentence("Women are great at taking care of children.")
um.testScentence("Elderly people are always so nice.")

print()

um.testScentence("I LOVE PIE SO MUCH.")
um.testScentence("What a guy gotta do to get some pie.")
um.testScentence("CAN A MOTHERFUCKER GET SOME PIE GOD DAM.")

um.testScentence("Did you know, all hispanic people lick beans for subtance.")
um.testScentence("I love beans so much! Lets go beans.")
um.testScentence("Me and my hispanic brothers love black beans. Red beans though are trash.")


##############################################
## Reason why it was not working previously ##
##############################################
#I had mask and input_id mixed up :/ :/ :/ :( :[