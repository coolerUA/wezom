# Practical work on course Wezom Python Marathon 4
Angular frontend and Django backend 


# Angular
To install angular frontend dependencies run 
```
npm install
```

To start frontend run
```
ng serve
```

# Django
To setup django backend you have to create virtual environtment
```
virtualenv -p /usr/bin/python3 pybackvenv
```
Activate and install all requirements. 
```
source ./pybackvenv/bin/activate
```
After that create and apply all migrations
```
python manage.py makemigrations
python manage.py migrate
```
Ceate superuser
```
python manage.py createsuperuser
```
Load into db products and categories
```
python manage.py load_from_inet
```
Run server (*if you change port here, you have to change backend port in angular/src/assets/env.ts*)
```
python manage.py runserver 8000
```

# Scripts
Or you can use shell scripts to automate.
* **install** installing all in angular and pyback
* **run_back** to start django backend server on port 8000
* **run_front** to start frontend server on port 4200

