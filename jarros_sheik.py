maior = True
for i in range(1, 4):
    if i == 1:
        while maior:
            c1 = float(input(f"\nQuantidade máxima do jarro {i}: "))
            if c1 <= 40:
                maior = False
            else:
                print("\nCapacidade máxima em cada jarro é de 40L")
        maior = True
        while maior:
            a1 = float(input(f"\nQuantidade de água no jarro {i}: "))
            if a1 <= c1:
                maior = False
            else:
                print(f"\nA quantidade de água no jarro {i} não pode ser maior que {c1}")
        maior = True
        t1 = float(input(f"\nQual a quantidade desejada no jarro {i}: "))
    if i == 2:
        while maior:
            c2 = float(input(f"\nQuantidade máxima do jarro {i}: "))
            if c2 <= 40:
                maior = False
            else:
                print("\nCapacidade máxima em cada jarro é de 40L")
        maior = True
        while maior:
            a2 = float(input(f"\nQuantidade de água no jarro {i}: "))
            if a2 <= c2:
                maior = False
            else:
                print(f"\nA quantidade de água no jarro {i} não pode ser maior que {c2}")
        maior = True
        t2 = float(input(f"\nQual a quantidade desejada no jarro {i}: "))
    if i == 3:
        while maior:
            c3 = float(input(f"\nQuantidade máxima do jarro {i}: "))
            if c3 <= 40:
                maior = False
            else:
                print("\nCapacidade máxima em cada jarro é de 40L")
        maior = True
        while maior:
            a3 = float(input(f"\nQuantidade de água no jarro {i}: "))
            if a3 <= c3:
                maior = False
            else:
                print(f"\nA quantidade de água no jarro {i} não pode ser maior que {c3}")
        t3 = float(input(f"\nQual a quantidade desejada no jarro {i}: "))
jarro1 = [c1, a1, t1]
jarro2 = [c2, a2, t2]
jarro3 = [c3, a3, t3]
for i in range(1, 4):
    if i == 1:
        print(f"\nCapacidade máxima no jarro 1: {jarro1[0]}L")
        print(f"Quantidade no jarro 1: {jarro1[1]}L")
        print(f"Quantidade desejada no jarro 1: {jarro1[2]}L")
    if i == 2:
        print(f"\nCapacidade máxima no jarro 2: {jarro2[0]}L")
        print(f"Quantidade no jarro 2: {jarro2[1]}L")
        print(f"Quantidade desejada no jarro 2: {jarro2[2]}L")
    if i == 3:
        print(f"\nCapacidade máxima no jarro 3: {jarro3[0]}L")
        print(f"Quantidade no jarro 3: {jarro3[1]}L")
        print(f"Quantidade desejada no jarro 3: {jarro3[2]}L")

