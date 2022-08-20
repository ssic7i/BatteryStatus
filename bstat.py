import psutil
import datetime


def battery_data():
    battery = psutil.sensors_battery()
    return {
        'power_plugged': battery.power_plugged,
        'percent': battery.percent,
        'left_time': str(datetime.timedelta(seconds=battery.secsleft)) if not battery.power_plugged else '-1'
    }


if __name__ == '__main__':
    print(battery_data())
