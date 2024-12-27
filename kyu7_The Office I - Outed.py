def outed(meet, boss):
 if sum([meet[i] if i!=boss else meet[i]*2 for i in meet])/len(meet) <= 5: return 'Get Out Now!' 
 else: return 'Nice Work Champ!'

print(outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura'))