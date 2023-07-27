#Melakukan Import mysql Connector
import mysql.connector
import csv

host = 'localhost'
user = 'username'
password = 'password'
database = 'database_name'

# Melakukan percobaan koneksi
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Membuat object cursor sebagai
cursor = conn.cursor()

# Deklarasi SQL Query untuk memasukkan record ke DB (Karyawan)
insert_sql = (
    "INSERT INTO Karyawan (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
    "VALUES (%s, %s, %s, %s, %s)"
)

# Data yang akan dimasukkan ke dalam tabel
values = ('Yanto', 'Mizwar', 25, 'Laki-laki', 75000)

try:
    # Eksekusi SQL Command
    cursor.execute(insert_sql, values)

    # Melakukan perubahan (commit) pada DB
    conn.commit()

except mysql.connector.Error as err:
    # Roll Back apabila ada issue
    print("Error:", err)
    conn.rollback()

# Menutup koneksi
cursor.close()
conn.close()

