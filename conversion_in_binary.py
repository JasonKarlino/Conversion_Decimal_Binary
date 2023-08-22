# conversion d'un nombre entier en décimal en binaire

print("Hello cher utilisateur, ce programme permet de conertir un nombre entier en\nbase 10 en binaire")
number_in_decimal=int(input("Entrez un nombre entier strictement positif en base 10 : "))

#vérifivation de la positivité du nombre 
while number_in_decimal<0:
    print("Erreur,le nombre à saisir doit être strictement positif")
    number_in_decimal=int(input("Veuillez réessayer, saisissez à nouveau : "))

#création d'une liste vide qui prendra les restes des divisions successives par 2
my_list=[]

#affectation du nombre saisi à une autre variable pour effectuer les divisions et conserver le valeur de départ
number=number_in_decimal

while(number!=0):
    my_list.append(number%2)
    number=number//2

if number_in_decimal==0:
    print(f"{number_in_decimal} en base {10} équivaut à {0} en binaire")
else:
    print(f"Le nombre {number_in_decimal} en base {10} (en décimal) équivaut en binaire (en base 2) à : ",end="")
    for i in my_list[::-1]:
        print(f"{i}",end="")
print("\n")