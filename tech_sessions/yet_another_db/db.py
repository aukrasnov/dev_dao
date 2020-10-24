import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-c", help="name of comand to be done")


def insert(id, val):
    f = open("database", "a+")
    f.write('{}, {}'.format(id, val))
    f.close()


def get(id):
    get_re = re.compile('^[0-9]*, *')


    return payload


def delete(id):


    "$1, #Thombstone" >> database | echo
