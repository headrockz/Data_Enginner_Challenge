import sqlite3
import pandas as pd


class LoadDb:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def create(self):
        table = '''
        CREATE TABLE IF NOT EXISTS "locations" (
            "id_location" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "longitude"	TEXT,
            "latitude"	TEXT,
            "gallons_arrival"	REAL,
            "gallons_departure"	REAL,
            "arrived"	TEXT,
            "departed"	TEXT
        );
        '''
        self.cursor.execute(table)

    def insert(self, id_location, longitude, latitude, gallons_arrival, gallons_departure, arrived, departed):
        consult = '''
        insert or ignore into locations (id_location, longitude, latitude, gallons_arrival, gallons_departure, arrived, departed) values (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(consult, (id_location, longitude, latitude, gallons_arrival,
        gallons_departure, arrived, departed))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# Tests
if __name__ == '__main__':
    data = LoadDb('database.db')

    df = pd.read_excel('data.xlsx')

    data.create()

    for i in df.values:
        data.insert(i[0], i[1], i[2], i[4], i[6], i[3], i[5])
        
    data.close()
