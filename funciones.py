def calcular_precio_producto(coste_producto):
    """
    num -> num

    Calcula el costo de un producto con una comision del 50% sobre el costo de fabrica

    >>> calcular_precio_producto(1000)
    1500.0

    >>> calcular_precio_producto(2000)
    3000.0

    :param coste_producto: num que representa el costo de fabrica del producto
    :return: num que representa el costo de fabrica mas el 50%
    """
    costo = (coste_producto * 0.5) + coste_producto
    return costo


def calcular_precio_servicio(cantidad_horas):
    """
    num -> num

    Calcula el costo del servicio segun las horas realizadas

    >>> calcular_precio_servicio(3)
    300000

    >>> calcular_precio_servicio(5)
    500000

    :param cantidad_horas: num que representa numero de horas trabajadas
    :return: num que representa el costo del servicio
    """
    servicio = (cantidad_horas * 100000)
    return servicio


def calcular_precio_servicio_extras(cantidad_horas):
    """
    num -> num

    Calcula el precio del servicio cuando trabaja horas extra

    >>> calcular_precio_servicio_extras(3)
    375000.0

    >>> calcular_precio_servicio_extras(6)
    750000.0

    :param cantidad_horas: num que representa las horas extra
    :return: num que representa el precio de las horas trabajadas mas el 25%
    """
    extra = (calcular_precio_servicio(cantidad_horas) * 0.25) + calcular_precio_servicio(cantidad_horas)
    return extra


def calcular_costo_envio(kilometros):
    pass


def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    """
    num -> num

    calcula el preciod e un producto teniendo en cuenta los costos del envio

    >>> calcular_precio_producto_fuera(5000, 500)
    65000.0

    >>> calcular_precio_producto_fuera(3000, 50)
    10250.0

    :param coste_producto: num que representa el costo de fabrica del producto
    :param kilometros: num que representa los kilometros recorridos en el envio
    :return: num que representa el costo final del producto mas el costo del envio
    """
    costo = calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)
    return costo


def calcular_iva_producto(coste_producto, tasa):
    pass

def calcular_iva_servicio(cantidad_horas, tasa):
    """
    num -> num

    calcula el iva del precio del servicio

    >>> calcular_iva_servicio(10, 19)
    190000.0

    >>> calcular_iva_servicio(15, 10)
    150000.0

    :param cantidad_horas: num que representa la cantidad de horas de servicio
    :param tasa: num que representa la cantidad de iva a calcular
    :return: num que representa el iva del servicio
    """
    tasa = tasa/100
    iva_servicio = calcular_precio_servicio(cantidad_horas) * tasa
    return iva_servicio


def calcular_iva_envio(kilometros, tasa):
    pass


def calcular_iva_servicio_extra(cantidad_horas, tasa):
    pass
    """
    num -> num

    calcula el iva del precio del servicio en horas extra

    >>> calcular_iva_servicio_extra(3, 19)
    71250.0

    >>> calcular_iva_servicio_extra(6, 10)
    75000.0

    :param cantidad_horas: num que representa la cantidad de horas extra
    :param tasa: num que representa la cantidad de iva a calcular
    :return: num que representa el costo de un servicio en horas extra mas el iva
    """
    tasa = tasa/100
    iva_extra = calcular_precio_servicio_extras(cantidad_horas) * tasa
    return iva_extra


def calcular_recaudo_locales(coste_producto_1, coste_producto_2, coste_producto_3):
    pass


def calcular_recaudo_horas_extra(horas_1, horas_2, horas_3, horas_4):
    """
    num -> num

    calcula el recaudo de 4 servicios realizados en horas extra

    >>> calcular_recaudo_horas_extra(1, 2, 3, 4)
    1250000.0

    >>> calcular_recaudo_horas_extra(2, 3, 4, 5)
    1750000.0

    :param horas_1: num que representa las horas extra trabajadas en el servicio #1
    :param horas_2: num que representa las horas extra trabajadas en el servicio #2
    :param horas_3: num que representa las horas extra trabajadas en el servicio #3
    :param horas_4: num que representa las horas extra trabajadas en el servicio #4
    :return: num que representa el recaudo total de los 4 servicios prestados en horas extras
    """
    recaudo_extra = calcular_precio_servicio_extras(horas_1) + calcular_precio_servicio_extras(horas_2) + \
                    calcular_precio_servicio_extras(horas_3) + calcular_precio_servicio_extras(horas_4)
    return recaudo_extra

  
def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    
