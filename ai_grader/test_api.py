import requests
import json

def check_gemini_api_key(api_key):
    print("⏳ Đang kết nối tới máy chủ Google Gemini...")
    
    # Endpoint chuẩn của Gemini API
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    
    # Gửi một câu chào cực kỳ đơn giản để test
    data = {
        "contents": [{"parts": [{"text": "Xin chào, hãy trả lời ngắn gọn: Bạn có hoạt động không?"}]}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        # Nếu mã trả về là 200 -> Thành công tuyệt đối
        if response.status_code == 200:
            result = response.json()
            ai_reply = result['candidates'][0]['content']['parts'][0]['text']
            print("\n✅ THÀNH CÔNG! API Key của bạn hoàn toàn hợp lệ và đang hoạt động.")
            print(f"🤖 Trợ lý AI trả lời: {ai_reply.strip()}")
            
        # Nếu mã là 400 (Bad Request) thường do API Key sai bét
        elif response.status_code == 400:
            print("\n❌ THẤT BẠI: Lỗi 400 - API Key của bạn không đúng hoặc bị copy thiếu ký tự.")
            print(f"Chi tiết từ Google: {response.json()}")
            
        # Nếu mã là 429 (Too Many Requests) do hết Quota hoặc spam quá nhiều
        elif response.status_code == 429:
            print("\n⚠️ CẢNH BÁO: Lỗi 429 - API Key của bạn đã hoạt động nhưng bị vượt quá giới hạn lượt gọi (Hết Quota).")
            
        # Các lỗi máy chủ khác (500, 503)
        else:
            print(f"\n❌ LỖI KHÔNG XÁC ĐỊNH: Mã lỗi {response.status_code}")
            print(f"Chi tiết: {response.json()}")
            
    except Exception as e:
        print(f"\n❌ LỖI MẠNG: Không thể kết nối tới Google. Vui lòng kiểm tra lại Wifi/Internet. Chi tiết: {e}")

# ==========================================
# ĐẠI VƯƠNG HÃY DÁN API KEY VÀO TRONG NGOẶC KÉP Ở DƯỚI ĐÂY
# ==========================================
MY_API_KEY = "AIzaSyCSDHw-n9F5id2cHMJ6o0wpxwXhEyR0Xyo"

check_gemini_api_key(MY_API_KEY)