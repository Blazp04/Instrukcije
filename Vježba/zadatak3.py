brojac = 0

# 56 
# 56/10 = 5
# 56 % 10 =6


while(True):
    broj = int(input("Unesi broj: "))
    brojac +=1
    if(broj>=10 and broj<=99):
        zbrojhZnamenki = broj/10 + broj%10
        if(zbrojhZnamenki % 3== 0):
            print("Broj je djeljiv sa 3")
            break
        print(broj)
        break
    else:
        if(brojac==10):
            break
        print("Pogrešan unos.")

