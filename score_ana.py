#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andrew'

import codecs


class Student(object):
    def __init__(self, head, value):
        for i in range(len(head)):
            self.__dict__[head[i]] = value[i]

    def __repr__(self):
        print 'here-------'
        for key in self.__dict__.keys():
            print key, self.__dict__[key]


def load_score_file():
    score_file = codecs.open('./score.txt', 'r', 'utf-16')
    first_line = score_file.readline()
    print "this is first line", first_line
    for line in score_file.readlines():
        print line
        stu = Student(first_line.split(), line.split())
        print stu
        # words = line.split()
        # for word in words:
        #     print word

if __name__ == "__main__":
    print 'in main'
    load_score_file()
