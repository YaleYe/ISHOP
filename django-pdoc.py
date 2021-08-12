# Based on github.com/pdoc3/pdoc#314
import os
import sys

sys.path.append(os.path.abspath('../YihongYe/'))  # path to your django project

# Specify settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'COSC481.settings')

# Setup Django
import django
django.setup()

import pdoc

modules = ['core.models', 'core.views']
context = pdoc.Context()

modules = [pdoc.Module(mod, context=context)
           for mod in modules]
pdoc.link_inheritance(context)

def recursive_htmls(mod):
    yield mod.name, mod.html()
    for submod in mod.submodules():
        yield from recursive_htmls(submod)

for mod in modules:
    for module_name, html in recursive_htmls(mod):
        with open(f"dev-docs/{module_name}.html", "w", encoding="utf8") as f:
            f.write(html)
