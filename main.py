Poblano = 1500
Mirasol = 6000
Serrano = 15500
Cayenne = 40000
Thai = 75000
Habanero = 125000

nombre_de_piments = int(input(""))
noms_des_piment = input("")
piquant_de_chili= 0

if noms_des_piment == "Poblano":
    piquant_de_chili += 1500

elif noms_des_piment == "Mirasol":
     piquant_de_chili += 6000

elif noms_des_piment == "Serrano":
     piquant_de_chili += 15500

elif noms_des_piment == "Cayenne":
     piquant_de_chili += 40000

elif noms_des_piment == "Thai":
     piquant_de_chili += 75000

elif noms_des_piment == "Habanero":
     piquant_de_chili += 125000

print(""+ piquant_de_chili +"")