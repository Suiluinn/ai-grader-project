import requests

# ĐIỀN KEY CỦA BẠN VÀO ĐÂY
KEY = "AIzaSyBd9tovOYW5q3TBs6-enZalTpB3hxjDfMc"
URL = f"https://generativelanguage.googleapis.com/v1beta/models?key={KEY}"

print("--- Đang lấy danh sách các Model khả dụng... ---")
try:
    res = requests.get(URL)
    data = res.json()
    if res.status_code == 200:
        print("CÁC MODEL BẠN CÓ THỂ DÙNG LÀ:")
        for m in data['models']:
            print(f"- {m['name']}")
    else:
        print(f"Lỗi {res.status_code}: {res.text}")
except Exception as e:
    print(f"Lỗi kết nối: {e}")