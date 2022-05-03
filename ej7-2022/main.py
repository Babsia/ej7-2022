from Viajerofrecuente import viajeroFrecuente
if __name__=='__main__':
    print('ej7')
    unviajero=viajeroFrecuente(1,'42853372','santiago','babsia',3800)
    
    millascomp=int(input('ingrese la cantidad de millas para comparar con el viajero numero 1 '))
    if unviajero==millascomp:
        print('la cantidad de millas ingresadas es igual a las del viajero numero 1')
    else:
        print('la cantidad de millas ingresadas es distinta a las del viajero numero 1')
    millascomp=int(input('ingrese la cantidad de millas para comparar con el viajero numero 1 por derecha '))
    if millascomp==unviajero:
        print('la cantidad de millas ingresadas es igual a las del viajero numero 1')
    else:
        print('la cantidad de millas ingresadas es distinta a las del viajero numero 1')
    millas=int(input('ingrese la cantidad de millas a acumular en el viajero: '))
    unviajero=millas+unviajero
    print(unviajero)
    millasc=int(input('ingrese la cantidad de millas a canjear en el viajero: '))
    unviajero=millasc-unviajero
    print(unviajero)



    