# 📚 คู่มือการตั้งค่า Lab 03: LINE Gold Price Bot

## 📋 สารบัญ

1. [สร้าง LINE Messaging API Channel](#1-สร้าง-line-messaging-api-channel)
2. [ติดตั้งและตั้งค่า ngrok](#2-ติดตั้งและตั้งค่า-ngrok)
3. [รัน n8n](#3-รัน-n8n)
4. [ตั้งค่า LINE Webhook](#4-ตั้งค่า-line-webhook)
5. [ทดสอบระบบ](#5-ทดสอบระบบ)

---

## 1. สร้าง LINE Messaging API Channel

### 1.1 เข้าสู่ LINE Developers Console

1. ไปที่ [https://developers.line.biz/console/](https://developers.line.biz/console/)
2. คลิก **Log in with LINE account**
3. Login ด้วย LINE Account ของคุณ

### 1.2 สร้าง Provider

> Provider คือกลุ่มของ Channels ที่จัดการโดยบุคคล/องค์กรเดียวกัน

1. คลิก **Create** ที่หน้า Providers
2. ใส่ชื่อ Provider เช่น `My LINE Bots`
3. คลิก **Create**

### 1.3 สร้าง Messaging API Channel

1. เลือก Provider ที่สร้างไว้
2. คลิก **Create a new channel**
3. เลือก **Messaging API**
4. กรอกข้อมูล:

| Field | ตัวอย่าง | หมายเหตุ |
|-------|---------|----------|
| Channel type | Messaging API | เลือกไว้แล้ว |
| Provider | My LINE Bots | เลือก Provider |
| Channel icon | (อัพโหลดรูป) | Optional |
| Channel name | Gold Price Bot | ชื่อ Bot |
| Channel description | Bot ราคาทอง | คำอธิบาย |
| Category | Finance | หมวดหมู่ |
| Subcategory | Financial Services | หมวดย่อย |

5. ติ๊ก ✅ ยอมรับ Terms of Use
6. คลิก **Create**

### 1.4 ตั้งค่า Channel

#### เปิด Messaging API Tab

1. คลิกที่ Channel ที่สร้าง
2. ไปที่ **Messaging API** tab

#### Issue Channel Access Token

1. เลื่อนลงไปที่ **Channel access token**
2. คลิก **Issue**
3. **คัดลอก Token เก็บไว้** (จะใช้ใน n8n)

```
⚠️ สำคัญ: อย่าเผยแพร่ Token นี้!
```

#### ปิด Auto-reply

1. ในส่วน **LINE Official Account features**
2. คลิก **Edit** ที่ Auto-reply messages
3. จะเปิดหน้า LINE Official Account Manager
4. ไปที่ **ตอบกลับ** > **การตอบกลับอัตโนมัติ**
5. **ปิด** ข้อความตอบกลับอัตโนมัติ
6. **ปิด** ข้อความทักทาย

### 1.5 จด Bot Basic ID / QR Code

- ใน **Messaging API** tab จะมี:
  - **Bot basic ID**: @xxx
  - **QR Code**: สำหรับเพิ่มเพื่อน

---

## 2. ติดตั้งและตั้งค่า ngrok

### 2.1 สมัครบัญชี ngrok

1. ไปที่ [https://ngrok.com/](https://ngrok.com/)
2. คลิก **Sign up for free**
3. สมัครด้วย Email หรือ GitHub/Google
4. ยืนยัน Email

### 2.2 ติดตั้ง ngrok

#### Windows (Chocolatey)
```powershell
choco install ngrok
```

#### Windows (Manual)
1. ดาวน์โหลดจาก [https://ngrok.com/download](https://ngrok.com/download)
2. แตกไฟล์ zip
3. ย้าย `ngrok.exe` ไปที่ต้องการ (เช่น `C:\ngrok\`)
4. เพิ่ม path ใน Environment Variables

#### macOS (Homebrew)
```bash
brew install ngrok
```

#### Linux (apt)
```bash
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
  sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
  echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
  sudo tee /etc/apt/sources.list.d/ngrok.list && \
  sudo apt update && sudo apt install ngrok
```

### 2.3 ตั้งค่า Authtoken

1. Login เข้า [ngrok Dashboard](https://dashboard.ngrok.com/)
2. ไปที่ **Your Authtoken**
3. คัดลอก Authtoken
4. รันคำสั่ง:

```bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

### 2.4 ทดสอบ ngrok

```bash
ngrok http 5678
```

ถ้าสำเร็จจะเห็น:

```
Session Status                online
Account                       your-email@example.com
Version                       3.x.x
Region                        Asia Pacific (ap)
Forwarding                    https://xxxx-xx-xx-xx-xx.ngrok-free.app -> http://localhost:5678

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

**จด URL นี้ไว้**: `https://xxxx-xx-xx-xx-xx.ngrok-free.app`

---

## 3. รัน n8n

### 3.1 รัน n8n ด้วย Docker

#### Terminal 1 - รัน n8n

```bash
docker run -it --rm --name n8n \
  -p 5678:5678 \
  -e N8N_SECURE_COOKIE=false \
  n8nio/n8n
```

เปิด browser ไปที่: [http://localhost:5678](http://localhost:5678)

### 3.2 รัน ngrok

#### Terminal 2 - รัน ngrok

```bash
ngrok http 5678
```

### 3.3 จด URLs

| Service | URL |
|---------|-----|
| n8n Local | `http://localhost:5678` |
| n8n Public (ngrok) | `https://xxxx.ngrok-free.app` |
| Webhook URL | `https://xxxx.ngrok-free.app/webhook/gold-bot` |

---

## 4. ตั้งค่า LINE Webhook

### 4.1 สร้าง Workflow ใน n8n ก่อน

> ต้องสร้าง Webhook Node ก่อน เพื่อให้ n8n รู้จัก path

1. เปิด n8n
2. สร้าง Workflow ใหม่
3. เพิ่ม **Webhook** Node
4. ตั้งค่า:
   - HTTP Method: `POST`
   - Path: `gold-bot`
5. คลิก **Listen for Test Event** หรือ **Test workflow**

### 4.2 ตั้งค่าใน LINE Developers Console

1. ไปที่ [LINE Developers Console](https://developers.line.biz/console/)
2. เลือก Channel ของคุณ
3. ไปที่ **Messaging API** tab
4. เลื่อนไปที่ **Webhook settings**

#### ใส่ Webhook URL

```
https://xxxx.ngrok-free.app/webhook/gold-bot
```

⚠️ **แทนที่ `xxxx.ngrok-free.app` ด้วย URL จาก ngrok ของคุณ**

#### เปิดใช้งาน Webhook

1. เปิด **Use webhook** ให้เป็น ON
2. คลิก **Verify**

#### ผลลัพธ์ที่ถูกต้อง

```
✅ Success
```

ถ้าเห็น Error:
- ตรวจสอบว่า n8n ทำงานอยู่
- ตรวจสอบว่า ngrok ทำงานอยู่
- ตรวจสอบ URL ให้ถูกต้อง

---

## 5. ทดสอบระบบ

### 5.1 เพิ่ม Bot เป็นเพื่อน

1. ใน LINE Developers Console > Messaging API tab
2. สแกน **QR Code** ด้วย LINE App
3. เพิ่มเป็นเพื่อน

### 5.2 ทดสอบส่งข้อความ

1. เปิด LINE App
2. เปิดแชทกับ Bot
3. พิมพ์: `ราคาทอง`
4. Bot ควรตอบกลับด้วยราคาทองล่าสุด

### 5.3 ตรวจสอบ Execution ใน n8n

1. ไปที่ n8n
2. คลิก **Executions** (ซ้ายมือ)
3. ดูผลการทำงานของ Workflow

---

## 🔧 Troubleshooting

### ปัญหา: Webhook Verify ไม่ผ่าน

**สาเหตุ**: n8n ไม่ได้รับ request

**แก้ไข**:
1. ตรวจสอบว่า n8n ทำงานอยู่
2. ตรวจสอบว่า ngrok ทำงานอยู่
3. ตรวจสอบ URL ให้ถูกต้อง (รวม `/webhook/gold-bot`)
4. ใน n8n ต้องกด **Test workflow** หรือ **Listen for Test Event**

### ปัญหา: Bot ไม่ตอบกลับ

**สาเหตุที่เป็นไปได้**:
1. Workflow ไม่ถูกต้อง
2. Channel Access Token ผิด
3. Auto-reply ยังเปิดอยู่

**แก้ไข**:
1. ดู Execution log ใน n8n
2. ตรวจสอบ Token
3. ปิด Auto-reply ใน LINE Official Account Manager

### ปัญหา: Error 401 Unauthorized

**สาเหตุ**: Channel Access Token ไม่ถูกต้อง

**แก้ไข**:
1. ไป LINE Developers Console
2. Issue Token ใหม่
3. อัพเดท Token ใน n8n

### ปัญหา: ngrok URL เปลี่ยน

**สาเหตุ**: รัน ngrok ใหม่ (Free plan URL จะเปลี่ยน)

**แก้ไข**:
1. จด URL ใหม่จาก ngrok
2. อัพเดท Webhook URL ใน LINE Console
3. Verify อีกครั้ง

---

## 📝 Checklist ก่อนส่งงาน

- [ ] สร้าง LINE Channel แล้ว
- [ ] ได้ Channel Access Token แล้ว
- [ ] ติดตั้ง ngrok แล้ว
- [ ] รัน n8n + ngrok ได้
- [ ] สร้าง Workflow ครบทุก Node
- [ ] ตั้งค่า Webhook URL ใน LINE แล้ว
- [ ] ทดสอบส่งข้อความ "ราคาทอง" แล้ว Bot ตอบ
- [ ] Export workflow.json แล้ว
- [ ] Push ขึ้น GitHub แล้ว

---

## 📞 ต้องการความช่วยเหลือ?

- สร้าง Issue ใน Repository
- ถามใน Discord/LINE Group ของวิชา
- ติดต่ออาจารย์ผู้สอน
