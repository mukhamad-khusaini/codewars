def get_drink_by_profession(param):
    obj={
        "jabroni":"Patron Tequila",
        "school counselor":	"Anything with Alcohol",
        "programmer":"Hipster Craft Beer",
        "bike gang member":"Moonshine",
        "politician":"Your tax dollars",
        "rapper":"Cristal"
    }
    
    if param.lower() in obj:
        return obj[param.lower()]
    else: 
        return "Beer"

print(get_drink_by_profession("BiKe GanG MeMBER"))