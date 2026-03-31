from Lioris import database, app
from Lioris.models import Usuario, Foto

with app.app_context():
    database.create_all()



