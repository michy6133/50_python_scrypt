import random
import string

#total = string.ascii_letters + string.digits + string.punctuation
#length = int (input("Veuillez rentrez le nombre de caractères pour votre mot de passe: "))
#password = "".join(random.sample(total, length))
#print(password)

def generer_mot_de_passe():
    longueur = int (input("Entrez la longueur desirer pour votre mot de passe: "))
    inclure_min = input("Voulez vous des caractères miniscules dans votre mot de passe? (oui ou non) :").strip().lower() == "oui"
    inclure_maj = input("Voulez vous des caractères majuscules dans votre mot de passe? (oui ou non) :").strip().lower() == "oui"
    inclure_chiffre = input("Voulez vous inclure des chiffres dans votre mot de passe? (oui ou non) :").strip().lower() == "oui"
    inclure_speciaux = input("Voulez vous inclure les caracteres spéciaux dans votre mot de passe? (oui ou non) :").strip().lower() == "oui"


    caractere = ""
    if inclure_min:
        caractere += string.ascii_lowercase
    if inclure_maj:
        caractere += string.ascii_uppercase
    if inclure_chiffre:
        caractere += string.digits
    if inclure_speciaux:
        caractere += string.punctuation

    if not caractere:
        print("Aucun caractère sélectionné. Impossible de generer un mot de passe!")
        return 
    
    mot_de_passe = "".join(random.sample(caractere, longueur))
    #mot_de_passe = "".join(random.choice(caractere) for _ in range(longueur))
    print(f"Votre mot de passe sécurisé est: {mot_de_passe}")
    

if __name__ == "__main__":
    generer_mot_de_passe()
