import sqlite3
import pandas as pd


class LoadInfos:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def create(self):
        table = '''
            CREATE TABLE IF NOT EXISTS "infos" (
                "id_info"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "distance"	REAL NOT NULL,
                "time"	REAL NOT NULL,
                "gallons"	REAL NOT NULL,
                "miles_hour"	REAL NOT NULL,
                "fk_departed"	INTEGER NOT NULL,
                "fk_arrived"	INTEGER NOT NULL,
                FOREIGN KEY("fk_arrived") REFERENCES "locations"("id_location"),
                FOREIGN KEY("fk_departed") REFERENCES "locations"("id_departed")
            );
        '''
        self.cursor.execute(table)

    def insert(self, id_info, distance, time, gallons, miles_hour, fk_arrived, fk_departed):
        consult = '''
            insert or ignore into infos (id_info, distance, time, gallons, miles_hour, fk_arrived, fk_departed)
            values (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(consult, (id_info, distance, time, gallons, miles_hour, fk_arrived, fk_departed))
        self.conn.commit()

    def search_arrival_depart(self):

        self.cursor.execute('select id_info, fk_arrived, fk_departed, max(miles_hour) from infos')

        id_max_speed = self.cursor.fetchall()

        self.cursor.execute(f'select longitude, latitude from locations where id_location={id_max_speed[0][1]}')
        result = self.cursor.fetchall()
        longitude_arrived, latitude_arrived = result[0]
 
        self.cursor.execute(f'select longitude, latitude from locations where id_location={id_max_speed[0][2]}')
        result = self.cursor.fetchall()
        longitude_departed, latitude_departed = result[0]

        return longitude_arrived, latitude_arrived, longitude_departed, latitude_departed

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    data = LoadInfos('database.db')

    print(data.search_arrival_depart())
