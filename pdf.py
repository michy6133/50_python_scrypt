from pdf2docx import Converter

def pdf_to_word(pdf_file, word_file):
    # Crée un objet Converter
    cv = Converter(pdf_file)
    
    # Convertit le PDF en Word
    cv.convert(word_file, start=0, end=None)  # start et end sont les pages à convertir
    cv.close()

# Exemple d'utilisation
pdf_file = ""
word_file = ""
pdf_to_word(pdf_file, word_file)

print(f"Conversion terminée ! Le fichier {word_file} a été créé.")

