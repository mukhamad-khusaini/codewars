def seven_ate9(str_):
    return [f"{i}{y}" if x=="9" else f"{i}{x}{y}" for i,x,y in zip(str_,str_[1:],str_[2:])]

print(seven_ate9("1245797"))