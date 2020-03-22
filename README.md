# Owncloud user cleanup

## Feature
* schedule to clean user and storage on certain period of time
* adhoc bulk delete user
 
## Require
```bash
 apt-get install python3-venv

```

## Installation Guide
 ```bash
 git clone http://gitlab.command-line.io/owncloud/user-cleanup.git /opt/owncloud/user-cleanup
 cd /opt/owncloud/user-cleanup/
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt

 ```

Default installation will only display all user available accept protected user delete = 0
 + make sure to set protected_user at config.conf
 + update all related config at config.conf

To start delete user and file
 + update delete = 1 at config.conf

 Run script by trigger
 ```bash
 python clean.py
 ```


