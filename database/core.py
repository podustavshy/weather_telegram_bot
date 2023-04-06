from database.common.models import db, History


db.connect()
db.create_tables([History])
