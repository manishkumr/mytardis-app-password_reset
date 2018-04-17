# mytardis-app-password_reset
Mytardis app to add password reset functionality for local account users

This app should be installed in Mytradis environment by running:

```
pip install -e git://github.com/manishkumr/mytardis-app-password_reset#egg=password_reset
```
Add this app to tardis/settings.py:

```
INSTALLED_APPS += ('password_reset',)
```


Restart MyTardis.
