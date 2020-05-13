import requests
import discord
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup as bs
from tqdm import tqdm


async def sendlolHentai(ctx, champion: str):

    url = "https://www.lolhentai.net/index?/category/"+champion

    get_all_images(url)


def get_all_images(url):

    urls = []

    images = bs(requests.get(url).content, "html.parser")

    for img in tqdm(images.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        
    img_url = urljoin(url, img_url)

    print(images)