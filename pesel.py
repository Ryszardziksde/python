pesel = input("podaj pesel ")
if (int(pesel[9]) % 2 == 0):
    print("jestes baba")
elif (int(pesel[9]) % 2 == 1):
    print("jestes chlop")
else:
    print("podałeś złą wartość")

