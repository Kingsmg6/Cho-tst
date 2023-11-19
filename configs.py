from os import path, getenv

class Config:
    API_ID = int(getenv('API_ID','23701401'))
    API_HASH = getenv('API_HASH','05c47cb068824a17192400d0d5ffe744')
    BOT_TOKEN = getenv('BOT_TOKEN','6784022172:AAH7zqqxo2G4boiqhjZ1XPrI-0cdAxoM1dk')

config = Config()
