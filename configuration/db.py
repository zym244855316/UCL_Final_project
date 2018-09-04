import os
import configparser
import pymysql.cursors
import datetime as dt

class TwitterDatabase():
    def __init__(self):
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config = configparser.RawConfigParser()
        configFilePath = '{}/configuration/db.properties'.format(root_path)
        config.read(configFilePath)
        profile = 'AWS'
        self.host = config.get(profile, 'host')
        self.user = config.get(profile, 'user')
        self.password = config.get(profile, 'password')
        self.db = config.get(profile, 'db')
        self.connection = None
        
    # SQL Layer functions
    def connect(self):
        self.connection = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            db = self.db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            max_allowed_packet=1073741824 # AWS MySQL max allowed packet upper limit
        )
        
    def close(self):
        self.connection.close()
        
    def reconnect(self):
        try:
            self.close()
            self.connect()
            print('Reconnected!')
        except:
            print('Failed to reconnect!')
        
    def query(self, sql, parameters = ()):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, parameters)
                result = cursor.fetchall()
            return result
        except Exception as e:
            self.__print_error(e, sql, parameters)
            self.reconnect()
        
    def execute(self, sql, parameters = ()):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, parameters)
            self.connection.commit()
        except Exception as e:
            self.__print_error(e, sql, parameters)
            self.reconnect()
    
    # Application layer functions
    # Note this is using INSERT IGNORE, hence it will not update user information when it has duplicated ids
    def insertTwitterUser(self, userJsonObject):
        fields = ['id', 'name', 'screen_name', 'location', 'url', 
                  'description', 'protected', 'verified', 'followers_count', 'friends_count', 
                  'listed_count', 'favourites_count', 'statuses_count', 'created_at', 'geo_enabled', 
                  'lang', 'contributors_enabled']
        sql = "INSERT IGNORE INTO `user` ({}) VALUES ({})".format(
            ', '.join('`{}`'.format(x) for x in fields),
            ', '.join('%s'.format(x) for x in fields)
        )
        parameters = [userJsonObject[x] for x in fields]
        parameters[13] =  dt.datetime.strptime(parameters[13], '%a %b %d %H:%M:%S %z %Y')
        self.execute(sql, tuple(parameters))
        
    def updateTwitterUserFollowers(self, user_id, id_list):
        sql = "UPDATE `user` SET `followers_json` = %s WHERE `id` = %s"
        parameters = (str(id_list), user_id)
        self.execute(sql, parameters)

    def updateTwitterUserFriends(self, user_id, id_list):
        sql = "UPDATE `user` SET `friends_json` = %s WHERE `id` = %s"
        parameters = (str(id_list), user_id)
        self.execute(sql, parameters)

    def queryTwitterUsersIdsFound(self, id_list):
        result = []
        size = 1000
        composite_list = [id_list[i:i+size] for i  in range(0, len(id_list), size)]
        format_string = {}
        for id_sublist in composite_list:
            numberOfParameters = len(id_sublist)
            if numberOfParameters not in format_string.keys():
                format_string[numberOfParameters] = ','.join(['%s'] * numberOfParameters)
            sql = "SELECT `id` FROM `user` WHERE `id` IN ({})".format(format_string[numberOfParameters])
            parameters = tuple(id_sublist)
            queryResult = self.query(sql, parameters)
            if queryResult is not None:
                result.extend(queryResult)
        return result
        
    def queryUnorderedTwitterUsers(self, id_list):
        result = []
        size = 1000
        composite_list = [id_list[i:i+size] for i  in range(0, len(id_list), size)]
        for id_sublist in composite_list:
            numberOfParameters = len(id_sublist)
            format_strings = ','.join(['%s'] * numberOfParameters)
            sql = "SELECT * FROM `user` WHERE `id` IN ({})".format(format_strings)
            parameters = tuple(id_sublist)
            result.extend(self.query(sql, parameters))
        return result
    
    def queryOrderedTwitterUsers(self, id_list):
        result = []
        size = 1000
        composite_list = [id_list[i:i+size] for i  in range(0, len(id_list), size)]
        for id_sublist in composite_list:
            numberOfParameters = len(id_sublist)
            format_strings = ','.join(['%s'] * numberOfParameters)
            sql = "SELECT * FROM `user` WHERE `id` IN ({}) ORDER BY FIELD(`id`, {})".format(
                format_strings,
                format_strings
            )
            parameters = tuple(id_sublist * 2)
            result.extend(self.query(sql, parameters))
        return result
        
    # Helpfer functions
    def __print_single_parameter(self, parameter):
        parameter_string = str(parameter)
        if len(parameter_string) < 30:
            return parameter_string
        else:
            return '{}...{}'.format(parameter_string[:10], parameter_string[-10:])
    
    def __print_error(self, error, sql, parameter_tuple):
        shorten_parameters = [self.__print_single_parameter(x) for x in parameter_tuple]
        error_message = 'Exception: {}, SQL: {}, parameters: {}'.format(
            error, sql, str(shorten_parameters))
        print(error_message)