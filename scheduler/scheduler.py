from tracker.tracker_logic import (
    BigBangTracker,
    AmazonDeTracker,
    EnaATracker,
    FuntechTracker,
)
from tracker.models import TrackedProducts
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    for item in TrackedProducts.objects.all():
        if item.link[:23] == "https://www.bigbang.si/":
            try:
                BigBangTracker().update(item.link)
            except:
                pass
        elif item.link[:22] == "https://www.amazon.de/":
            try:
                AmazonDeTracker().update(item.link)
            except:
                pass
        elif item.link[:21] == "https://www.enaa.com/":
            try:
                EnaATracker().update(item.link)
            except:
                pass
        elif item.link[:23] == "https://www.funtech.si/":
            try:
                FuntechTracker().update(item.link)
            except:
                pass


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", days=1)
    scheduler.start()
