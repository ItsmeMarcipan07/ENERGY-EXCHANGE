from connection import connection_plc
from base_hour_price import base_hour

def write_modbus():
    # sending information/write #
    sunrise_hour_write = connection_plc().write_registers(0x000,
                                                          float(base_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv')[0]),
                                                          unit=0x1)
    # sunrise_minutes_write = connection.connection_plc().write_registers(0x001,
    #                                                                     int(weather_config.get_sunrise().split(":")[1]),
    #                                                                     unit=config.UNIT)
    # sunset_hour_write = connection.connection_plc().write_registers(0x002,
    #                                                                 int(weather_config.get_sunset().split(":")[0]),
    #                                                                 unit=config.UNIT)
    # sunset_minutes_write = connection.connection_plc().write_registers(0x003,
    #                                                                    int(weather_config.get_sunset().split(":")[1]),
    #                                                                    unit=config.UNIT)
    # current_temperature_write = connection.connection_plc().write_registers(0x004,
    #                                                                         int(weather_config.get_temperature()),
    #                                                                         unit=config.UNIT)
    # local_hour_write = connection.connection_plc().write_registers(0x005,
    #                                                                int(weather_config.get_local_time()
    #                                                                    [3].split(":")[0]),
    #                                                                unit=config.UNIT)
    # local_minutes_write = connection.connection_plc().write_registers(0x006,
    #                                                                   int(weather_config.get_local_time()
    #                                                                       [3].split(":")[1]),
    #                                                                   unit=config.UNIT)

    return sunrise_hour_write


def read_modbus():
    # reading information/read #
    sunrise_hour_read = connection_plc().read_holding_registers(0x000, 1, unit=0x1)
    # sunrise_minutes_read = connection.connection_plc().read_holding_registers(0x001, 1, unit=config.UNIT)
    # sunset_hour_read = connection.connection_plc().read_holding_registers(0x002, 1, unit=config.UNIT)
    # sunset_minutes_read = connection.connection_plc().read_holding_registers(0x003, 1, unit=config.UNIT)
    # current_temperature_read = connection.connection_plc().read_holding_registers(0x004, 1, unit=config.UNIT)
    # local_hour_read = connection.connection_plc().read_holding_registers(0x005, 1, unit=config.UNIT)
    # local_minutes_read = connection.connection_plc().read_holding_registers(0x006, 1, unit=config.UNIT)

    return sunrise_hour_read