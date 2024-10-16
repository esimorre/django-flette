# django-flette
Minimalist wedding between django and flet

Implementation of a minimalist pure python frontend/backend POC based on django and flet

   * no DRF but a simple json view
   * reuse of the flet "todo" sample
   * a unique API function: initial loading of tasks corresponding to the names of django groups in base



```commandline
cd todo
flet build web --base-url frontend -o ../static/web main.py
```


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
venv
pip install django==5.0 pyYAML
get static.zip
unzip static.zip

```
