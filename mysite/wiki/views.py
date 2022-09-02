from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####

import sys
sys.path.insert(0, './ner')
from .ner_utils import evaluate_sentence, id_label


def index(request):
    return HttpResponse("Hello, world. You're at the NER index.")

def get_labels(request): 
    topic = request.GET.get('topic', None)

    print('topic:', topic)
    evaluated = evaluate_sentence(topic)

    data = {
        'summary': evaluated,
        'raw': 'Successful',
    }

    print('json-data to be sent: ', data)

    return JsonResponse(data)