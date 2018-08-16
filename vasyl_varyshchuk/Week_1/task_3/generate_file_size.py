"""
This module returns random size of file
"""

import random

list_of_files = ['reports.txt', 'monthly_reports.zip', 'README.txt',
                 'picture.jpg', 'logo.ttf', 'config.ini']


def recognize_file_type(file_name):
    _, extension = file_name.split('.')
    return extension


def txt_handler():
    return random.randint(100, 450)


def zip_handler():
    return random.randint(500, 700)


def jpg_handler():
    return random.randint(800, 1000)


def ttf_handler():
    return random.randint(1100, 1300)


def ini_handler():
        return random.randint(1300, 1500)


functions = {
    'txt': txt_handler,
    'zip': zip_handler,
    'jpg': jpg_handler,
    'ttf': ttf_handler,
    'ini': ini_handler
 }


def run_executors(file_name):
    extension = recognize_file_type(file_name)

    size = functions[extension]()
    print('Generated size of {} file => {}'.format(extension, size))


# Example of use for single file name
run_executors('some_file.txt')
# Run with map for list of file names
map(run_executors, list_of_files)
