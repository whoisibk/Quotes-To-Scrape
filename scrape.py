import requests
import lxml.html

html = requests.get("https://store.steampowered.com/explore/new/")
object_ = lxml.html.fromstring(html.content)

new_releases = object_.xpath('//div[@id="tab_newreleases_content"]')[0]

names = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

tags = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tag_list = [tag.text_content().split(", ") for tag in tags]

platformz = new_releases.xpath('.//div[@class="tab_item_details"]')
platforms = [] 

for pltfm in platformz:
    platform_span = pltfm.xpath('.//span[contains(@class, "platform_img")]')
    platform = [platform.get("class").split(' ')[-1] for platform in platform_span]
    platforms.append(platform)

#creating a list of dictionaries
list_of_games = []
for game in zip(names, prices, platforms, tag_list):
    game_dict = {}
    game_dict["Name"] = game[0]
    game_dict["Price"] = game[1]
    game_dict["Platforms"] = game[2]
    game_dict["Tags"] = game[3]
    list_of_games.append(game_dict)

for game in list_of_games:
    print(game)
