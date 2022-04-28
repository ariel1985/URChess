# Chess Multi Player Django Rest Framework

# Initial Set Up 

Install all required packages from file
```bash
pip install -r requirements.txt
```
Set up Database
```bash
python manage.py makemigrations
python manage.py migrate
```
Create admin user
```bash
python manage.py createsuperuser
```

# Run

```bash

python manage.py runserver
```

Add new game CURL:

```bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://localhost:8000/api/

curl --data "param1=value1&param2=value2" http://localhost:8000/api/

```

To do :
 
 - Initate game (set in db via api)
 - set game board by FEN string
 - save moves
