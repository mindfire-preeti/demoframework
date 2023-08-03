# this file will read the common data from config.ini file

import configparser


config = configparser.RawConfigParser()
config.read('./Configurations/config.ini')

class readConfig:
    @staticmethod # created static method so that we can method using classname and without creation its Obj
    def getApplicationURL():
        url = config.get('common info', 'baseURl')
        return url

    @staticmethod  # created static method so that we can method using classname and without creation its Obj
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod  # created static method so that we can method using classname and without creation its Obj
    def getUserPassword():
        password = config.get('common info', 'password' )
        return password