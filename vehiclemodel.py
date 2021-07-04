import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
def create_model():
    df=pd.read_excel("vehiclemodel.xlsx")
    print(df)
    model_np=np.array(df["model"])
    kilometer_np=np.array(df["kilometer"])
    year_np=np.array(df["year"])
    power_np=np.array(df["power"])
    price_np=np.array(df["price"])
    print(model_np)
    print(kilometer_np)
    print(year_np)
    print(power_np)
    print(price_np)

#linear regression .....preprocessing

    model_pp=preprocessing.LabelEncoder()
    model_pp.fit(model_np)
    model_preprocess=model_pp.transform(model_np)
    print(model_preprocess)
#model creation , creating dictionary

    dict={'model':model_preprocess,'kilometer':kilometer_np,'year':year_np,'power':power_np}


    df1=pd.DataFrame(dict)
    print(df1)

#import linear regression ,linear regression model
    lr=LinearRegression()
    lr.fit(df1,price_np)
    print(lr)

    model_name=input("Enter the model name:")
    kilometer=int(input("Enter the kilometer:"))
    year=int(input("Enter the year:"))
    power=int(input("Enter the power:"))

    model_entered_preprocessed=model_pp.transform([model_name])
    print(model_entered_preprocessed)

#getting prediction

    for_prediction_np=np.array([[model_entered_preprocessed[0],kilometer,year,power]])
    prediction=lr.predict(for_prediction_np)
    print(prediction)

create_model()
