from flask import Flask
## Using __name__ calls Flask as method
app = Flask(__name__)

@app.route('/')
def index():
	return 'Server works'

# To activate this project's virtualenv, run pipenv shell. 
# Alternatively, run a command inside the virtualenv with pipenv run.