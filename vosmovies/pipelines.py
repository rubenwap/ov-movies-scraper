# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
load_dotenv()


pg_config = {"host": "docker.for.mac.host.internal",
             "database": "ruben", "user": "ruben", "password": ""}
# pg_config = {"host": os.getenv("HOST"),
# 			"database": os.getenv("DB"),
# 			"user": os.getenv("USERNAME"),
# 			"password": os.getenv("PASSWORD"),
#              "sslmode": 'require'}

conn = psycopg2.connect(**pg_config)


class VosmoviesPipeline(object):
	def process_item(self, item, spider):

		cinema = item["cinema"]
		date = item["date"]
		details = item["details"]
		hour = item["hour"]
		title = item["title"]
		timestamp = item["datetime"]

		print(item["cinema"])
		print(item)

		sql_insert = """
			INSERT INTO public.movies(
	cinema, movie_date, details, movie_time, title, datetime)
	VALUES (%(cinema)s,
			%(date)s,
			%(details)s,
			%(hour)s,
			%(title)s, 
			%(datetime)s
			);
			"""

		with conn.cursor(cursor_factory=RealDictCursor) as cursor:
			cursor.execute(sql_insert, item)
			conn.commit()
		return item
