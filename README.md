# NasaApiDjango

# Getting Started
1. Clone the repo
*Prerequisites : git
```sh
git clone https://github.com/alexgoyr/NasaApiDjango
```

OR

Download the zip file : https://github.com/alexgoyr/NasaApiDjango/archive/refs/heads/main.zip

2. 
*Prerequisites : Python3 and pip installed
```sh
pip install -r requirements.txt
python3 manage.py runserver
```

OR

*Prerequisites : Docker installed
```sh
docker build -t nasa_api_django .
docker run -p 8000:8000 nasa_api_django
```

# Usage
Once started, the project is accessible with the address : http://localhost:8000