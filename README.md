# CurrencyConverter

Provides a web interface and rest API for calculating currency conversions using http://exchangeratesapi.io/

## Installing

### Using Docker:
```bash
git clone https://github.com/rmountjoy92/CurrencyConverter.git
cd CurrencyConverter
docker build -t CurrencyConverter .
docker run --publish 5000:5000 CurrencyConverter
```

### Development Server:
Clone repository & navigate to it:

```bash
git clone https://github.com/rmountjoy92/CurrencyConverter.git
cd CurrencyConverter
```

Create virtual environment & activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Start the test server:
```bash
python3 run_test_server.py
 ```



Visit the following address in your browser:  
`http://localhost:5000/`

For the Rest API documentation, go to:
`http://localhost:5000/api`

### Stack
- (optionally) Docker
- Flask (Python 3.8)
- HTML5/Jinja2
- Bootstrap CSS
- RestX, SwaggerUI
