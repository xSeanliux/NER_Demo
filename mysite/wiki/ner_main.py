from transformers import BertTokenizerFast
from .ner_utils import evaluate_sentence
from .ner_model import BERTModel
import torch

"""
the .pt file best.pt can be found and downloaded at https://drive.google.com/drive/folders/1Zk0KksUbsHmecJEbVhtGlzHxcLtcIyjd?usp=sharing. 
Please email zxliu2@illinois.edu if you encounter any problems.
"""


device = "cpu" #mps probably broken ;(

tokenizer = BertTokenizerFast.from_pretrained('bert-base-cased')
model = BERTModel().cpu()

try: 
    ckpt = torch.load(f"./wiki/best.pt", map_location=torch.device('cpu'))
    model.load_state_dict(ckpt['model_state_dict'])
    print("Finished Loading model! Please enter a sentence.")
except:
    print("best.pt not found. Please find it and try again to run on a pretrained model. The .pt file can be found at https://drive.google.com/drive/folders/1Zk0KksUbsHmecJEbVhtGlzHxcLtcIyjd?usp=sharing.")

model.eval()


sentence = input()

result = evaluate_sentence(sentence)

print(result)


