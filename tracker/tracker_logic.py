import requests
import datetime
from bs4 import BeautifulSoup
from babel.numbers import parse_decimal
from . import models
import json
from datetime import date
from django.utils.timezone import make_aware
import cloudscraper


class BigBangTracker:
    def scrape(self, url):
        response = requests.get(url)
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            price = parse_decimal(
                soup.select_one(".cd-current-price")
                .contents[0]
                .getText()
                .strip()
                .replace(" €", ""),
                locale="sl_SI",
            )
            title = soup.select_one(".cd-title").getText().strip()
            description = soup.select_one(".cms-content").getText().strip()
            JSON = {str(date.today()): price}
            models.TrackedProducts(
                name=title,
                link=response.url,
                price=price,
                date=date.today(),
                priceHistory=json.dumps(JSON, default=str),
                description=description,
            ).save()
        except:
            pass

    def update(self, url):
        response = requests.get(url)
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            price = parse_decimal(
                soup.select_one(".cd-current-price")
                .contents[0]
                .getText()
                .strip()
                .replace(" €", ""),
                locale="sl_SI",
            )
            instance = models.TrackedProducts.objects.get(link=url)
            tempDict = json.loads(instance.priceHistory)
            tempDict[str(date.today())] = price
            if price < instance.price:
                instance.price = price
            instance.priceHistory = json.dumps(tempDict, default=str)
            instance.modifiedDate = make_aware(datetime.datetime.now())
            instance.save()
        except:
            pass


class AmazonDeTracker:
    def scrape(self, url):
        scraper = cloudscraper.create_scraper()
        response = scraper.get(
            url,
            headers={
                "authority": "www.amazon.de",
                "pragma": "no-cache",
                "cache-control": "no-cache",
                "dnt": "1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-dest": "document",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            },
        )
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.content, "lxml")
            temp = (
                soup.select_one(".a-offscreen")
                .getText()
                .replace("€", "")
                .replace(",", "")
            )
            price = float(temp)
            title = soup.select_one(".product-title-word-break").getText().strip()
            JSON = {str(date.today()): price}
            models.TrackedProducts(
                name=title,
                link=response.url,
                price=price,
                date=date.today(),
                priceHistory=json.dumps(JSON, default=str),
            ).save()
        except:
            pass

    def update(self, url):
        scraper = cloudscraper.create_scraper()
        response = scraper.get(
            url,
            headers={
                "authority": "www.amazon.de",
                "pragma": "no-cache",
                "cache-control": "no-cache",
                "dnt": "1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-dest": "document",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            },
        )
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.content, "lxml")
            temp = (
                soup.select_one(".a-offscreen")
                .getText()
                .replace("€", "")
                .replace(",", "")
            )
            price = float(temp)
            instance = models.TrackedProducts.objects.get(link=url)
            tempDict = json.loads(instance.priceHistory)
            tempDict[str(date.today())] = price
            if price < instance.price:
                instance.price = price
            instance.priceHistory = json.dumps(tempDict, default=str)
            instance.modifiedDate = make_aware(datetime.datetime.now())
            instance.save()
        except:
            pass


class EnaATracker:
    def scrape(self, url):
        response = requests.get(url)
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            price = parse_decimal(
                soup.select_one(".single-product-price")
                .getText()
                .strip()
                .replace(" €", ""),
                locale="sl_SI",
            )
            title = soup.select_one(".section-title").getText().strip()
            description = (
                soup.select_one(".single-product-description")
                .getText()
                .strip()
                .replace("   Celoten opis", "")
            )
            JSON = {str(date.today()): price}
            models.TrackedProducts(
                name=title,
                link=response.url,
                price=price,
                date=date.today(),
                priceHistory=json.dumps(JSON, default=str),
                description=description,
            ).save()
        except:
            pass

    def update(self, url):
        response = requests.get(url)
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            price = parse_decimal(
                soup.select_one(".single-product-price")
                .getText()
                .strip()
                .replace(" €", ""),
                locale="sl_SI",
            )
            instance = models.TrackedProducts.objects.get(link=url)
            tempDict = json.loads(instance.priceHistory)
            tempDict[str(date.today())] = price
            if price < instance.price:
                instance.price = price
            instance.priceHistory = json.dumps(tempDict, default=str)
            instance.modifiedDate = make_aware(datetime.datetime.now())
            instance.save()
        except:
            pass


class FuntechTracker:
    def scrape(self, url):
        response = requests.get(url)
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            price = parse_decimal(
                soup.select_one(".nasa_cena")
                .getText()
                .strip()
                .replace("Naša cena:  ", "")
                .replace(" €", ""),
                locale="sl_SI",
            )
            title = soup.select_one(".naslov_ogled_artikla").getText().strip()
            description = soup.select_one(".opis").getText().strip()
            JSON = {str(date.today()): price}
            models.TrackedProducts(
                name=title,
                link=response.url,
                price=price,
                date=date.today(),
                priceHistory=json.dumps(JSON, default=str),
                description=description,
            ).save()
        except:
            pass

    def update(self, url):
        response = requests.get(url)
        response.raise_for_status()
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            price = parse_decimal(
                soup.select_one(".nasa_cena")
                .getText()
                .strip()
                .replace("Naša cena:  ", "")
                .replace(" €", ""),
                locale="sl_SI",
            )
            instance = models.TrackedProducts.objects.get(link=url)
            tempDict = json.loads(instance.priceHistory)
            tempDict[str(date.today())] = price
            if price < instance.price:
                instance.price = price
            instance.priceHistory = json.dumps(tempDict, default=str)
            instance.modifiedDate = make_aware(datetime.datetime.now())
            instance.save()
        except:
            pass
