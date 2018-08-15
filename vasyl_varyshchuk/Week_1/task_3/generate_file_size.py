"""
This module returns random size of file
"""

import random

list_of_files = ['reports.txt', 'monthly_reports.zip', 'README.txt',
                 'picture.jpg', 'logo.ttf', 'config.ini']


def recognize_file_type(a_file):
    return a_file.split('.')[1]


def run_executors(file_name):
    def txt_handler(file_ext):
        return random.randint(100, 450) if file_ext == 'txt' else None

    def zip_handler(file_extension):
        return random.randint(500, 700) if file_extension == 'zip' else None

    def jpg_handler(file_extension):
        return random.randint(800, 1000) if file_extension == 'jpg' else None

    def ttf_handler(file_extension):
        return random.randint(1100, 1300) if file_extension == 'ttf' else None

    def ini_handler(file_extension):
        return random.randint(1300, 1500) if file_extension == 'ini' else None

    ext = recognize_file_type(file_name)

    functions = {
        'txt': txt_handler,
        'zip': zip_handler,
        'jpg': jpg_handler,
        'ttf': ttf_handler,
        'ini': ini_handler
    }

    choosed_func = functions[ext]
    size = choosed_func(ext)

    print('Generated size of .{} file => {}'.format(ext, size))


# Example of use for single file name
run_executors('some_file.txt')
# Run with map for list of file names
map(run_executors, list_of_files)
