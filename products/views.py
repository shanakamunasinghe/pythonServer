from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import openpyxl as xl
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib  # save the model
from pathlib import Path
from sklearn import tree  # make grphical representation


# /Products
def index(request):
    return HttpResponse('hello world')


def show_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('hello world new')


# used to create model
def dump_model(request):
    music_data = pd.read_csv(r'D:\testProjectDjango\products\music.csv')
    x = music_data.drop(columns=['genre'])
    y = music_data['genre']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    # model.fit(x,y)
    # graph and the features
    tree.export_graphviz(model, out_file='music-recomender.dot',
                         feature_names=['age', 'gender']
                         , class_names=sorted(y.unique()),
                         label='all',
                         rounded=True,
                         filled=True)
    # make job
    joblib.dump(model, 'music-recommender.joblib')
    return HttpResponse('model creation completed')


# used to get model predictions
def run_model(request):
    model = joblib.load('music-recommender.joblib')
    predictions = model.predict([[21, 1]])
    return HttpResponse('model value created')


# def show_files(request):
#     path = Path()
#     file = []
#     for file in path.glob('*.csv'):
#         print(file)
#     return HttpResponse(file)
