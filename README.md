# WUB Result Bot

This bot aims to provide student's grade over facebook messenger platform as text message using chatfuel and heruko services.
This is a fun project and it will not actively maintained.

To run this app you need to have `python3, Flask`and `gunicorn` (Optional)
```bash
python3 -m pip install Flask gunicorn
```

To run:
```bash
python3 app/app.py
```

or to run using gunicorn:
```bash
gunicorn --chdir app app:app --log-file=-
```

Maintainer [Rakibul Yeasin](https://www.facebook.com/dreygur) & [Mohammad Rohel](https://www.facebook.com/null.rohel)

Created with :heart: ash burned in :fire: