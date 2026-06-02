import sqlite3

# Kết nối thẳng vào file database vật lý
conn = sqlite3.connect('grader.db')
cursor = conn.cursor()

# Ép nó đúc ra cái bảng này
cursor.execute('''
CREATE TABLE IF NOT EXISTS lesson_document (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    file_name VARCHAR(255),
    file_path VARCHAR(255),
    extracted_text TEXT
)
''')

conn.commit()
conn.close()

print("==================================================")
print("🚀 ĐÃ DÙNG VŨ LỰC TẠO BẢNG THÀNH CÔNG VÀO GRADER.DB!")
print("==================================================")