rodjene = int(input("Koje godine ste rođeni: "))

godine = 2024 - rodjene

if godine >= 18:
    print("Vi ste punoljetni")
    if godine == 18:
        print("Vi imate 18 godina")
else:
    print("Vi niste punoljetni")

print('test')