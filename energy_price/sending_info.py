import sys
import pathlib
from tkinter import messagebox

sys.path.insert(1, f"{pathlib.Path().resolve()}")
messagebox.showinfo(title="INFO WINDOW", message=f"Connecting...\nClick OK!")
import modbus_protocols
import connection
from time import *

while True:
    connection.connection_plc()
    modbus_protocols.write_modbus()
    modbus_protocols.read_modbus()
    sleep(15)
