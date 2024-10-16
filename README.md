# django-flette
Minimalist wedding between django and flet

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
