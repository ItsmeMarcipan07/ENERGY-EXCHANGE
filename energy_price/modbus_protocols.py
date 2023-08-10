import struct
from energy_price.connection import connection_plc
from energy_price.base_hour_price import base_hour


def write_modbus():
    # sending information/write #
    value = 134.34
    value_hex = struct.pack('!f', value)
    register1 = int.from_bytes(value_hex[0:2], byteorder='big')
    register2 = int.from_bytes(value_hex[2:], byteorder='big')
    first_part = connection_plc().write_registers(0x001, 0x4359, unit=1)
    second_part = connection_plc().write_registers(0x002, 0xcf5c, unit=1)


def read_modbus():
    sunrise_hour_read = connection_plc().read_holding_registers(0x001, 1, unit=1)
    sunrise_minutes_read = connection_plc().read_holding_registers(0x002, 1, unit=1)
    return sunrise_hour_read
