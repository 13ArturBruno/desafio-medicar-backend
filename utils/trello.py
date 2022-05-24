import os

import requests

_cardsBaseUrl = 'https://api.trello.com/1/cards'
_apiKey = os.getenv('TRELLO_API_KEY')
_apiToken = os.getenv('TRELLO_API_TOKEN')
_idList = os.getenv('TRELLO_LIST_ID')


def create_card(data):
    try:
        url = '{}?idList={}&key={}&token={}&name={}&due={}'.format(
            _cardsBaseUrl,
            _idList,
            _apiKey,
            _apiToken,
            data['medico'] + ' / ' + str(data['horario']),
            data['dia']
        )

        response = requests.request("POST", url, data={})
        data = response.json()
        return data['id']

    except Exception as e:
        print(e)
        pass


def delete_card(trello_card_id):
    try:
        url = '{}/{}?key={}&token={}'.format(
            _cardsBaseUrl,
            trello_card_id,
            _apiKey,
            _apiToken,
        )

        requests.request("DELETE", url)

    except Exception as e:
        print(e)
        pass
