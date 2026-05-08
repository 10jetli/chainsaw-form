# วิธีติดตั้งบน Replit

## ขั้นตอน (ทำครั้งเดียว ~5 นาที)

### 1. สมัคร Replit (ฟรี)
- ไปที่ https://replit.com
- กด Sign up → ใช้ Google account ได้เลย

### 2. สร้างโปรเจกต์
- กด **+ Create Repl**
- เลือก Template: **Python**
- ตั้งชื่อ: `chainsaw-form` หรืออะไรก็ได้
- กด **Create Repl**

### 3. อัปโหลดไฟล์
ลบไฟล์เดิมทั้งหมดออก แล้วอัปโหลด:
- `main.py`
- `requirements.txt`
- `.replit`
- โฟลเดอร์ `static/` (ที่มี `index.html` อยู่ข้างใน)

### 4. ใส่ API Key (สำคัญ!)
- ด้านซ้ายกด 🔒 **Secrets**
- กด **+ New Secret**
- Key: `ANTHROPIC_API_KEY`
- Value: ใส่ key จาก https://console.anthropic.com
- กด **Add Secret**

### 5. รัน
- กดปุ่ม **▶ Run** สีเขียว
- รอสักครู่ → จะได้ URL เช่น `https://chainsaw-form.yourname.repl.co`
- แชร์ URL นี้ให้ลูกค้าได้เลย!

## หมายเหตุ
- Replit ฟรีมี sleep หลังไม่มีคนใช้ ~1 ชั่วโมง (ครั้งแรกที่เปิดจะช้า 10-20 วินาที)
- ถ้าอยากให้ออนไลน์ตลอด 24 ชั่วโมง ต้องสมัคร Replit Core (~$7/เดือน)
- API Key เก็บใน Secrets ปลอดภัย ลูกค้าไม่เห็น
