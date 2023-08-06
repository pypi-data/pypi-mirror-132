# pysafie
Safie API client library for Python

# Requirement
A subscription is required to use the Safie API. Please refer to this link for details.<br>
https://developers.safie.link/

# Installation
```
pip install pysafie
```

# Usage

By receiving authentication code, you can use it as follows.

```python
import pysafie

client_id = 'hogehoge'
client_secret = 'hogehoge'
redirect_uri = 'https://hoge.com/'

authentication_code = 'hogehoge' # Need to get it from the redirected URL

safie = pysafie.Safie(client_id, client_secret, redirect_uri)
safie.get_access_token(authentication_code)

res = safie.get_device_list() # Returns requests' response object
print(res.json())
```

If you have already stored token information, you can set it when you create an instance.

```python
import pysafie

client_id = 'hogehoge'
client_secret = 'hogehoge'
redirect_uri = 'https://hoge.com/'

access_token = 'hogehoge'
refresh_token = 'hogehoge'
expires_at = 1624247730 # Set the token expiration in unix time

safie = pysafie.Safie(client_id, client_secret, redirect_uri, 
                      access_token, refresh_token, expires_at)

res = safie.get_device_list() # Returns requests' response object
print(res.json())
```

# Note
For now, this library only supports auth, devices, and media_files APIs.


# Author
* kndt84
* Future Standard Co., Ltd.

# License
pysafie is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
