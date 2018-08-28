""""
This module returns random size of file name from list by processing elements in separate processes
"""

import random
import string
import ConfigParser
from multiprocessing import Process

config = ConfigParser.ConfigParser()
path_to_config_file = '/home/vasyl/GL_Trainee/training_newcomers/vasyl_varyshchuk/Week_2/task_1/config.ini'
config.read(path_to_config_file)
number_of_processes = int(config.get('Main', 'number_of_processes'))

length_of_file_names_list = number_of_processes * 100


def recognize_file_type(file_name):
    """This function returns extension of file passing file name as parameter"""
    _, extension = file_name.split('.')
    return extension


def generate_file_names_list():
    """
    This function generate list of files with random names.
    Length of list is specified by global variable
    length_of_file_names_list which value depend on number of processes.
    """
    extensions = ['txt', 'zip', 'ini', 'jpg', 'ttf']
    file_names = []
    for i in range(length_of_file_names_list):
        file_name = ''.join([random.choice(string.ascii_lowercase) for j in range(5)])
        file_name_with_extension = '.'.join([file_name, random.choice(extensions)])
        file_names.append(file_name_with_extension)
    return file_names


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


handlers = {
    'txt': txt_handler,
    'zip': zip_handler,
    'jpg': jpg_handler,
    'ttf': ttf_handler,
    'ini': ini_handler
 }


def choose_handlers(list_of_file_names):
    """This function runs handlers for corresponding file extensions"""
    extensions = map(recognize_file_type, list_of_file_names)
    for extension in extensions:
        handler = handlers[extension]
        result = handler()
        print('Generated size for .{} is: {}'.format(extension, result))


def run_executors(list_of_file_names):
    """Function which returns random size for file names from a list."""
    for i in range(number_of_processes):
        process = Process(target=choose_handlers, args=(list_of_file_names,))
        process.start()
        process.join()
        print('------------------------Processing completed for {}-------------------------'.format(process.name))


# Example of use
list_of_files = generate_file_names_list()
run_executors(list_of_files)
