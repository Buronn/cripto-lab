# birthday paradox
p = 0.99
n = 365
x = 1
for i in range(n):
    x = x * ((n-i+1)/n)
    if(1-x >= p):
        print("Probabilidad de que no se repita un mensaje:",round(x*100,2),"%")
        print("Probabilidad de que se repita un mensaje:",round((1-x)*100,2),"%")
        print(i)
        break