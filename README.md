# Trackify

## Yet another price tracking web app powered by Django.

Input a link, get a daily prices chart! **You can also register to add items to your tracking collection!**

Focused mostly on Slovenian retailers, although it does also accept amazon.de.

**Supports: www.amazon.de, www.bigbang.si, www.enaa.com and www.funtech.si**

## Demo

**An instance is running at: http://trackify-env-1.eba-9g8g5ghp.eu-central-1.elasticbeanstalk.com/**

## Run locally
**Local image is meant for running locally - Runs with "debug = True" and is served with Django's development server!**

To run locally with docker:

```
git clone https://github.com/blazskufca/Trackify.git
git switch local
docker-compose up -d
```
If you need a superuser account (for localhost:8000/admin/)

`docker-compose exec -it trackify python manage.py createsuperuser`

And follow the prompts in the terminal. You should have a superuser account by the end of it, with which you can login into the admin panel.

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
