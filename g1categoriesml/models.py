from django.db import models
#from G1Crawler.spiders.G1Spider import G1spiderSpider
#from django.http import HttpResponse
#import os
# Create your models here.

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    #os.system('rm noticias.json')	
    #G1spiderSpider.parse
    #os.system('scrapy runspider G1Crawler/spiders/G1Spider.py --nolog -o noticias.json')
    #print('foi')
    #pass
    #G1Spider.parse(HttpResponse)

