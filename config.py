import sys 

DATABASE_PATH='Clientes.csv'

if "pytest" in sys.argv[0]:
    DATABASE_PATH="tests/Clientes_test.csv"