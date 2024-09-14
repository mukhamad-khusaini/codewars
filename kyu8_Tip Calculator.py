import math
def calculate_tip(amount, rating):
    val = math.ceil(amount*0 if rating.lower()=="terrible" else amount*0.05 if rating.lower()=="poor" else amount*0.1 if rating.lower()=="good" else amount*0.15 if rating.lower()=="great" else amount*0.2 if rating.lower()=="excellent" else -1)
    return val if val!=-1 else "Rating not recognised"