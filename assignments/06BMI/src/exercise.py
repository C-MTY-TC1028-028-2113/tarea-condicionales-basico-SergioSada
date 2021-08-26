def main():
    #escribe tu código abajo de esta línea
    peso=float(input("Peso en kg: "))
    altura=float(input("Altura en m: "))
    if altura > 0 and peso > 0:
        indice=peso/altura**2
        if indice < 20:
            print("PESO BAJO")
        if 20 <= indice < 25:
            print("NORMAL")
        if 25 <= indice < 30:
            print("SOBREPESO")
        if 30 <= indice < 40:
            print("OBESIDAD")	
        if indice >= 40:
            print("OBESIDAD MORBIDA")
    else:
        print("Revisa tus datos, alguno de ellos es erróneo.")

if __name__=='__main__':
    main()