import requests
from datetime import datetime
import os
from time import sleep


# while True:
succes_file = open('files/access.log', "a")
error_file = open('files/error.log', "a")
# sleep(1)

try:
    TODAY = datetime.today().strftime("%d.%m.%Y")
    URL = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={TODAY}"

    response = requests.get(URL)
    PB = response.json()

    print(type(PB))
    print(type(PB['exchangeRate']))
    # for row in PB['exchangeRate']:
    #     print(row)

    succes_file.write(f"| {os.getlogin()} | {datetime.today().strftime('%d.%m.%Y %H:%M:%S')}\
| {str(response.status_code)} {str(response.reason)} Operation success!\n")
except Exception as ex:
    error_file.write(f"| {os.getlogin()} | {datetime.today().strftime('%d.%m.%Y %H:%M:%S')}\
| {str(response.status_code)} {str(response.reason)} Operation failed!\n")
finally:
    succes_file.close()
    error_file.close()


# Створити модуль з наступними функціями:
#  - запис даних у JSON