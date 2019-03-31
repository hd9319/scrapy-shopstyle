# scrapy-shopstyle
Leverages the power of Scrapy to build an ETL Pipeline.

## Prerequisites
* Requires the Scrapy library

## Installing
1. Create a virtual environment for your project and activate
`virtualenv -p python3 [projectname]`

2. Clone repository
`git clone https://github.com/hd9319/scrapy-shopstyle`

3. Install dependencies using requirements.txt files
`pip install -r requirements.txt`

## How to Use
1. Alter settings.py file for specific configurations (file output, number of concurrent requests, etc.)
2. Run spider via scrapy commands (spider name is defined within file)
`scrapy runspider [spider_name]`
