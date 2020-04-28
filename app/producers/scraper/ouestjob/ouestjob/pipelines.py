# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import persistqueue
import os

q = persistqueue.SQLiteQueue(os.path.join(os.path.dirname(__file__), "../../../../queue"), auto_commit=True)

class OuestjobPipeline(object):
    def process_item(self, item, spider):
        q.put({"id": int(item['id']), "clean_text": item['description']})
        
