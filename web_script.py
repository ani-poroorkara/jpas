import imp
import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters
import datetime
import csv

from config import jobList

# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)

# Scraper properties
scraper = LinkedinScraper(
    chrome_executable_path="chromedriver_win32/chromedriver.exe",
    chrome_options=None,  
    headless=True, 
    max_workers=1, 
    slow_mo=5,  
)

# Creating base text file
x = datetime.datetime.now()
x = str(x).replace(" ", "_")
x = str(x).replace("-", "")
x = str(x).replace(":", "")
x = str(x).replace(".", "")
f = open("data/data_"+x+".csv", "a", encoding="utf-8")
writer = csv.writer(f)


def on_data(data: EventData):
    row = [str(data.title), str(data.company), str(data.date), str(data.link), str(data.description)]
    writer.writerow(row)
    # print('[ON_DATA]', data.title, data.company, data.date, data.link, len(data.description))

def on_error(error):
    print('[ON_ERROR]', error)

def on_end():
    print('[ON_END]')

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

c = 0
while ( c < len(jobList)):
    queries = [
        Query(
            query=jobList[c],
            options=QueryOptions(
                locations=['Canada'],
                optimize=True,
                limit=150,
                filters=QueryFilters(  # Filter by companies
                    relevance=RelevanceFilters.RECENT,
                    time=TimeFilters.MONTH,
                    type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                    experience=None,                
                )
            )
        ),
    ]
    scraper.run(queries)
    c += 1