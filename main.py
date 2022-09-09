# Import input instance module.
from class_inputs import Input_mysql_credentials

# Module connection Mysql
from class_mysql import Mysql_connection 



# Catch the host, database, user and password. 
CREDENTIALS = Input_mysql_credentials()
CREDENTIALS.displayInput()


# Connection with MySQL
mysql_auth = {'host': CREDENTIALS.host, 
              'database' : CREDENTIALS.database, 
              'user' : CREDENTIALS.user, 
              'password' : CREDENTIALS.password}


mysqlcn = Mysql_connection(mysql_auth['host'], mysql_auth['database'], mysql_auth['user'], mysql_auth['password'])  # Insert the arguments that the instance need.
mysqlcn.connection_mysql()
