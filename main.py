import LocalBitcoin
import os
import time

hmac_auth_key = os.environ['hmac_auth_key']
# hmac_auth_key = str(config.get('auth', 'hmac_auth_key'))  # REQUIRED
hmac_auth_secret = os.environ['hmac_auth_secret']
# hmac_auth_secret = str(config.get('auth', 'hmac_auth_secret'))  # REQUIRED

lc = LocalBitcoin.LocalBitcoin(hmac_auth_key, hmac_auth_secret, False)
min_counter = 13

try:
    myself = lc.getMyself()
    print("\r\nHello, " + myself['data']['username'] + ".\r\n")
except Exception:
    print(
        "Error authenticating API KEY + API SECRET, or error parsing data. Please try again.")
    exit()

while True:
    min_counter -= 1
    if (min_counter == 0):
        print('Refreshing online status for ' + myself['data']['username'] + '.')
        lc.getMyself()
        min_counter = 13
    else:
        print(str(min_counter) + ' minutes remaining until refresh.')
    time.sleep(60)