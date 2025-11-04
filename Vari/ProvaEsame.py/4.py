def lis(lista: list[int], a: int) -> int | None:
    for i in lista:
        if i == a:
            return a

print(lis([1,2,3,5,5,2,3,7,8],8))