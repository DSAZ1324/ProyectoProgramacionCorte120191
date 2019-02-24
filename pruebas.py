import unittest
import funciones as f


class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):
        self.assertEqual(f.calcular_precio_producto(1000), 1500)
        self.assertEqual(f.calcular_precio_producto(0), 0)

    def test_calcular_precio_servicio(self):
        self.assertEqual(f.calcular_precio_servicio(3), 300000)
        self.assertEqual(f.calcular_precio_servicio(0), 0)

    def test_calcular_precio_servicio_extras(self):
        self.assertEqual(f.calcular_precio_servicio_extras(5), 625000)
        self.assertEqual(f.calcular_precio_servicio_extras(0), 0)

    def test_calcular_costo_envio(self):
        pass

    def test_calcular_precio_producto_fuera(self):
        self.assertEqual(f.calcular_precio_producto_fuera(5000, 50), 13250)
        self.assertEqual(f.calcular_precio_producto_fuera(0, 0), 0)
        self.assertEqual(f.calcular_precio_producto_fuera(5000, 0), 7500)
        self.assertEqual(f.calcular_precio_producto_fuera(0, 60), 6900)

    def test_calcular_iva_producto(self):
        pass

    def test_calcular_iva_servicio(self):
        self.assertEqual(f.calcular_iva_servicio(5, 19), 95000)
        self.assertEqual(f.calcular_iva_servicio(0, 0), 0)
        self.assertEqual(f.calcular_iva_servicio(5, 0), 0)
        self.assertEqual(f.calcular_iva_servicio(0, 19), 0)

    def test_calcular_iva_envio(self):
        pass

    def test_calcular_iva_servicio_extra(self):
        self.assertEqual(f.calcular_iva_servicio_extra(5, 19), 118750)
        self.assertEqual(f.calcular_iva_servicio_extra(0, 0), 0)
        self.assertEqual(f.calcular_iva_servicio_extra(0, 19), 0)
        self.assertEqual(f.calcular_iva_servicio_extra(5, 0), 0)

    def test_calcular_recaudo_locales(self):
        pass

    def test_calcular_recaudo_horas_extra(self):
        self.assertEqual(f.calcular_recaudo_horas_extra(1, 2, 3, 4), 1250000)
        self.assertEqual(f.calcular_recaudo_horas_extra(0, 0, 0, 0), 0)
        self.assertEqual(f.calcular_recaudo_horas_extra(1, 2, 3, 0), 750000)

    def test_calcular_recaudo_mixto_local(self):
        pass


if __name__ == 'main':
    unittest.main()
