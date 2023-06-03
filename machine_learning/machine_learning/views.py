from django.shortcuts import render
from . import ml_pred
def home(request):
    return render(request,'index.html')

def res(request):
    age=int(request.GET['age'])
    pclass=int(request.GET['pclass'])
    sex=int(request.GET['sex'])
    sibsp=int(request.GET['sibsp'])
    parch=int(request.GET['parch'])
    fare=int(request.GET['fare'])
    embarked=int(request.GET['embarked'])
    predictions=ml_pred.prediction_model(pclass,age,sex,sibsp,parch,fare,embarked)
    return render(request,'result.html',{'predictions': predictions})
