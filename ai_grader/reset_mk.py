# tra_cuu.py
from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    print("="*50)
    print(" 🕵️ DANH SÁCH TOÀN BỘ TÀI KHOẢN TRONG HỆ THỐNG ")
    print("="*50)
    
    # 1. Tra cứu toàn bộ tài khoản
    users = User.query.all()
    if not users:
        print("❌ Cơ sở dữ liệu đang trống rỗng, chưa có tài khoản nào!")
    else:
        for u in users:
            print(f"👉 Mã Đăng Nhập: {u.student_id: <15} | Quyền: {u.role}")
            
    print("-" * 50)
    
    # 2. Ép đổi mật khẩu
    print("\n💡 CHẾ ĐỘ CỨU HỘ:")
    target_id = input("Nhập 'Mã Đăng Nhập' của Admin (hoặc tài khoản) bạn muốn reset mật khẩu (Bấm Enter để bỏ qua): ")
    
    if target_id.strip():
        user = User.query.filter_by(student_id=target_id.strip()).first()
        if user:
            # Ép mật khẩu mới
            user.password = generate_password_hash('123456')
            db.session.commit()
            print(f"\n✅ THÀNH CÔNG! Đã ép đổi mật khẩu của '{user.student_id}' về mặc định là: 123456")
            print("Đại vương có thể quay lại Web để đăng nhập ngay!")
        else:
            print(f"\n❌ Lỗi: Không tìm thấy tài khoản có mã '{target_id}' trong hệ thống.")
    else:
        print("\nĐã thoát chế độ cứu hộ.")