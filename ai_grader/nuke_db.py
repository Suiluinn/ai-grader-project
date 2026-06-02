from app import app, db
from sqlalchemy import text

with app.app_context():
    # Dùng chính kết nối nội bộ của Flask để ép tạo bảng bằng SQL thuần
    sql = text('''
    CREATE TABLE IF NOT EXISTS lesson_document (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255) NOT NULL,
        file_name VARCHAR(255),
        file_path VARCHAR(255),
        extracted_text TEXT
    )
    ''')
    db.session.execute(sql)
    db.session.commit()
    print(" ĐÃ TIÊM BẢNG VÀO ĐÚNG CÁI DATABASE FLASK ĐANG DÙNG!")
