import requests
import lxml.html
import csv

quote_webpage = requests.get("https://quotes.toscrape.com/")
quote_webpage.encoding = "utf-8"
quote_object = lxml.html.fromstring(quote_webpage.content)

quote_cap = quote_object.xpath('//div[@class="quote"]')

authors = []
quotes = []
tagz = []
for quote_info in quote_cap:
    quote = quote_info.xpath('.//span[@class="text"]/text()')[0]
    author = quote_info.xpath('.//small[@class="author"]/text()')[0]
    tags = quote_info.xpath('.//div[@class="tag"]')
    tags  = [tag.text_content().rstrip().split(' ') for tag in tags]

    quotes.append(quote)
    authors.append(author)
    tagz.append(tags)




quote_list = []
for quote_scrape in zip(authors, quotes, tagz):
    quote_list.append([quote_scrape[0], quote_scrape[1], quote_scrape[2]])
    
with open("csv_scrape2.csv", "w", encoding="utf-8") as csv_scrape2:
        scrape_writer = csv.DictWriter(csv_scrape2, fieldnames=["Author", "Quote"], quoting=csv.QUOTE_ALL)
        scrape_writer.writeheader()
        for quote_1 in quote_list:
            scrape_writer.writerow({"Author": quote_1[0], "Quote": quote_1[1]})
        
