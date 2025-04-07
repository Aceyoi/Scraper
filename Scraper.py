import requests
from bs4 import BeautifulSoup

def pars(pages=1):
    # Парсинг с первой до указанной страницы
    m = 1
    while m < pages:
        url = f"https://modrinth.com/mods?m=100&page={m}"
        print(f"Страница {m}")

        title = requests.get(url)

        soup = BeautifulSoup(title.text, "html.parser")

        mod  = soup.find_all('article', class_='project-card base-card padding-bg')

        mod_titles = []
        for data in mod:
            if data.find('h2', class_='name !text-2xl') is not None:
                mod_titles.append(data.find('h2', class_='name !text-2xl'))

        mod_author = []
        for data in mod:
            if data.find('a', class_='title-link') is not None:
                mod_author.append(data.find('a', class_='title-link'))

        mod_stat = []
        for data in mod:
            if data.find('span', class_='date-label') is not None:
                mod_stat.append(data.find_all('span', class_='date-label'))

        mod_overview = []
        for data in mod:
            if data.find('p', class_='description') is not None:
                mod_overview.append(data.find('p', class_='description'))

        i = 0
        while i < len(mod_titles):
            print(f"{mod_titles[i].text} by {mod_author[i].text} - {mod_overview[i].text}")
            i += 1
        m += 1

        #for data in mod_stat:
        #    print(f"{data}")

#Выбираем сколько страниц парсить
n = int(input("Сколько страниц парсим?:"))
pars(n)



