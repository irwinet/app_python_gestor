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