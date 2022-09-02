import torch.nn as nn

from transformers import BertForTokenClassification, BertConfig

id_label = {0: 'B-art', 1: 'B-eve', 2: 'B-geo', 3: 'B-gpe', 4: 'B-nat', 5: 'B-org', 6: 'B-per', 7: 'B-tim', 8: 'I-art', 9: 'I-eve', 10: 'I-geo', 11: 'I-gpe', 12: 'I-nat', 13: 'I-org', 14: 'I-per', 15: 'I-tim', 16: 'O'}


class BERTModel(nn.Module):

  def __init__(self):
    
    super(BERTModel, self).__init__()
    self.bert = BertForTokenClassification.from_pretrained('bert-base-cased', num_labels=len(id_label))

  def forward(self, inputs, mask, labels):
    return self.bert(input_ids = inputs, attention_mask = mask, labels = labels, return_dict = False)