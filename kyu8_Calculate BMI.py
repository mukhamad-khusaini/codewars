def bmi(weight, height):
    bmi=weight/height**2
    return "Obese" if bmi>30 else "Overweight" if bmi>25 else "Normal" if bmi>18.5 else "Underweight"