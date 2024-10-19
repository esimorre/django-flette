# django-flette
Minimalist wedding between django and flet
[Live demo](https://ricocs.alwaysdata.net/)

Implementation of a minimalist pure python frontend/backend POC based on django and flet

   * no DRF but a simple json view
   * reuse of the flet "todo" sample
   * a unique API function: initial loading of tasks corresponding to the names of django groups in base


## flet client generation 
```python
# can modify this in todo/main.py
API_URL = "https://MYSITE/api/"
# or with same origin
API_URL = None
```

```bash
cd todo
# --web-renderer html : lighter client
flet build web --base-url frontend --web-renderer html -o ../static/web
cd ..
zip static
```

## Installation (dev local)
```bash
python manage.py migrate
# populate: user admin(admin) & groups/tasks
python manage.py loaddata data.yaml

# frontend & backend (same origin)
python manage.py runserver 

# separate frontend (desktop mode)
flet run -p 8001 main.py

# separate frontend (browser)
flet run -p 8001 --web main.py
```

## Deployement
```bash
wget https://github.com/esimorre/django-flette/archive/refs/heads/master.zip
unzip master.zip
(build venv)
pip install django==5.0 pyYAML
get static.zip
unzip static.zip -d ROOT_PROJECT

# Apache: static pathes
#/frontend/admin/=/.venv/lib/python3.12/site-packages/django/contrib/admin/static/admin/
#/frontend/=/ROOT_PROJECT/static/web/
```