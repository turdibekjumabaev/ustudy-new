import os
from src import create_app
from dotenv import load_dotenv

load_dotenv()

env = os.getenv('FLASK_ENV')
app = create_app(env)

if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port)
