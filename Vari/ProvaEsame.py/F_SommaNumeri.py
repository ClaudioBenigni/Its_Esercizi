#Filtra e Somma Numeri – PUNTI 1
#Scrivi una funzione:
#filter_and_sum(nums: list[int], min_val: int) -> int
#Restituisce la somma di tutti i numeri maggiori di min_val.

def filter_and_sum(nums: list[int], min_val: int) -> int:
    somma=[] 
    for n in nums:
        if n>min_val:
            somma.append(n)
    
    return sum(somma)