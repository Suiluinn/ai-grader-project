from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# KHỞI TẠO DB 
db = SQLAlchemy()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True) # Mã Sinh Viên
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False) # 'Admin' hoặc 'Student'
    full_name = db.Column(db.String(100))
    school = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    # Liên kết với bảng Submission (Khi xóa User, xóa luôn bài nộp)
    submissions = db.relationship('Submission', backref='user', lazy=True, cascade="all, delete-orphan")

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    max_score = db.Column(db.Float, default=10)
    # Liên kết với các bảng con
    test_cases = db.relationship('TestCase', backref='problem', cascade="all, delete-orphan")
    submissions = db.relationship('Submission', backref='problem', lazy=True, cascade="all, delete-orphan")

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=False)
    input_data = db.Column(db.Text, nullable=False)
    expected_output = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float, default=1.0) # Điểm số riêng cho từng test case

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=False)
    code_content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(100)) # VD: 'Pass Toàn Bộ', 'Lỗi Cú Pháp'
    final_score = db.Column(db.Float, default=0.0)
    ai_hint = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    questions = db.Column(db.Text)  # Lưu toàn bộ đề dưới dạng chuỗi JSON
    is_active = db.Column(db.Boolean, default=True) # Tính năng Bật/Tắt làm bài
    created_at = db.Column(db.DateTime, default=datetime.now)

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    score = db.Column(db.Float)
    

    user_answers = db.Column(db.Text) 
    
    submitted_at = db.Column(db.DateTime, default=datetime.now)

class LessonDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False) # Tên buổi học/bài giảng
    file_name = db.Column(db.String(255))             # Tên file gốc (VD: bai1.pdf)
    file_path = db.Column(db.String(255))             # Đường dẫn lưu file trên server
    extracted_text = db.Column(db.Text)               # Chứa toàn bộ chữ bóc tách được để cho AI đọc

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255))
    option_b = db.Column(db.String(255))
    option_c = db.Column(db.String(255))
    option_d = db.Column(db.String(255))
    correct_answer = db.Column(db.String(1))