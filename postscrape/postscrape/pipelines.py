# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
from itemadapter import ItemAdapter


class PostscrapePipeline:

    def __init__(self):

        client = MongoClient("mongodb+srv://mark:admin.123@test1.ydsr0.mongodb.net/<dbname>?retryWrites=true&w=majority")
        db = client.get_database('projectDB')
        record = db.posts
        #record.count_documents({})

        new_entry = {
            'problem' : '1. problem',
            'solution' : 'this is solution'
        }
        record.insert_one(new_entry)


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        #print("Pipeline :" + item['problem'][0])
        return item
