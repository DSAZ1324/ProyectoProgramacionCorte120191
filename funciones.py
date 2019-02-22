def calcular_precio_producto(coste_producto):
    '''
    num -> num

    Calcular el costo de un producto con una comision del 50% sobre el costo de fabrica

    >>> calcular_precio_producto(1000)
    1500.0

    >>> calcular_precio_producto(2000)
    3000.0

    :param coste_producto: num que representa el costo de fabrica del producto
    :return: num que representa el costo de fabrica mas el 50%
    '''

    Costo = (coste_producto * 0.5) + coste_producto
    return Costo



def calcular_precio_servicio(cantidad_horas):

    '''
    num -> num

    calcula el costo del servicio segun las horas realizadas

    >>> calcular_precio_servicio(3)
    300000

    >>> calcular_precio_servicio(5)
    500000

    :param cantidad_horas:num que representa numero de horas trabajadas
    :return: num que representa el costo del servicio
    '''
    servicio = (cantidad_horas * 100000)
    return servicio




def calcular_precio_servicio_extras(cantidad_horas):
    pass


def calcular_costo_envio(kilometros):
    pass

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    pass


def calcular_iva_producto(coste_producto, tasa):
    pass


def calcular_iva_servicio(cantidad_horas, tasa):
    pass


def calcular_iva_envio(kilometros, tasa):
    pass


def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    pass


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    pass

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    pass


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    pass