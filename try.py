# coding=utf-8
#
import os

for f in os.listdir('./templates'):
    p = open('./templates/' + f, 'r').read()
    p = p.replace('rel="shortcut icon"', 'rel="shortcut icon" type="image/x-icon"')

    fw = open('./templates/' + f, 'w')
    fw.write(p)
    fw.close()