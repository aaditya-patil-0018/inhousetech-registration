import sqlite3

class DB:

    def __init__(self):
        # name of the database
        self.dbname = 'registration.db'
        # creating the connection with the database
        self.connection = sqlite3.connect(self.dbname)
        # creating the cursor object, so that we can interact with the database
        self.cursor = self.connection.cursor()
        # creating the database table if it already doesn't exists
        self.create()

    def create(self):
        # creating the database if it does not exists
        self.cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS registration 
                (   
                    serial_no INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    phone_no TEXT NOT NULL,
                    email_id TEXT NOT NULL
                )
            '''
        )
        # saving the database
        self.connection.commit()
        print("Table Creation process done!")

    def read(self):
        # select all the records inside the table
        self.cursor.execute("SELECT * FROM registration;")
        # fetching all the records from the database
        data = self.cursor.fetchall()
        # printing the data one by one
        for record in data:
            print(record)

    def update(self, fname, lname, phn, email):
        # Inserting the data into the table
        self.cursor.execute(
            '''
                INSERT INTO registration
                (first_name, last_name, phone_no, email_id)
                VALUES
                (?, ?, ?, ?)
            ''',
            (fname, lname, phn, email,)
        )
        # saving the database
        self.connection.commit()
        print("Table Updated with new Values!")

    def delete(self, id):
        # delete the record by the given unique serial id
        self.cursor.execute(
            '''
                DELETE FROM registration
                WHERE
                serial_no=?
            ''',
            (id,)
        )
        # saving the database
        self.connection.commit()
        print("The Record has been Deleted from the database!")