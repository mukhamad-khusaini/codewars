def rental_car_cost(d):
    return 40*d if (d<3) else (40*d)-20 if(3<=d<7) else (40*d)-50

print(rental_car_cost(4))