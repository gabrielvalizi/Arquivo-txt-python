search_text = ","
replace_text = ";"

with open ("original.txt", "r") as arquivo:

    texto = arquivo.read ()

    print ("Texto original\n", texto, "\n")

    

    texto = texto.replace (search_text, replace_text)

with open("aaaaaa.txt", 'w') as arquivo:
  
    arquivo.write (texto)
    print("Texto alterado\n", texto)

