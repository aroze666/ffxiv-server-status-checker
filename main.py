from bs4 import BeautifulSoup
import urllib.request
import time
server_name = input("Enter name of the server: ")

while True:
    soup = BeautifulSoup(urllib.request.urlopen('https://na.finalfantasyxiv.com/lodestone/worldstatus/').read())
    for li in soup.find_all("li", class_="item-list"):
        for div_name in li.find_all("div", class_="world-list__world_name"):
            for p_name in div_name.find_all("p"):
                if p_name.get_text() == server_name:
                    status = li.find_all("div", class_="world-list__world_category")
                    status = status[0].find_all("p")[0].get_text();
    print("%s: %s" % (time.strftime("%H:%M:%S", time.localtime()), status))
    if status != "Congested":
        exit(0)
    time.sleep(60)

