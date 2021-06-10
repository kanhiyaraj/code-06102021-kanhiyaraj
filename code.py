import pandas as pd
import numpy as np

def bmiCalculator(data=None):

    sampleData = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
    85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
    "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
    "HeightCm": 167, "WeightKg": 82}]

    if not data:
        data = sampleData

    tableJson = [
        {"minBMI": 0, "maxBMI": 18.4, "BMI Category": "Underweight", "Health risk": "Malnutrition risk"}, 
        {"minBMI": 18.5, "maxBMI": 24.9, "BMI Category": "Normal weight", "Health risk": "Low risk"}, 
        {"minBMI": 25, "maxBMI": 29.9, "BMI Category": "Overweight", "Health risk": "Enhanced risk"},
        {"minBMI": 30, "maxBMI": 34.9, "BMI Category": "Moderately obese", "Health risk": "Medium risk"},
        {"minBMI": 35, "maxBMI": 39.9, "BMI Category": "Severely obese", "Health risk": "High risk"},
        {"minBMI": 40, "maxBMI": np.inf, "BMI Category": "Very severely obese", "Health risk": "Very High risk"}]

    table = pd.DataFrame(tableJson)
    initialData = pd.DataFrame(data)

    initialData["BMI(kg/m)"] = initialData["WeightKg"]/ (initialData["HeightCm"]/100)**2

    initialData["BMI Category"]=""
    initialData["Health risk"]=""

    for row in table.itertuples():

        initialData.loc[((initialData["BMI(kg/m)"]> row[1]) & (initialData["BMI(kg/m)"]< row[2])), 'BMI Category'] = row[3]
        initialData.loc[((initialData["BMI(kg/m)"]> row[1]) & (initialData["BMI(kg/m)"]< row[2])), 'Health risk'] = row[4]

    overweightPeople = initialData[(initialData["BMI(kg/m)"] >= 25) & (initialData["BMI(kg/m)"] < 30)].shape[0]

    print("data with BMI Category and Health risk:\n\n", initialData)
    print("\ntotal number of overweight people: ",overweightPeople)


bmiCalculator()