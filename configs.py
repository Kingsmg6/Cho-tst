from os import path, getenv

class Config:
    API_ID = int(getenv('API_ID','21019111'))
    API_HASH = getenv('API_HASH','1c1a6ee469f6acd14661c2ba245219e5')
    BOT_TOKEN = getenv('BOT_TOKEN','5619874453:AAHgQ1FnHA8q3Q5j_lLfFHkKKabDyUEM2Dg')

config = Config()
