from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    return entered_code==correct_code and datetime.strptime(current_date, "%B %d, %Y")<=datetime.strptime(expiration_date, "%B %d, %Y")



print(check_coupon('123','123','September 5, 2014','September 25, 2014'))