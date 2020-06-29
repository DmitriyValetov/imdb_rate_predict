import os
import json
import pathlib

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

def classify(review):
    vectorizer = joblib.load(os.path.join(pathlib.Path(__file__).parent.absolute(), 'vectorizer.jbl'))
    model = joblib.load(os.path.join(pathlib.Path(__file__).parent.absolute(), 'model.jbl'))
    return model.predict(vectorizer.transform([review]))[0]
    

class Index(View):
    template_name = 'index.html'

    def get(self, request):
          return render(request, self.template_name)

class Model(View):
    
    def get(self, request):       
        return HttpResponse("Dead end")

    def post(self, request):
        rating = classify(request.POST['review'])
        print(rating)
        return HttpResponse(json.dumps({'rating': int(rating)}), content_type="application/json")
