import os

input_file = "grades.txt"
output_file = "results.txt"

try:
    
    with open(input_file, "r", encoding="utf-8") as f_in:
        results = []
        for line in f_in:
            line = line.strip()
            if not line:
                continue  
            
            parts = line.split(",")
            name = parts[0]
            
            
            grades = [float(grade) for grade in parts[1:]]
            
            if grades:
                average = sum(grades) / len(grades)
                results.append(f"{name},{average:.2f}")

    
    with open(output_file, "w", encoding="utf-8") as f_out:
        for res in results:
            f_out.write(res + "\n")
            
    print(f"Calculs terminés avec succès ! Résultats enregistrés dans '{output_file}'.")

except FileNotFoundError:
    print(f"Erreur : Le fichier d'entrée '{input_file}' est introuvable. Veuillez vérifier son emplacement.")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")