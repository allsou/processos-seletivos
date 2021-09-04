import csv
import traceback

import psycopg2
from psycopg2.errors import UniqueViolation

import settings
from parsers.market import MarketParser

ID_INDEX = 0
LONG_INDEX = 1
LAT_INDEX = 2
SETCENS_INDEX = 3
AREAP_INDEX = 4
CODDIST_INDEX = 5
CODSUBPREF_INDEX = 7
NUMERO_INDEX = 14
try:
    print('Starting migration...')
    connection = psycopg2.connect(
        host='postgre', dbname=settings.DATABASE_NAME, user=settings.DATABASE_USER, password=settings.DATABASE_PASSWORD
    )
    print('Database connected.')
    cursor = connection.cursor()
    print('Cursor opened, creating table if not exists...')
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {settings.TABLE_NAME} ("
                   f"id serial PRIMARY KEY,"
                   f"long integer,"
                   f"lat integer,"
                   f"setcens bigint,"
                   f"areap bigint,"
                   f"coddist integer,"
                   f"distrito varchar(300),"
                   f"codsubpref integer,"
                   f"subprefe varchar(300),"
                   f"regiao5 varchar(300),"
                   f"regiao8 varchar(300),"
                   f"nome_feira varchar(300),"
                   f"registro varchar(10) UNIQUE NOT NULL,"
                   f"logradouro varchar(300),"
                   f"numero varchar(10),"
                   f"bairro varchar(300),"
                   f"referencia varchar(300)"
                   f");"
                   )
    connection.commit()
    print('Table created or already created successfully')
    print('Loading data from csv file')
    with open('datasource/DEINFO_AB_FEIRASLIVRES_2014.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        print('csv file loaded, starting insertion...')
        for row in csv_reader:
            if len(row) < 17:
                row.append('')
            row[ID_INDEX] = int(row[ID_INDEX])
            row[LONG_INDEX] = int(row[LONG_INDEX])
            row[LAT_INDEX] = int(row[LAT_INDEX])
            row[SETCENS_INDEX] = int(row[SETCENS_INDEX])
            row[AREAP_INDEX] = int(row[AREAP_INDEX])
            row[CODDIST_INDEX] = int(row[CODDIST_INDEX])
            row[CODSUBPREF_INDEX] = int(row[CODSUBPREF_INDEX])
            row[NUMERO_INDEX] = MarketParser.number_from_csv_to_int(number=row[NUMERO_INDEX])
            try:
                cursor.execute('INSERT INTO markets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,'
                               ' %s, %s, %s, %s, %s, %s, %s, %s)', row)
            except UniqueViolation:
                connection.rollback()
                print(f'Row duplicated, continue | {row}')
    print('Sync serial id')
    cursor.execute('SELECT SETVAL((SELECT PG_GET_SERIAL_SEQUENCE(\'"markets"\', \'id\')),'
                   ' (SELECT (MAX("id") + 1) FROM "markets"), FALSE);')
    print('Insertion done')
    connection.commit()
    print('Committed changes')
    cursor.close()
    print('Cursor closed')
    connection.close()
    print('Connection closed, migration done')
except Exception as exception:
    print(traceback.format_exc())
    print('An undefined error occur when migrate data')
