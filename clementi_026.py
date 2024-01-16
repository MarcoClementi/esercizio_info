

from math import sqrt

def my_input():
    a = int(input("Inserisci il numero:"))
    b = int(input("Inserisci il numero:"))
    c = int(input("Inserisci il numero:"))
    return a,b,c

def elaboration(a,b,c):
    solution1=0
    solution2=0
    delta=b*b-4*a*c
    if delta < 0:
        print("<delta is negative,the equation is impossible!")
    if delta == 0:
        solution1= b/2*a

    if delta > 0:
        solution1 = b + sqrt(delta)/2*a
        solution2 = b + sqrt(delta)/2*a

    return solution1,solution2

def exit(solution1,solution2):
    print(solution1)
    print(solution2)

a,b,c = my_input()
solution1,solution2 = elaboration(a,b,c)
exit(solution1,solution2)


    
