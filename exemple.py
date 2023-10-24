prenom = input("Bonjour, comment vous vous appelez ?  ")
nom = input("et ton nom de famille ?  ")
dictionnaire = {
    "voiture":12000,
    "maison":230000,
    "moto":1000
}
print("bonjour " + prenom + " " + nom.upper() )
produit = input("par quel produit est-tu interessé ?  voiture  moto   maison ")
print( " " )
print( produit + " Le produit coûte : ")
print(dictionnaire[produit])
print (" euros")

