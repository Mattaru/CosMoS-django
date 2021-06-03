from dotenv import load_dotenv


load_dotenv()


bind = '127.0.0.1:8000'

workers = 3

user = os.getenv('OS_USERNAME')

timeout = 120
