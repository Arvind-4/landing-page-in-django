# Landing-Page-in-Django

Make a Landing Page for your Business with Django and Postgres.

Take a Look What is Built. [landingbusinesspage.herokuapp.com](https://landingbusinesspage.herokuapp.com/)

# How to Run this Locally


### Step 1: Create a Virtual Environment
```
pip install virtualenv
cd /path/to/folder
mkdir landing_page
cd landing_page
virtualenv .
source scripts/activate
```

### Step 2: Clone Repository and Install Dependencies
```
cd /path/to/folder
mkdir src
cd src
git clone https://github.com/Arvind-4/Landing-Page-in-Django.git .
pip install -r requirements.txt
```

### Step 3: Run the Server
```
cd /path/to/folder/landing_page
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open [127.0.0.1:8000](http://127.0.0.1:8000/) in Browser.<br>
Take a Look at the Website on [landingbusinesspage.herokuapp.com](https://landingbusinesspage.herokuapp.com/)
