import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class readConfigfile():
    @staticmethod
    def getApplication(self):
        URL=config.read('common info','base_url')
        return URL

    @staticmethod
    def getusername(self):
        username = config.read('common info', 'username')
        return username

    @staticmethod
    def getpassword(self):
        password = config.read('common info', 'password')
        return password
