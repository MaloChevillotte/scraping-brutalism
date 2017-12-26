# -*- coding: utf-8 -*-
import scrapy
import os
import time
import re

list_ids = []
with open('/Users/malochevillotte/Desktop/brutalism/list_ids.txt', 'rb') as f:
    for item in f:
        list_ids.append(item.strip())

class JobsSpider(scrapy.Spider):
    name = 'get_jsons'
    allowed_domains = ['sosbrutalism.org']
    start_urls = []
    for idd in list_ids:
        start_urls.append("http://www.sosbrutalism.org/sixcms/detail.php?id=" + idd + "&json=1")
#        print(start_urls)

    def parse(self, response):
        page = response.url.split("/")[-2]
        table = []
        filename = 'get_jsons-%s.json' % re.findall('id=\s*([^"\n\r]*&)', response.url)
        with open(os.path.join('/Users/malochevillotte/Desktop/brutalism/json_files/', filename), 'wb') as f:
            f.write(response.body)

        # for element in list_ids:
        #     filename = 'get_jsons-%s.json' % element
        #     with open(os.path.join('/Users/malochevillotte/Desktop/brutalism/json_files/', filename), 'wb') as f:
        #         f.write(response.body)
        #     time.sleep(0.1)
