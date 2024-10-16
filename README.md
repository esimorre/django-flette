# django-flette
Minimalist wedding between django and flet

```commandline
cd todo
flet build web --base-url static/web main.py [-o build/web]
```


```bash
python manage.py migrate
# backend  (background)
python manage.py runserver 

# frontend (desktop mode)
flet run -p 8001 main.py


```
