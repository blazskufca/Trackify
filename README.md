# Trackify

## Yet another price tracking web app powered by Django.

Input a link, get a daily prices chart! **You can also register to add items to your tracking collection!**

Focused mostly on Slovenian retailers, although it does also accept amazon.de.

**Supports: www.amazon.de, www.bigbang.si, www.enaa.com and www.funtech.si**

## Run a instance with docker
To run with docker:

1.) Clone the repo
```
git clone https://github.com/blazskufca/Trackify.git
cd Trackify
```
2.) Create a .env file with the following keys
```
KEY=YOUR_SECRET_KEY
DEBUG=0 or 1 [0 is debug = False, 1 is debug = True]
DB_HOST=db *leave as is, if changed change also docker-compose.yml
DB_PORT=5432 *Can be left as is
HOST=localhost *Can be left as is
POSTGRES_USER=YOUR_POSTGRE_USERNAME
POSTGRES_PASSWORD=YOUR_POSTGRE_PASSWORD
POSTGRES_DB=YOUR_POSTGRE_DATABASE_NAME
```

3.) `docker-compose up -d`


4.) Make database migrations

`docker-compose exec web python manage.py migrate --noinput`

5.) Create a superuser account
`docker-compose exec -it web python manage.py createsuperuser`

**An instance should be running on localhost:80**

## TODO

- **Clean up the codebase** (in the current state it's a bit of a mess, tons of potential for optimization)
- Add more supported retailers
- Add an API
- More things (?)

## Tech Stack

- Python
- Django
- APscheduler
- Requests
- BeautifulSoup
- Bootstrap
- Chart.js

## Screenshots

Home page:
![Home page](https://i.ibb.co/PGkhgvn/image.png|width=50)

Detailed view:
![Detailed view](https://i.ibb.co/6ZQBj2r/image.png "Detailed view")

Personal profile
![Personal profile](https://i.ibb.co/dJddg03/image.png "Personal profile")
git 
