import random
import sqlite3

with sqlite3.connect("liftup.db") as connect:
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS liftup(Ariza_Turu TEXT, Nominal_Deger INT, Calisma_Araligi TEXT, Akim FLOAT, Gerilim FLOAT)")
    cursor.execute("INSERT INTO liftup VALUES('Yüksek Sicaklik',0.096,'0.096ohm - 0.2ohm', 11.82, 18.53)")
    cursor.execute("INSERT INTO liftup VALUES('Kablo Kopmasi',0,'0', 0, 0)")
    cursor.execute("INSERT INTO liftup VALUES('Kisa Devre',0,'0', 0, 0)")
    cursor.execute("INSERT INTO liftup VALUES('Yüksek Gerilim',28,'28V - 35V', 17.92, 28.10)")
    cursor.execute("INSERT INTO liftup VALUES('Alcak Gerilim',28,'23V - 28V', 11.78, 18.47)")
    connect.commit()

# Yüksek Sıcaklık:
def temperature():
    for i in range(10):
        value_range = random.uniform(0.000,0.35)
        if value_range < 0.096:
            print(f"{i+1}) {value_range}V  WARNING !!! Below nominal value!")
        elif value_range > 0.2:
            print(f"{i+1}) {value_range}V  WARNING !!! Above nominal value")
        else:
            print(f"{i+1}) ","It operates at normal value")

# Yüksek Gerilim:
def high_voltage():
    for i in range(10):
        value_range = random.randint(22,40)
        if value_range < 28:
            print(f"{i+1}) {value_range}V  WARNING !!! Below nominal value!")
        elif value_range > 35:
            print(f"{i+1}) {value_range}V  WARNING !!! Above nominal value")
        else:
            print(f"{i+1}) ","It operates at normal value")


# Alçak Gerilim:
def low_Voltage():
    for i in range(10):
        value_range = random.randint(15,35)
        if value_range < 23:
            print(f"{i+1}) {value_range}V  WARNING !!! Below nominal value!")
        elif value_range > 28:
            print(f"{i+1}) {value_range}V  WARNING !!! Above nominal value")
        else:
            print(f"{i+1}) ","It operates at normal value")

temperature()
print("\n")
high_voltage()
print("\n")
low_Voltage()
