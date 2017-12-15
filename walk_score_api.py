import urllib2
from bs4 import BeautifulSoup


def get_score(address, city, state, zip_code, score_type):
    string_address = "-".join([address.replace(" ","-"), city.replace(" ","-"), state, zip_code])
    url = "{u}{a}".format(u="https://www.walkscore.com/score/", a=string_address)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    data_tag = "score page {t} badge".format(t=score_type)
    try:
        score_div = soup.find("div", attrs={"class": "block-header-badge score-info-link", "data-eventsrc": data_tag})
        image_string = score_div.find("img").attrs["src"]
        return int(image_string.split("/")[-1].split(".")[0])
    except AttributeError:
        print("Could not find {t} score for {a}".format(t=score_type, a=address))
        return None

def get_walk_score(address, city, state, zip_code):
    return get_score(address, city, state, zip_code, "walk")


def get_transit_score(address, city, state, zip_code):
    return get_score(address, city, state, zip_code, "transit")




def walk_score_api(address, city, state, zip_code):
    from geopy.geoencoders import Nominatim
    API_KEY = "71cbe4b96d79399d9dc173d3944685aa"
    geolocator = Nominatim()
    address_string = "{a} {c}".format(a=address, c=city)
    address = {
                "street": address,
                "city": city,
                "postalcode": zip_code,
                "state": state
              }
    location = goelocator.geocode(address)
