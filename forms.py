from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, HiddenField
from wtforms.validators import DataRequired
import json
from models import books

choices_list=[]
books_list = []
# wiem że ten kod nie powinien się to znajdować ale z jakiegoś powodu wstawienie tego kodu do models powoduje że lista autorów jest aktualizowana tylko co restart servera,
# to co zrobiłem poniżej to jedyny sposób który znajazłem na to by to działało tak jak chcę
def reload_authors():
    try:
        with open("authors.json", 'r') as f:
            authors_list = json.load(f)
    except FileNotFoundError:
        authors_list = []
    choices_list.clear()
    for author in authors_list:
        choices_list.append(f"{author.get('first_name')} {author.get('last_name')}")
reload_authors()

class BookForm(FlaskForm):
# chciałem tutaj dodać "id=hiddenfield("id", default=books.all()[-1]["id"]+1)" ale wartośc zmieniała się tylko przy restarcie servera
# np. dodanie 3 nowych książek po załadowaniu strony prowadziło do tego że wszystkie 3 miały to samo ID
# próbowałem to rozwiązać czymś podobnym do "reload_authors()"ale też nie działało
    id=HiddenField('id', default=int(books.last_id()) +1)
    title=StringField("Tytuł", validators=[DataRequired()])
    author=SelectField("Autor",choices = choices_list, validators=[DataRequired()])
    read=BooleanField("Czy przeczytana")
    length=IntegerField("Ilość stron", validators=[DataRequired()])

class AuthorForm(FlaskForm):
    first_name=StringField("Imie", validators=[DataRequired()])
    last_name=StringField('Nazwisko', validators=[DataRequired()])

