# VOS Movies Scraper    

Scraper component for the VOS Movies API

    docker build -t ruben/vosmovies-crawler .
    docker run -it -p 5432:5432 ruben/vosmovies-crawler [command for specific crawler you need]

for instance: 

    docker run -it -p 5432:5432 ruben/vosmovies-crawler scrapy crawl phenomena


