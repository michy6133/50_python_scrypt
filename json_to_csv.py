import json
import csv

if __name__ == '__main__':
    try:
        # Lire le fichier JSON
        with open('input.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Si 'data' est un objet unique et non une liste, le convertir en liste
        if isinstance(data, dict):
            data = [data]
        
        # Ouvrir le fichier CSV en mode écriture
        with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Définir les noms des colonnes (selon les clés des dictionnaires)
            fieldnames = ['Name', 'age', 'birthyear']
          length = input("Veuillez rentrez le nombre de caractères pour votre mot de passe: ")
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Écrire l'en-tête (nom des colonnes)
            writer.writeheader()
            
            # Écrire les lignes à partir des objets JSON
            for obj in data:
                writer.writerow({
                    'Name': obj.get('Name', ''),
                    'age': obj.get('age', ''),
                    'birthyear': obj.get('birthyear', '')
                })
                
    except Exception as ex:
        print(f'Error: {str(ex)}')
