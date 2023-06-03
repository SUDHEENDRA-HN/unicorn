def prediction_model(pclass,age,sex,sibsp,parch,fare,embarked):
 import pickle
 x=[[pclass,age,sex,sibsp,parch,fare,embarked]]
 random_forest=pickle.load(open('titanic_model.sav','rb'))
 predictions=random_forest.predict(x)
 if predictions ==  1:
     predictions = "survived"
 elif predictions == 0:
     predictions = "not survived"
 else:
     predictions = "error"
 return predictions
