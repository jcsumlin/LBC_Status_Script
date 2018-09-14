import LocalBitcoin
import os
# import configparser
import time

# config = configparser.ConfigParser()
# config.read('auth.ini')
hmac_auth_key = os.environ['hmac_auth_key']
# hmac_auth_key = str(config.get('auth', 'hmac_auth_key'))  # REQUIRED
hmac_auth_secret = os.environ['hmac_auth_secret']
# hmac_auth_secret = str(config.get('auth', 'hmac_auth_secret'))  # REQUIRED

lc = LocalBitcoin.LocalBitcoin(hmac_auth_key, hmac_auth_secret, False)
min_counter = 13

try:
    myself = lc.getMyself()
    print("\r\nHello, " + myself['username'] + ".\r\n")
except Exception as e:
    print(
        "Error authenticating API KEY + API SECRET, or error parsing data. Please try again.\n\n")
    print(e)
    exit()

while True:
    min_counter -= 1
    if (min_counter == 0):
        print('Refreshing online status for ' + myself['username'] + '.')
        lc.getMyself()
        min_counter = 13
    else:
        print(str(min_counter) + ' minutes remaining until refresh.')
    time.sleep(60)