import pwd, os, json, configparser

## grep default config from file
config = configparser.ConfigParser()
config.read('config.conf')

## set user for owncloud
uid = pwd.getpwnam(config.get('default','webserver_user'))[2] 
os.setuid(uid)

## declare default variable
owncloud = config.get('default','owncloud')
occ = os.path.join(owncloud,'occ')
del_status = int(config.get('default', 'delete'))

output = os.popen('php %s %s' % (occ, 'user:list --output=json --attributes=uid')).read()

class User(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

user = User(output)

## remove user from cleanup list
user.__dict__.pop(config.get('default', 'protected_user'), None)

## Operation function
#  This function is to decide whether to list user or delete all user
## 
def del_operation(status, attribute):
    if status != 0:
        operation = os.popen('php %s %s %s' % (occ, 'user:delete', attribute)).read()
    else:
        operation = attribute
    
    return operation

for att in user.__dict__.keys():
    print(del_operation(del_status, att))
