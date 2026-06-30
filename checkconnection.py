import requests

def checkinternet():
    connected = True
    try:
        requests.get('https://www.google.com', timeout=5)
    except Exception:
        connected = False
    if not connected:
        print("    |-$ It seems that you are not connected to Internet.")
        print('    |-$ bomberthon will stop now...')
        exit()
    
