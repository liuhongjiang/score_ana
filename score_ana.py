#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andrew'

import codecs


class Student(object):
    def __init__(self, head, value):
        for i in range(len(head)):
            self.__dict__[head[i]] = value[i]

    def __unicode__(self):
        # print 'here-------'
        return_name = ""
        for key in self.__dict__.keys():
            return_name += key + ':' + self.__dict__[key] + ', '
        return return_name

    def __str__(self):
        return self.__unicode__()


def load_score_file():
    score_file = codecs.open('./score.txt', 'r', 'utf-16')
    first_line = score_file.readline()
    print "this is first line", first_line
    for line in score_file.readlines():
        print line
        stu = Student(first_line.split(), line.split())
        print unicode(stu)
        # words = line.split()
        # for word in words:
        #     print word

if __name__ == "__main__":
    print 'in main'
    load_score_file()
