## Jak projekt spustit lokálně (PyCharm IDE)
1. Otevřít projekt `django`
2. Je potřeba mít nainstalované `Python (verze 3.7)` a `MySQL server (verze 5.7)`
3. Nastavit Python interpreter (venv) - `File-Settings-Project-Project Interpreter`
4. Konfigurace projektu
```
pip install django
pip install djangorestframework
pip install mysqlclient
pip install django-cors-headers
```
Pokud by cokoliv z toho nešlo nainstalovat, je možné ruční přídání přes `File-Settings-Project-Project Interpreter- +`
Pravděpodobně bude vyžadována kombinace obojího

5. DB migrace
```
python manage.py makemigrations app
python manage.py migrate
```
6. Spuštění
```
python manage.py runserver 8080
```

Aplikace běží na `localhost:8080`

