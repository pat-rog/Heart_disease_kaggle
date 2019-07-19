choice = 0
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

def average(choice):
    print("Średnia dla wybranej kolumny ")
    print(choice)

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
