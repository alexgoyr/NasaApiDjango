# NasaApiDjango

# How to launch ?
(requirement : Python3 and pip installed)
pip install -r requirements.txt
python3 manage.py runserver

OR

(reqirement : Docker installed)
docker build -t nasa_api_django .
docker run -p 8000:8000 nasa_api_django