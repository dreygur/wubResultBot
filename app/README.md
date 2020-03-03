# APP

We have separated the source codes from Heroku specific configs and stored the sources here.

The directory contais:
- app.py
- models.py
- views.py
- static files
- template files
- Database files

To run this app you need to have `python3`and `Flask`
```bash
python3 -m pip install Flask
```

To run:
```bash
python3 app.py
```

or to run using gunicorn:
```bash
gunicorn app:app --log-file=-
```

Created with :heart: ash burned in :fire: