n = int(input("Qual número deseja veificar na sequência de Fibonacci? "))
t1 = 0
t2 = 1

while True:
    t3 = t1 + t2
    t1 = t2 
    t2 = t3
    if t1 == n:
        print("O número pertence a sequência fibonacci")
        break
    elif t2 == n:
        print("O número pertence a sequência fibonacci")
        break
    elif t3 > n and t1 != n and t2 != n:
        print("O número não pertence a sequência fibonacci")
        break


