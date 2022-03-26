import logging
import os
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters

# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)


if(os.path.isfile("data/data.csv")):
    f = open("data/data.csv", "a")
    print("File exists")
else:
    f = open("data/data.csv", "a")
    f.write("job_id"+","+"title+ "+","+"company"+ "," +"location"+","
    +"date" + "," + "link" + ", " + "Length description"+","
    +"employment_type"+","+"seniority_level"+","+"place"+","+"job_function"+"\n")
def on_data(data: EventData):

    f.write(str(data.job_id)+","+str(data.title).replace(",","") + "," + str(data.company).replace(",","") + "," +str(data.location)+","
    +str(data.date) + "," + str(data.link) + ", " + str(len(data.description))+","
    +str(data.employment_type)+","+str(data.seniority_level)+","+str(data.place).replace(",","")+","+str(data.job_function).replace(",","")+"\n")
    print('[ON_DATA]', data.title, data.company, data.date, data.link, len(data.description))


def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path="chromedriver_m1/chromedriver", # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver)
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=2,  # Slow down the scraper to avoid 'Too many requests (429)' errors
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        #query='Software Engineer',
        options=QueryOptions(
            locations=['Canada'],
            optimize=True,
            limit=10000,
            filters=QueryFilters(  # Filter by companies
                #relevance=RelevanceFilters.RECENT,
                #time=TimeFilters.MONTH,
                #type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                #experience=None,
            )
        )
    ),
]

scraper.run(queries)
f.close()