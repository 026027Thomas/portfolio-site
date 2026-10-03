git clone <repository>
cd <project>
python -M venv .venv
source .venv/bin/activate
pin install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver