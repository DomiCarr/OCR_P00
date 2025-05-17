# SManipulation de fichiers csv
#

import csv
with open('input.csv') as input_csv:
    reader = csv.DictReader(input_csv, delimiter=',')
    datas_to_transform = []
    for line in reader:
        datas_to_transform.append(line)

print ("datas_to_transform: ",datas_to_transform)

datas_to_load = []
for data in datas_to_transform:
    transformed_data = {}
    transformed_data["nom"] = data ["nom"]    
    transformed_data["salaire"]=data["heures_travaillees"]*15
    print ("transformed_data: ",transformed_data)
    datas_to_load.append(transformed_data)

print ("datas_to_load: ",datas_to_load)

with open("output.csv", mode="w") as file:
    fieldnames = ["nom", "salaire"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for data in datas_to_load:
        writer.writerow(data)





