import copy
import unittest
import database as db
import helpers
import config
import csv

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

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('232323', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.borrar('15J')
        db.Clientes.modificar('28Z', 'Mariana', 'Garcia')

        dni, nombre, apellido = None, None, None 
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, '28Z')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(dni, '28Z')