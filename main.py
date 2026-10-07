#run this file in your CLI (i.e. Command Prompt, Terminal, etc.) or IDE.

import os
import subprocess
import time

from .tools import earth_conv
from .tools import fiction_conv

from datetime import datetime

def clear():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])

RED = "\033[31m"
RESET = "\033[0m"

#-------------------------

def print_err(text):
    print(RED + text + RESET)
    time.sleep(3)
    clear()


def get_conversion_type():
    while True:
        conv_type = input(
"""
Fictional Date Converter
---------------------------
Choose a date conversion:
[1] Earth date to Fictional date
[2] Fictional date to Earth date

> """
        )

        if conv_type not in ["1", "2"]:
            print_err("Choose a value between 1 and 2!")
            continue

        else:
            return int(conv_type)

#----------------------------------

#Earth date validation

def is_leapyear(yr):
    return (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0)

days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

#----------------------------------

def get_date_input(conv_type):
    while True:

        if conv_type == 1: #earth-to-fictional
            earth_date = input(
"""
Fictional Date Converter
---------------------------
Enter Earth date (YYYY/MM/DD format).

> """
            )

            if earth_date.count('/') != 2:
                print_err("Invalid date format! Year, Month and Day must be separated by '/'.")
                continue

            else:
                year, month, day = earth_date.split('/')

                try:
                    year = int(year.strip())
                    month = int(month.strip())
                    day = int(day.strip())

                except ValueError:
                    print_err("Invalid date! Year, Month and Day must be numbers.")
                    continue

                if year == 0:
                    print_err("The year cannot be 0! Negative numbers are allowed, but not 0. There is no 0 CE / BCE.")
                    continue

                if month < 1 or month > 12:
                    print_err("The month must be between 1 and 12!")
                    continue

                if day < 1:
                    print_err("The day cannot be less than 1!")
                    continue

                if month == 2 and is_leapyear(year):
                    if day > 29:
                        print_err("The day of the month cannot be more than 29!")
                        continue

                else:
                    max_days = days_in_month[month - 1]
                    if day > max_days:
                        print_err(f"The day of the month cannot be more than {max_days}!")
                        continue

            break

        else: #fictional-to-earth
            pass

            break

    return datetime(year, month, day)


def get_time_input(conv_type):
    if conv_type == 1:

        while True:
            earth_time = input(
"""
Fictional Date Converter
---------------------------
Enter Earth time (hh:mm:ss format)
(optional, press Enter without any input to skip.)

> """
            )

            if earth_time.strip() == "":
                return 0, 0, 0

            else:
                pass


                break



        while True:
            tz = input(
"""
Fictional Date Converter
---------------------------
Enter timezone (UTC offset, e.g. -8.00)
(optional, press Enter without any input to skip.)

> """
            )

            if tz.strip() == "":
                return 0.00

            else:
                pass


                break





    else:
        pass





        


def convert_date(conv_type):
    if conv_type == 1:
        fictional_date = earth_conv.converter()



def main():
    conv_type = get_conversion_type()
    date = get_date_input(conv_type)
    time = get_time_input(conv_type)