import emoji

def is_emoji(char):
    return emoji.is_emoji(char)

# Lista de hashtags
hashtags = []

# Lista de palabras
palabras = []

# Lista de enlaces
links = []

# Lista de monosílabos
monosilabos = []
# Lista de nombres de archivo
archivos = ["./datos/hashtags.txt", "./datos/links.txt", "./datos/monosilabos.txt", "./datos/palabras.txt"]

# Itera sobre la lista de nombres de archivo
for archivo in archivos:
    # Abre el archivo en modo de escritura
    file = open(archivo, "w")

    # Trunca el archivo al tamaño 0
    file.truncate()

    # Cierra el archivo
    file.close()

# Abre el archivo de tweets en modo lectura
with open("./datos/tweets.txt", "r") as lista:

    # Lee todas las líneas del archivo y las almacena en una lista
    lines = lista.readlines()
    lines = [lineas[2:] for lineas in lines]
    # Itera sobre la lista de líneas
    for line in lines:
        
        # Separa las palabras de la línea
        words = line.split()

        # Añade las palabras a la lista de palabras
        palabras.extend(words)

        """for word in words:
            if is_emoji(words[word])==True:
                words[word]="""""
        
        #print(words)
        # Itera sobre las palabras de la línea
        for word in words:
            # Si la palabra comienza con '#', se añade a la lista de hashtags
            if word[0] == "#":
                hashtags.append(word)

            # Si la palabra es un enlace, se añade a la lista de enlaces
            elif len(word) == 2:
                monosilabos.append(word)
            
            elif word[:4] =="http":
                links.append(word)
            else:
                palabras.append(word)

hashtags.sort(key=len)

"""letras=[char for char in ''.join(palabras)]
print(letras)

for letras in letras:
    if is_emoji(letras)==True:
        letra=""
print("--------------------------------------------------")
print(letras)"""



with open("./datos/hashtags.txt", "w") as hashtag:
    for x in hashtags:
        hashtag.write(x+'\n')

with open("./datos/links.txt", "w") as link:
    for y in links:
        link.write(y +'\n')

with open("./datos/palabras.txt", "w") as palabra:
    for z in palabras:
        palabra.write(z +'\n')
with open("./datos/monosilabos.txt", "w") as monosilabo:
    for w in monosilabos:
        monosilabo.write(w+'\n')



