from dotenv import load_dotenv


load_dotenv()


bind = '127.0.0.1:8000'

workers = 2

user = os.getenv('OS_USERNAME')

timeout = 120
