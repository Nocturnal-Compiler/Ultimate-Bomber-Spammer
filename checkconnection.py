import requests

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com')
        res = False
    except Exception:
        res = True
    if res:
        print("    |-$ It seems that you are not connected to Internet.")
        print('    |-$ bomberthon will stop now...')
        exit()
    
