from django.core.management.base import BaseCommand, CommandError
import base64
import re
from market.models import Category, Product
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import urllib.request
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
import random

STOP_WORDS = ['Безопасная', 'скидка']


def get_product_description(link, category):
    URL = 'https://tainabox.com.ua'
    print('Start importing from %s' % URL+link)
    # rez = requests.get(URL + link, verify=False)
    rez = requests.get(URL + link)
    soup = BeautifulSoup(rez.text, 'html.parser')

    for desc in soup.findAll('div', {'class': 'product__big-item'}):
        image = desc.find('div', {'class': 'product__big-item_right'}).find('img')
        consist = desc.find('div', {'class': 'product__item__composition__value'})
        price = desc.find('div', {'class': 'to-order__value'})
        name = desc.find('div', {'product__big-item__name'})

        in_stop = False
        for w in STOP_WORDS:
            if name.text.find(w) > -1:
                in_stop = True
            if consist.text.find(w) > -1:
                in_stop = True

        if not in_stop:
            p = Product()
            p.name = re.sub('\n', '', name.text)
            p.price = re.split(r'\n', price.text)[0]
            p.consist = consist.text
            p.category = category
            img_url = URL + image['src']

            img_temp = NamedTemporaryFile(delete=True)
            req = urllib.request.Request(
                img_url,
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )

            img_temp.write(urllib.request.urlopen(req).read())
            img_temp.flush()
            img_res = re.split(r'\.', image['src'])
            p.image.save("image_.{}".format(img_res[-1]), File(img_temp))
            p.save()


def get_products(link, category):
    URL = 'https://tainabox.com.ua'
    print('Start importing from %s' % URL+link)
    rez = requests.get(URL + link)
    # rez = requests.get(URL + link, verify=False)
    html = re.sub("\"=\"\"", "=\"\"", rez.text)
    soup = BeautifulSoup(html, 'html5lib')

    for prod in soup.find('div', {'class': 'dishes-box'}).findAll('div', {'class': 'product__item__dish-item'}):
        for dish in prod.find('div', {'class': 'dish-top-img'}):
            if len(dish) > 1:
                if isinstance(dish, NavigableString):
                    continue
                if isinstance(dish, Tag):
                    taga = dish.prettify(formatter="html")
                link = re.search(r'href="([A-Za-z0-9\/-]+)"', taga)
                time.sleep(random.randint(1,5))
                get_product_description(link.group(1), category)


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Clearing DB')
        # удаляем записи и картинки
        Category.objects.all().delete()
        Product.objects.all().delete()
        # shutil.rmtree('%s/media/product' % BASE_DIR)

        # достаем главную страницу и парсим
        URL = 'https://tainabox.com.ua'
        print('Start importing from %s' % URL)
        rez = requests.get(URL)
        # rez = requests.get(URL, verify=False)
        soup = BeautifulSoup(rez.text, 'html.parser')

        # находим нужный див и в нем картинки
        content = soup.find('div', {'id': 'header-custom-middle-block'})
        for menu in content.findAll('ul', {'class': 'header__mid-menu'}):
            for category in menu.findAll('span', {'class': 'hlink'}):
                time.sleep(random.randint(1,5))
                c = Category()
                c.name = category.text
                c.save()
                link = base64.b64decode(category.attrs['data-href']).decode("utf-8")
                get_products(link, c)
            for category in menu.findAll('a'):
                print(category.text)
                c = Category()
                c.name = category.text
                c.save()
                get_products(category['href'], c)
