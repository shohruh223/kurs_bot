from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')
API_KEY = env('API_KEY')