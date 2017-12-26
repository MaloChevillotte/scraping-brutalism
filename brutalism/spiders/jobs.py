# -*- coding: utf-8 -*-
import scrapy
import os


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['sosbrutalism.org']
    start_urls = ['http://www.sosbrutalism.org/sixcms/detail.php?id=15891515&json=1',
    'http://www.sosbrutalism.org/sixcms/detail.php?id=16339125&json=1']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'jobs-%s.json' % page
        with open(os.path.join('/Users/malochevillotte/Desktop/brutalism/json_files/', filename), 'wb') as f:
            f.write(response.body)
