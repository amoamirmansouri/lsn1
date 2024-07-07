from config import url

import requests
import json

def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return response.status_code


def archive(filenam, rates):
    with open(f'arc/{filenam}.json', "w") as file:
        for i in rates:
            file.write(json.dumps(i)+':'+str(rates[i])+'\n')

if __name__ == "__main__":
    response = get_rates()
    archive('tody',response)