from app import app, db
from models import LessonDocument

with app.app_context():
    db.create_all()
    print(" ĐÃ TẠO BẢNG LESSON_DOCUMENT THÀNH CÔNG!")
