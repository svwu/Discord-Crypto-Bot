from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

baseUrl = "https://pro-api.coinmarketcap.com/v1/"
CMC_API_KEY = os.environ.get("CMC_API_KEY")

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': os.environ.get("CMC_API_KEY")
}

def informationForCryptoBySymbolName(symbolName):
    session = Session()
    session.headers.update(headers)

    requestPath = 'cryptocurrency/quotes/latest'
    requestUrl = baseUrl + requestPath

    parameters = {
      'convert':'USD',
      'symbol': symbolName
    }

    try:
      response = session.get(requestUrl, params = parameters)
      responseText = json.loads(response.text)
      print(responseText)
      data = responseText['data']
      tokenId = next(iter(data), None)
      return data[tokenId]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      return "Error getting all token information from CoinMarketCap"