import sys
import pathlib

sys.path.insert(1, f"{pathlib.Path().resolve()}")
from pymodbus.client import ModbusTcpClient as ModbusClient
from tkinter import messagebox


def connection_plc():
    client = ModbusClient("127.0.0.1", 502)  # create modbus client with PLC_IP and PLC_PORT
    client.connect()  # create connection
    return client  # return connection


try:
    connection_plc()
    messagebox.showinfo(title="INFO WINDOW", message="Connected to PLC!")
    print("Connected!")

except Exception:
    messagebox.showerror("Error", str(e))
    connection_plc().close()
    raise OSError("Fail to connect!")