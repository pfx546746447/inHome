# _*_ coding: utf-8 _*_

import csv


class FileOperator(object):
    def __init__(self, filename, type):
        self.filename = filename
        self.type = type

    def csvR(self):
        return [i for i in csv.reader(open(self.filename, 'r'))]

    def csvW(self):
        return csv.writer(open(self.filename, 'wb'))

    def txtR(self):
        return [i for i in open(self.filename, 'r')]

    def txtW(self):
        return open(self.filename, 'wb')

def start(file,type):
    fo = FileOperator(filename=file,type=type)
    if type == 'cr':
        return fo.csvR()
    elif type == 'cw':
        return fo.csvW()
    elif type == 'tr':
        return fo.txtR()
    elif type == 'tw':
        return fo.txtW()
