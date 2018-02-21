#coding:utf-8

import sys
sys.path.insert(0, '/home/esokur/RusDict/')
sys.path.insert(0, '/home/esokur/RusDict/user_interface/')

from app import app as application

if __name__=="__main__":
    application.run()
