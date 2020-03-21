import pwd, os, json, configparser

config = configparser.ConfigParser()
config.read('config.conf')

## set user for owncloud
uid = pwd.getpwnam(config.get('default','webserver_user'))[2] 
os.setuid(uid)

## declare default variable
owncloud = config.get('default','owncloud')
occ = os.path.join(owncloud,'occ')

output = os.popen('php %s %s' % (occ, 'user:list --output=json --attributes=uid')).read()

class User(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

user = User(output)

## remove user from cleanup list
user.__dict__.pop('freakie', None)

for att in user.__dict__.keys():
     os.popen('php %s %s %s' % (occ, 'user:delete', att)
#    print(att)

