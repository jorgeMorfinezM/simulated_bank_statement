# -*- coding: utf-8 -*-

"""
Requires Python 3.8 or later
"""

__author__ = "Jorge Morfinez Mojica (jorge.morfinez.m@gmail.com)"
__copyright__ = "Copyright 2021"
__license__ = ""
__history__ = """ """
__version__ = "1.21.F21.1 ($Rev: 1 $)"

import json
import random
import string
from datetime import timedelta, datetime


class DataFillClass:

    @staticmethod
    def fill_string_fixed_data(fixed_list_data, data_format):
        # rows_list = []
        #
        # n = 0
        #
        # while n < data_qty:
        #     result_str = random.choice(fixed_list_data)
        #
        #     rows_list.append("" + str(result_str) + "")
        #
        #     n += 1
        #
        # return rows_list

        result_str = random.choice(fixed_list_data)

        return "" + str(result_str) + ""

    @staticmethod
    def fill_date_data(data_prefix, start, end):
        # rows_list = []
        # n = 0
        #
        # """Return a random date between two datetime objects start and end"""
        #
        # while n < data_qty:
        #     delta = end - start
        #
        #     int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        #
        #     random_second = random.randrange(int_delta)
        #
        #     date_time_random = start + timedelta(seconds=random_second)
        #
        #     # FALTA FORMATEAR A dd/mm/aaaa
        #     date_random = date_time_random.date().strftime("%d/%m/%Y")
        #
        #     rows_list.append(date_random)
        #
        #     n += 1
        #
        # return rows_list

        delta = end - start

        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds

        random_second = random.randrange(int_delta)

        date_time_random = start + timedelta(seconds=random_second)

        date_random = date_time_random.date().strftime("%d/%m/%Y")

        return date_random

    @staticmethod
    def fill_string_digits_data(data_len, data_prefix, data_format):

        letters_digits = string.digits  # para letras ramdom lower

        input_str = str(data_prefix) + str(letters_digits)

        result_str = ''.join(random.choice(input_str) for _ in range(data_len))

        return result_str

        # rows_list = []
        #
        # n = 0
        #
        # letters_digits = string.digits  # para letras ramdom lower
        #
        # input_str = str(data_prefix) + str(letters_digits)
        #
        # while n < data_qty:
        #     result_str = ''.join(random.choice(input_str) for _ in range(data_len))
        #
        #     # print("Random string of length", data_qty, "is:", result_str)
        #
        #     rows_list.append("" + str(result_str) + "")
        #
        #     n += 1
        #
        # return rows_list

    @staticmethod
    def fill_amount_integer_data(data_prefix, data_format):
        ammount_data = str()

        ammount_data = random.uniform(100, 100000)

        ammount_data = data_format.format(ammount_data)

        ammount_data = "" + str(data_prefix) + str(ammount_data) + ""

        return ammount_data

        # n = 0
        # ammount_data = str()
        # rows_list = []
        #
        # while n < data_qty:
        #     ammount_data = random.uniform(100, 100000)
        #
        #     ammount_data = str(data_prefix) + str(int(ammount_data))
        #
        #     # print(decimal_formatting(ammount_data))
        #     rows_list.append(ammount_data)
        #
        #     n += 1
        #
        # return rows_list

    @staticmethod
    def fill_time_formated_data(data_prefix, start, end):

        delta = end - start

        init_delta = (delta.days * 24 * 60 * 60) + delta.seconds

        random_time = random.randrange(init_delta)

        date_time_random = start + timedelta(seconds=random_time)

        time_random = date_time_random.time().strftime("%H.%M")

        return time_random
        # rows_list = []
        # n = 0
        #
        # while n < data_qty:
        #     delta = end - start
        #
        #     init_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        #
        #     random_time = random.randrange(init_delta)
        #
        #     date_time_random = start + timedelta(seconds=random_time)
        #
        #     time_random = date_time_random.time().strftime("%H.%M")
        #
        #     rows_list.append(time_random)
        #
        #     n += 1
        #
        # return rows_list
