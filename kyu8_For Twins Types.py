def type_validation(variable, _type): 
    return type(variable).__name__==_type


print(type("45").__name__)