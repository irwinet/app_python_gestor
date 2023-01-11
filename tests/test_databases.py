import copy
import unittest
import database as db

class TesDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15J','Marta', 'Perez'),
            db.Cliente('48H', 'Manolo', 'Lopez'),
            db.Cliente('28Z', 'Ana', 'Garcia')
        ]
    
    def test_buscar_cliente(self):
        cliente_existe = db.Clientes.buscar('15J')
        cliente_inexiste = db.Clientes.buscar('99X')
        self.assertIsNotNone(cliente_existe)
        self.assertIsNone(cliente_inexiste)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39X', 'Irwin', 'Estrada')        
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Irwin')
        self.assertEqual(nuevo_cliente.apellido, 'Estrada')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('28Z'))
        cliente_modificado = db.Clientes.modificar('28Z', 'Mariana', 'Garcia')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('48H')
        cliente_rebuscado = db.Clientes.buscar('48H')
        self.assertEqual(cliente_borrado.dni, '48H')
        self.assertIsNone(cliente_rebuscado)
