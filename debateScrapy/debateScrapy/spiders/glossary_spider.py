import scrapy

class GlossarySpider(scrapy.Spider):
	name="glossary"

	def start_requests(self):

	urls=[http://idebate.org/glossary]

	for url in urls:
		yield scrapy.Request(url=url, callback=self.parse)

	def prarse(self, response):
		terms,definitions = response.url.xpath('//dl/dt/a/@id').extract(), response.ur$
                glossary = {k:v for k, v in zip(terms,definitions)}

		filename = 'glossary.html'
	        with open(filename, 'wb') as f:
	            f.write(response.body)
		self.log('Saved file ' % filename)
 
	
#terms,definitions = response.url.xpath('//dl/dt/a/@id').extract(), response.url.xpath('//dl/dd/p/text()').extract()
#glossary = {k:v for k, v in zip(terms,definitions)}
