def calcular_precio_producto(coste_producto):
    costo = (coste_producto * 0.5) + coste_producto
    return costo


def calcular_precio_servicio(cantidad_horas):
    servicio = (cantidad_horas * 100000)
    return servicio


def calcular_precio_servicio_extras(cantidad_horas):
    extra = (calcular_precio_servicio(cantidad_horas) * 0.25) + calcular_precio_servicio(cantidad_horas)
    return extra


def calcular_costo_envio(kilometros):
    recargo = (kilometros * 115)
    return recargo


def calcular_precio_producto_fuera(coste_producto, kilometros):
    costo = calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)
    return costo


def calcular_iva_producto(coste_producto, tasa):
    tasa = tasa / 100
    iva_producto = calcular_precio_producto(coste_producto) * tasa
    return iva_producto


def calcular_iva_servicio(cantidad_horas, tasa):
    tasa = tasa / 100
    iva_servicio = calcular_precio_servicio(cantidad_horas) * tasa
    return iva_servicio


def calcular_iva_envio(kilometros, tasa):
    tasa = tasa / 100
    iva_envio = calcular_costo_envio(kilometros) * tasa
    return iva_envio


def calcular_iva_servicio_extra(cantidad_horas, tasa):
    tasa = tasa / 100
    iva_extra = calcular_precio_servicio_extras(cantidad_horas) * tasa
    return iva_extra


def calcular_recaudo_locales(coste_producto_1, coste_producto_2, coste_producto_3):
    recaudo_locales = (calcular_precio_producto(coste_producto_1) + calcular_precio_producto(coste_producto_2)
                       + calcular_precio_producto(coste_producto_3)) * 0.5
    return recaudo_locales


def calcular_recaudo_horas_extra(horas_1, horas_2, horas_3, horas_4):
    recaudo_extra = calcular_precio_servicio_extras(horas_1) + calcular_precio_servicio_extras(horas_2) + \
                    calcular_precio_servicio_extras(horas_3) + calcular_precio_servicio_extras(horas_4)
    return recaudo_extra


def calcular_recaudo_mixto_local(coste_producto_1, coste_producto_2, horas_1, horas_2):
    mixto_local = ((calcular_precio_producto(coste_producto_1) + calcular_precio_producto(coste_producto_2)) * 0.5) + \
                  calcular_precio_servicio(horas_1) + calcular_precio_servicio(horas_2)
    return mixto_local