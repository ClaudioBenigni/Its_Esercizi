def vero(x,y,z):
    if x and (y or z) ==True:

        return "Azione permessa"
    
    else:
        return "Azione negata"

a = True
b=False
c=False

print(vero(a,b,c))