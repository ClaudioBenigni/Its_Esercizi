def max(lista:list[int]) -> tuple:
    
    a=lista[0] 
    b=lista[0] 

    for i in lista:
        if i >a:
            a=i
        elif i<b:
            b=i
    
    div =(a,b)

    print(div)
max([1,2,3,4,5,6,7,8]) 