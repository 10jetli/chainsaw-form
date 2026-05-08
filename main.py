from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='static')
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB

# ใส่ Anthropic API Key ตรงนี้
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', 'ใส่-key-ของคุณ-ตรงนี้')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/read-card', methods=['POST'])
def read_card():
    try:
        body = request.get_json()
        image_data = body.get('image')
        mime_type = body.get('mime', 'image/jpeg')

        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers={
                'x-api-key': ANTHROPIC_API_KEY,
                'anthropic-version': '2023-06-01',
                'content-type': 'application/json',
            },
            json={
                'model': 'claude-sonnet-4-20250514',
                'max_tokens': 1000,
                'messages': [{
                    'role': 'user',
                    'content': [
                        {
                            'type': 'image',
                            'source': {
                                'type': 'base64',
                                'media_type': mime_type,
                                'data': image_data
                            }
                        },
                        {
                            'type': 'text',
                            'text': '''นี่คือรูปบัตรประชาชนไทย อ่านข้อมูลทั้งหมดแล้วตอบเป็น JSON เท่านั้น ห้ามมีข้อความอื่น:
{"prefix":"นาย หรือ นาง หรือ นางสาว","firstname":"ชื่อภาษาไทย","lastname":"นามสกุลภาษาไทย","idcard":"เลข 13 หลักตัวเลขล้วน","dob":"วันเกิดภาษาไทย เช่น 10 เมษายน 2503","baan":"บ้านเลขที่","moo":"หมู่ที่","tambon":"ตำบลหรือแขวง","amphoe":"อำเภอหรือเขต","changwat":"จังหวัด"}
ถ้าอ่านค่าใดไม่ได้ให้ใส่ ""'''
                        }
                    ]
                }]
            },
            timeout=30
        )

        data = response.json()
        if 'error' in data:
            return jsonify({'error': data['error']['message']}), 400

        raw = ''.join(b.get('text', '') for b in data.get('content', []))
        import re, json
        m = re.search(r'\{[\s\S]*\}', raw)
        if not m:
            return jsonify({'error': 'อ่านบัตรไม่ได้ กรุณาถ่ายรูปใหม่ให้ชัดขึ้น'}), 400

        return jsonify(json.loads(m.group(0)))

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
