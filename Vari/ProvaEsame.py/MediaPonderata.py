def calculate_weighted_mean(values: list[float], weights: list[float]) -> float:

    if not values or not weights:
        raise ValueError("Input non valido")
    
    elif len(values)!=len(weights):
        raise ValueError("Input non valido")
    
    else:
        media= (sum(values)*sum(weights))/sum(weights)
        print(f"La media ponderata è di{media}")

