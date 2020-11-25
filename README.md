# REST test server
This is a simple test REST server for testing API requests.

### Dependencies:
It is requires Python 3.8 and aiohttp 3.7<br>
You can use it with pipenv `pipenv install` or manually with pip.

### Server start: 
You can use param **-p** to configure the port<br>
`pipenv run python simple_rest_server.py -p 8000`<br>
or example without pipenv 
`python3 simple_rest_server.py`

### Testing API requests:
Use URL http://localhost:8080/get-response?code=404&time=2
* code - http code for responce
* time - number of seconds to delay response