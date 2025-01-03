import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

authToken = os.getenv('API_TOKEN')
myCountrycode = ''

class CO2Signal:

    def __init__(self, authToken, countryCode):
        self.authToken = authToken
        self.countryCode = countryCode

    def requestC02Signal(self):
            url = 'http://api.co2signal.com/v1/latest?countryCode=' + self.countryCode
            headers = {'auth-token': self.authToken}
            self.resDict = requests.get(url, params=headers).json()
            