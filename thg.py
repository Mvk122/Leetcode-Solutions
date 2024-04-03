def countSignals(frequencies, filterRanges):
    count = 0
    for frequency in frequencies:
        for r in filterRanges:
            if frequency < r[0] or frequency > r[1]:
                break
        else:
            count += 1
    return count

import requests


def getCapitalCity(country):
    # Write your code here
    r = requests.get(f"https://jsonmock.hackerrank.com/api/countries?name={country}")
    data = r.json()
    if data['data']:
        return data['data'][0]['capital']