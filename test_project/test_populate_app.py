import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_project.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT
import random
from test_app.models import table_topic, table_webpage, table_AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','MarketPlace',"News",'Games']

def add_topic():
    t = table_topic.objects.get_or_create(col_topic1=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create the fake data for the entry of table_webpage
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new table_webpage entry
        wp = table_webpage.objects.get_or_create(col_webpage1=top,col_webpage2=fake_name,col_webpage3=fake_url)[0]

        # create a fake access record
        acc_rec = table_AccessRecord.objects.get_or_create(col_AccessRecord1=wp, col_AccessRecord2=fake_date)

if __name__=='__main__':
    print('population script!')
    populate(20)
    print('populatating complete!')