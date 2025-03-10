def make_car(produttore: str, modello:str, color:str= None, tow_package:bool=None):
    if color == None and tow_package == None:
        car: dict = {"produttore": produttore, "modello":modello}
    elif color == None and tow_package != None:
        car: dict = {"produttore": produttore, "modello":modello, "tow_package": tow_package}
    elif color == None and tow_package != None:
        car: dict = {"produttore": produttore, "modello":modello, "colore": color}
    else:
        car: dict = {"produttore": produttore, "modello":modello, "colore": color, "tow_package": tow_package}
    return car
chiamata= make_car("porsche", "911gt3rs", color = "rosa")