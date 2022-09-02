import numpy as np
from transformers import BertTokenizerFast
from .ner_model import BERTModel
import torch 

label_id = {'B-art': 0, 'B-eve': 1, 'B-geo': 2, 'B-gpe': 3, 'B-nat': 4, 'B-org': 5, 'B-per': 6, 'B-tim': 7, 'I-art': 8, 'I-eve': 9, 'I-geo': 10, 'I-gpe': 11, 'I-nat': 12, 'I-org': 13, 'I-per': 14, 'I-tim': 15, 'O': 16}
id_label = {0: 'B-art', 1: 'B-eve', 2: 'B-geo', 3: 'B-gpe', 4: 'B-nat', 5: 'B-org', 6: 'B-per', 7: 'B-tim', 8: 'I-art', 9: 'I-eve', 10: 'I-geo', 11: 'I-gpe', 12: 'I-nat', 13: 'I-org', 14: 'I-per', 15: 'I-tim', 16: 'O'}

def get_labels_and_idx(sentence, labels, tokenizer):

  """
  slower but much better labeller from https://github.com/chambliss/Multilingual_NER/blob/master/python/utils/main_utils.py#L118
  """
  words = sentence.split()
  labels = labels.split()
  ret = [-1] #CLS will be 0
  idxes = [-1] #CLS idx -1
  prev_word = None

  for i, word in enumerate(words):
    tokenized_word = tokenizer(word, return_tensors = "pt")
    assert len(tokenized_word.input_ids[0]) > 2
    token_cnt = len(tokenized_word.input_ids[0]) - 2 # [CLS] and [SEP] are not counted
    try:
      ret = ret + [label_id[labels[i]]] * token_cnt
    except: 
      ret = ret + [-1] * token_cnt
    idxes = idxes + [i] * token_cnt

  if len(ret) < 512:
    ret = ret + [-1] * (512 - len(ret))
    idxes = idxes + [-1] * (512 - len(idxes))
  else:
    ret = ret[0:512]
    idxes = idxes[0:512]

  return ret, idxes

model = None
tokenizer = None
hasInit = False

def __init__():
  global model, tokenizer 
  global tokenizer 
  model = BERTModel().cpu()
  tokenizer = BertTokenizerFast.from_pretrained('bert-base-cased')
  # do something
  try:
    ckpt = torch.load(f"./wiki/best.pt", map_location=torch.device('cpu'))
    model.load_state_dict(ckpt['model_state_dict'])
    model.eval()
    hasInit = True
    print("Model loaded.")
  except:
    print("best.pt not found. Please find it and try again to run on a pretrained model. The .pt file can be found at https://drive.google.com/drive/folders/1Zk0KksUbsHmecJEbVhtGlzHxcLtcIyjd?usp=sharing.")
  
  
  

def evaluate_sentence(sentence, device = "cpu"):

  if not hasInit: 
    __init__()

  tokenized = tokenizer(sentence, padding='max_length', max_length = 512, truncation=True, return_tensors="pt")
  input_ids = tokenized["input_ids"].to(device)
  masks = tokenized["attention_mask"].to(device)
  label, idxes = get_labels_and_idx(sentence, "O " * 512, tokenizer)

  logits = model(input_ids, masks, None)

  results = ["O"] * len(sentence.split())

  logits_clean = logits[0][label != -1].squeeze()
  preds = logits_clean.argmax(dim = 1).tolist()

  for i, pred in enumerate(preds):
    if pred == -1 or idxes[i] == -1:
      continue
    else:
      if results[ idxes[i] ] == "O":
        results[ idxes[i] ] = id_label[pred]

  print(sentence, results)

  tags = []
  words = sentence.split()
  for i, word in enumerate(words):
    if results[i] != "O":
      tags.append(f'<span class = "labeled {results[i][-3:]}">{word}</span>')
    else:
      tags.append(f'{word}')
  ret = " ".join(tags)
  print("ret = ", ret)
  return ret