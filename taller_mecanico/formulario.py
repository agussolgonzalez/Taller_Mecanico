# Funciones
def recibir_matricula():
    patente = input('Ingrese la patente del vehiculo: ')
    return patente

def pat_exist(matr):
    flag = False
    mat_asoc = {
        'Patente_registrada': 'JKI203',
        'K.M': 1000,
        'Fecha de ultimo service': '10-08-2022',
        'Modelo': 'Peugot 206',
        'Año': 2010,
        'Marca de aceite y filtro utilizado': 'Marca Ejemplo'
    }
    if matr == mat_asoc['Patente_registrada']:
        flag = True
        print('Este es una patente asociada, pasamos a mostrar los detalles: ')
        print('-------------------------------------------------------------------------------------------------------------------------')
        print(mat_asoc)
        print('-----------------------------------------------------------------------------------------------------------------------------')
        prox = calc_prox_serv(mat_asoc['K.M'])
        print('El proximo service lo necesita a los: ', prox, 'km.')
    else:
        
        print('Cliente nuevo')
        print('-------------------------------------------------------------------------------------------------------------------------')
    return flag

def cliente_nuevo(x):
    nuevo_auto = {}
    patente = x
    km = int(input('Ingrese el kilometraje del vehiculo: '))
    ultimo_service = input('Ingrese la ultima fecha de service en formato dd/mm/aa: ')
    modelo = input('Ingrese el modelo del auto y el año: ')
    servicio = input('Ingrese el servicio que se realizo: ')
    nuevo_auto = {
        'Patente:': patente,
        'Km: ': km,
        'Fecha de ultimo service: ':ultimo_service,
        'Modelo: ': modelo,
        'Marca de aceite y filtro utilzado: ': servicio
    }
    print('-----------------------------------------------------------------------------------------------------------------------------------')
    print('Guardando datos.......')
    print('Datos guardados con exito.')
    print(nuevo_auto)
    return nuevo_auto['Km: ']
def calc_prox_serv(x):
    nuevo_service = x + 15000
    print('El proximo servicio es a los : ',nuevo_service,'km.')
    return nuevo_service


# Proyecto main
opc = 0
while opc != 2:
    opc = int(input('Ingrese 1 para ingresar un vehiculo o 2 para terminar: '))
    if opc == 1:
        pat = recibir_matricula()
        z = pat_exist(pat)
        if z == False:
            q = cliente_nuevo(pat)
            p = calc_prox_serv(q)
    else:
        print('Gracias..')