import pandas as pd

def menu():
    print("1. #age [Age in years]: ")
    print("2. #sex [1 = male; 0 = female]: ")
    print("3. #cp [chest pain type]: ")
    print("4. #trestbps [resting blood pressure in mm Hg on admission to the hospital]: ")
    print("5. #chol [serum cholestoral in mg/dl]: ")
    print("6. #fbs [fasting blood sugar > 120 mg/dl 1 = true & 0 = false]: ")
    print("7. #restecg [resting electrocardiographic results]: ")
    print("8. #thalach [maximum heart rate achieved]: ")
    print("9. #exang [exercise induced angina 1 = yes & 0 = noe]: ")
    print("10. #oldpeak [ST depression induced by exercise relative to rest]: ")
    print("11. #slope [the slope of the peak exercise ST segment]: ")
    print("12. #ca [number of major vessels 0-3 colored by fluorosopy]: ")
    print("13. #thal [3= normal; 6 = fixed defect; 7 = reversable defect]: ")
    print("14. #target [1 or 0]: ")

def import_data(choice,name_of_column):
    data_csv = pd.read_csv('heart.csv')
    if (choice==1):
        name_of_column = 'age'
    elif (choice==2):
        name_of_column = 'sex'
    elif (choice==3):
        name_of_column = 'cp'
    elif (choice==4):
        name_of_column = 'trestbps'
    elif (choice==5):
        name_of_column = 'chol'
    elif (choice==6):
        name_of_column = 'fbs'
    elif (choice==7):
        name_of_column = 'restecg'
    elif (choice==8):
        name_of_column = 'thalach'
    elif (choice==9):
        name_of_column = 'exang'
    elif (choice==10):
        name_of_column = 'oldpeak'
    elif (choice==11):
        name_of_column = 'slope'
    elif (choice==12):
        name_of_column = 'ca'
    elif (choice==13):
        name_of_column = 'thal'
    elif (choice==14):
        name_of_column = 'target'
    else:
        print('error')
    data = data_csv[name_of_column]
    return data

def average(data, choice, name_of_column):
    x = import_data(choice, name_of_column)
    print("Średnia dla wybranej kolumny")
    i = 0
    sum = 0
    for age in x:
        number = int(x[i])
        sum = sum + number
        i = i + 1
    average_result = round(sum/i, 3)
    print(average_result)
    return average_result

def median(choice):
    print("Mediana dla wybranej kolumny ")
    print(choice)


def standard_deviation(choice):
    print("Odchylenie standardowe dla wybranej kolumny ")
    print(choice)


def standard_error(choice):
    print("Błąd standardowy dla wybranej kolmny ")
    print(choice)


def variance(choice):
    print("Wariancja dla wybranej kolumny ")
    print(choice)


def kurtosis(choice):
    print("Kurtoza za wybranej kolumny ")
    print(choice)
