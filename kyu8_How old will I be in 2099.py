def calculate_age(year_of_birth, current_year):
    date=current_year-year_of_birth
    if date==0: return "You were born this very year!"
    elif date < 0:
        if date==-1: return "You will be born in 1 year."
        return f"You will be born in {str(date)[1:]} years."
    elif date > 0:
        if date==1: return "You are 1 year old."
        return f"You are {str(date)} years old."

print(calculate_age(2000,3001))