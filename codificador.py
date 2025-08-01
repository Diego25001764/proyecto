clave_en_uso=" "
def setkey(valor):
    global clave_en_uso
    global clave
    clave = " ".join(valor)
    if '"' in clave:
        print(" resultado >> ERROR! Llave no valida")
        return setkey()
    else:
        clave_en_uso=clave
        return clave

#En esta subrutina del codificador, es la encargada de hacer el equivalente a las palabras con tilde minusculas a palabras sin tilde minusculas ejemplo: "á" lo convierte a "\a"
def codificador_tildes_minusculas(txt,e,segunda_letra,codificado):
    if int(ord(txt[e])) == 225:
        codificado.append(chr(92))
        nueva_letra_numero = int(0 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    elif int(ord(txt[e])) == 233:
        codificado.append(chr(92))
        nueva_letra_numero = int(4 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    elif int(ord(txt[e])) == 237:
        codificado.append(chr(92))
        nueva_letra_numero = int(8 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    elif int(ord(txt[e])) == 243:
        codificado.append(chr(92))
        nueva_letra_numero = int(14 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    elif int(ord(txt[e])) == 250:
        codificado.append(chr(92))
        nueva_letra_numero = int(20 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    return nueva_letra_letra

#En esta subrutina del codificador, es la encargada de hacer el equivalente a las palabras con tilde Mayusculas a palabras sin tilde Mayusculas ejemplo: "Á" lo convierte a "\A"
def codificador_tildes_mayusculas(txt,e,segunda_letra,codificado):
    if int(ord(txt[e])) == 193:
        codificado.append(chr(92))
        nueva_letra_numero = int(0 + segunda_letra)                
        nueva_letra_letra = nueva_letra_numero + 65
    elif int(ord(txt[e])) == 201:
        codificado.append(chr(92))
        nueva_letra_numero = int(4 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    elif int(ord(txt[e])) == 205:
        odificado.append(chr(92))
        nueva_letra_numero = int(8 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    elif int(ord(txt[e])) == 211:
        codificado.append(chr(92))
        nueva_letra_numero = int(14 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    elif int(ord(txt[e])) == 218:
        codificado.append(chr(92))
        nueva_letra_numero = int(20 + segunda_letra)
        nueva_letra_letra = nueva_letra_numero + 65
    return nueva_letra_letra

#En esta subrutina del descodificador es la encargada de encontrar si alguna de las palabras (Ya sea minuscula o Mayuscula) tenía tilde por ejemplo: "\a" lo convierte a "á" o ls "\A" lo convierte a "Á"
def descodificador_sintildes(descodificado):
    a = 0 
    sintildes = []
    for tildes in descodificado:
        if (tildes == "\\"):
            if descodificado[a+1] == "a":
                sintildes.append("á")
            elif descodificado[a+1] == "e":
                sintildes.append("é")
            elif descodificado[a+1] == "i":
                sintildes.append("í")
            elif descodificado[a+1] == "o":
                sintildes.append("ó")
            elif descodificado[a+1] == "u":
                sintildes.append("ú")
            elif descodificado[a+1] == "A":
                sintildes.append("Á")
            elif descodificado[a+1] == "E":
                sintildes.append("É")
            elif descodificado[a+1] == "I":
                sintildes.append("Í")
            elif descodificado[a+1] == "O":
                sintildes.append("Ó")
            elif descodificado[a+1] == "U":
                sintildes.append("Ú")
            else:
                sintildes.append("\\")
            descodificado.remove(descodificado[a+1])
            a += 1 
        else:
            sintildes.append(descodificado[a]) 
            a += 1
    return sintildes

#En esta subrutina del codificador es la encargada de realizar la operacion matemática para encontrar la letra equivalente en base a la oracion original y la llave ya convetida en una oracion
def codificador_codificado(key,txt,key_nueva,codificado):
    e = 0
    segunda_letra = ord(key_nueva[e].upper()) - ord("A")
    for codificar in txt:
        if codificar.isupper():
            if (int(ord(txt[e])) == 193) or (int(ord(txt[e])) == 201) or (int(ord(txt[e])) == 205) or (int(ord(txt[e])) == 211) or (int(ord(txt[e])) == 218):
                nueva_letra_letra = codificador_tildes_mayusculas(txt,e,segunda_letra,codificado)
            else:
                primer_letra = ord(txt[e]) - ord("A")
                segunda_letra = ord(key_nueva[e].upper()) - ord("A")
                nueva_letra_numero = int(primer_letra + segunda_letra)
                nueva_letra_letra = nueva_letra_numero + ord("A")

            if nueva_letra_letra <= 90:
                final = chr(nueva_letra_letra)
                letra = final
            else:
                final = chr(nueva_letra_letra + 6)
                letra = final.upper()
            codificado.append(letra)
            e += 1

        elif codificar.islower():
            primer_letra = ord(txt[e]) - ord("a")
            segunda_letra = ord(key_nueva[e].lower()) - ord("a")
            if (int(ord(txt[e])) == 225) or (int(ord(txt[e])) == 233) or (int(ord(txt[e])) == 237) or (int(ord(txt[e])) == 243) or (int(ord(txt[e])) == 250):
                nueva_letra_letra = codificador_tildes_minusculas(txt,e,segunda_letra,codificado)
            else:
                nueva_letra_numero = int(primer_letra + segunda_letra)
                nueva_letra_letra = nueva_letra_numero + 65   

            if nueva_letra_letra <= 90:
                final = chr(nueva_letra_letra)
                letra = final.lower()
            else:
                final = nueva_letra_letra + 6
                letra = chr(final)
            codificado.append(letra)
            e += 1
        elif txt[e] == chr(92):
            codificado.append(txt[e])
            codificado.append(chr(92))
            e += 1 
        else:
            codificado.append(txt[e])
            e += 1
    return codificado

#En esta subrutina del descodificador es la encargada de realizar la operacion matematica para encontrar el texto original 
def descodificador_descodificado(key,txt,key_nueva,descodificado):
    e = 0
    for descodificar in txt:
        if descodificar.isupper():
            primer_letra = ord(txt[e]) - ord("A")
            segunda_letra = ord(key_nueva[e].upper()) - ord("A")
            nueva_letra_numero = int(primer_letra - segunda_letra)
            if nueva_letra_numero >= 0:
                nueva_letra_letra = nueva_letra_numero + 65
            else:
                nueva_letra_letra = nueva_letra_numero + 26 + 65
            final = chr(nueva_letra_letra)
            letra = final
            descodificado.append(letra)
            e += 1

        elif descodificar.islower():
            primer_letra = ord(txt[e]) - ord("a")
            segunda_letra = ord(key_nueva[e].lower()) - ord("a")
            nueva_letra_numero = int(primer_letra - segunda_letra)
            if nueva_letra_numero >= 0:
                nueva_letra_letra = nueva_letra_numero + 97
            else:
                nueva_letra_letra = nueva_letra_numero + 26 + 97 
            final = chr(nueva_letra_letra)
            letra = final
            descodificado.append(letra)
            e += 1
        else:
            descodificado.append(txt[e])
            e += 1
    resultado1 = descodificador_sintildes(descodificado)
    resultado = "".join(resultado1) 
    return resultado 

def encode_text(Llave,texto):#proceso para decodificar   
    key=list(Llave)
    txt=list(texto)
    key_nueva=[]
    codificado=[]
    i = 0
    caracter = 0
    for posicion in txt:
        if (posicion != " ") and (txt[caracter].isalpha()):
            key_nueva.append(key[0+i])

            if i >= (len(key)-1):
                i -= (len(key)-1)
            else:
                i += 1
            caracter += 1
        else:
            key_nueva.append(" ")
            caracter += 1
    resultado1 = codificador_codificado(key,txt,key_nueva,codificado)
    resultado = "".join(resultado1)
    print(" resultado >>", resultado)
    return resultado

def decode_text(Llave, texto):
    key=list(Llave)
    txt=list(texto)
    key_nueva=[]
    descodificado=[]
    i = 0
    caracter = 0
    for posicion in txt:
        if (posicion != " ") and (txt[caracter].isalpha()):
            key_nueva.append(key[0+i])
            if i >= (len(key)-1):
                i -= (len(key)-1)
            else:
                i += 1
            caracter += 1
        else:
            key_nueva.append(" ")
            caracter += 1
    resultado1 = descodificador_descodificado(key,txt,key_nueva,descodificado)
    resultado = "".join(resultado1)
    print(" resultado >>", resultado)
    return resultado

def encode_file(nombre_archivo,clave=None):
    if clave is None:
        if clave_en_uso.strip() != "":
            clave = clave_en_uso 
        else:
            clave = "llaveuno"

    try:
        with open(nombre_archivo,"r",encoding="utf-8")as entrada:
            with open(nombre_archivo.replace(".txt",".gcf"),"w",encoding="utf-8")as salida:
                linea = entrada.readline()
                while linea != "":
                    mensaje = linea.strip("\n")
                    codificado = encode_text(clave,mensaje)
                    salida.write(codificado + "\n")
                    linea=entrada.readline()
        print(" resultado >> Archivo codificado exitosamente")        
    except FileNotFoundError:
        print(f" resultado >> ERROR! '{nombre_archivo}' no fue encontrado.")

def decode_file(nombre_archivo,clave=None):
    if clave is None:
        if clave_en_uso.strip() != "":
            clave = clave_en_uso 
        else:
            clave = "llaveuno"
    try:
        with open(nombre_archivo,"r",encoding="utf-8")as entrada:
            with open(nombre_archivo.replace(".gcf",".txt"),"w",encoding="utf-8")as salida:
                linea = entrada.readline()
                while linea != "":
                    mensaje_codificado = linea.strip("\n")
                    if mensaje_codificado == "":
                        break
                    decodificado=decode_text(clave, mensaje_codificado)
                    salida.write(decodificado + "\n")
                    linea=entrada.readline()
        print(" resultado >> Archivo decodificado exitosamente")        
    except FileNotFoundError:
        print(f" resultado >> ERROR! '{nombre_archivo}' no fue encontrado.")

def menu():
    print("┌────────────────────────────────────────────────────────────────────┐")
    print("│-----------------Proyecto codificador y decodificador---------------│")
    print("├────────────────────────────────────────────────────────────────────┤")
    print("│ Diego Mejia (25001764)                                             │")
    print("│ Salvador Solórzano (25001194)                                      │")
    print("├────────────────────────────────────────────────────────────────────┤")
    print("│ Seccion AN                                                         │")
    print("│ Grupo 6                                                            │")
    print("└────────────────────────────────────────────────────────────────────┘")
    print("")
    print("┌────────────────────────────────────────────────────────────────────┐")
    print("│------------------------Opciones del programa-----------------------│")
    print("├────────────────────────────────────────────────────────────────────┤")
    print("│ 1 - llave: setkey <nueva llave>                                    │")
    print("│ 2 - codificar texto: encode-text <Texto a cifrar>                  │")
    print("│ 3 - decodificar texto: decode-text <Texto cifrado>                 │")
    print("│ 4 - codificar archivo: encode-file <nombre del archivo>            │")
    print("│ 5 - decodificar archivo: decode-file <nombre del archivo>          │")
    print("│ 6 - salir del programa: quit                                       │")
    print("├────────────────────────────────────────────────────────────────────┤")
    print("│ NOTA: Lo que aparece en < > significa el nombre que le va a dar    │")
    print("│ ejemplo; setkey lemon                                              │")   
    print("└────────────────────────────────────────────────────────────────────┘")
    print("")

def main():
    menu()
    while True:
        seleccion=input("codificador >> ")
        lista1 = seleccion.strip().split()
        if len(lista1) >= 2:
            if (lista1[0]).lower() == "setkey":
                clave=setkey(lista1[1:])
                print(" resultado >> nueva llave aceptada")
            elif (lista1[0]).lower() == "encode-text":
                mensaje=" ".join(lista1[1:])
                codificado=encode_text(clave, mensaje)
            elif (lista1[0]).lower() == "decode-text":
                mensaje_codificado=" ".join(lista1[1:])
                decodificado=decode_text(clave, mensaje_codificado)
            elif (lista1[0]).lower() == "encode-file":
                nombre_archivo=" ".join(lista1[1:])
                encode_file(nombre_archivo, clave=None)
            elif (lista1[0]).lower() =="decode-file":
                nombre_archivo=" ".join(lista1[1:])
                decode_file(nombre_archivo, clave=None)
            elif (lista1[0]).lower() == "quit":
                print("Saliendo ...")
                print("┌────────────────────────────────────────────────────────────────────┐")
                print("│-----------------Gracias por usar nuestro programa------------------│")
                print("└────────────────────────────────────────────────────────────────────┘")
                break
            else:
                print(" resultado >> ERROR! Expresión no valida")
        else:
            print(" resultado >> ERROR! No ingreso la palabra solo la expresión")


main()