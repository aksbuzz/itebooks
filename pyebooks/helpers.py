import requests
import sys


def get_json(end_point):
    '''
    Make request to http://api.erail.in/
    '''

    try:
        r = requests.get(end_point)

    except requests.exceptions.RequestException as e:

        print(e)
        sys.exit(1)

    return r.json()
