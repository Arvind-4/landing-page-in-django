
# Landing Page

Make a Landing Page for your Business with Django and Postgres.

## Stack

- [Django](https://www.djangoproject.com) - Django makes it easier to build better web apps more quickly and with less code.
- [Bootstrap](https://getbootstrap.com/) - Build fast, responsive sites with Bootstrap.
- [Postgres](https://firebase.google.com/) - The World's Most Advanced Open Source Relational Database.

---

Deployed on [Vercel](https://vercel.com/). <br/>
Click Here for [Live Preview.](https://getidea.ml)

---




Add Your Environment variable to `.env`. <br />
 Refer `.sample.env` file.

--- 
# How to Run this Locally

### Step 1: Clone Repository:
```
cd /path/to/folder
mkdir landing
cd landing
git clone https://github.com/Arvind-4/Landing-Page-in-Django.git .
```

### Step 2: Create a Virtual Environment:
```
pip3 install virtualenv
cd landing
python3.9 -m virtualenv .
source bin/activate
```
**For Windows use:** `.\Scripts\activate`

### Step 3: Install Dependencies:
```
pip install -r requirements.txt
```


### Step 3: Run the Server
```
cd /path/to/folder/landing
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver localhost:8000
```

Open [localhost:8000](http://localhost:8000/) in Browser.
