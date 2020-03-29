import django
django.setup()


def parse_mods():
    from bs4 import BeautifulSoup

    from mods.models import Mod

    html_file = open('modlist.html')
    html = BeautifulSoup(html_file, 'html.parser')
    modlist = html.find_all('li')
    modlist = sorted(modlist, key=lambda x: x.get_text().lower())

    for mod in modlist:
        mod_update = Mod(title=mod.get_text())
        mod_update.save()

    html_file.close()


parse_mods()
