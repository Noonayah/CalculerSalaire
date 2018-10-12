#Fonction de Calcul de Salaire selon le métier:

def calculSalaire(metier,exp):
     if metier == 'architecte' and exp == 4:
         salaire = '4000 euros'
         return salaire

     if metier == 'médecin' and exp == 8:
          salaire = '7000 euros'
          return salaire

     if metier == 'consultant' and exp == 5:
          salaire = '5000 euros'
          return salaire


print("Le salaire d'un architecte ayant une expérience de 4 ans a un salaire de "+calculSalaire('architecte',4))
print("Le salaire d'un médecin ayant une expérience de 8 ans a un salaire de " +calculSalaire('médecin',8))
print("Le salaire d'un consultant ayant une expérience de 5 ans a un salaire de " +calculSalaire('consultant',5))

