# 📝 Quiz - Lab 03: LINE Messaging API & External API Integration

## คำชี้แจง
- Quiz มีทั้งหมด 10 ข้อ
- แต่ละข้อ 10 คะแนน รวม 100 คะแนน
- เลือกคำตอบที่ถูกต้องที่สุดเพียงข้อเดียว

---

## ข้อ 1: LINE Webhook Protocol (10 คะแนน)

LINE Webhook **ต้อง**ใช้ Protocol ใดในการรับข้อมูล?

- A) HTTP
- B) HTTPS
- C) FTP
- D) WebSocket

---

## ข้อ 2: ngrok คืออะไร (10 คะแนน)

ngrok ทำหน้าที่อะไรใน Lab นี้?

- A) เป็น Database สำหรับเก็บข้อมูล
- B) สร้าง HTTPS Tunnel จาก localhost ไปยัง Internet
- C) เป็น LINE Bot SDK
- D) เป็น API สำหรับดึงราคาทอง

---

## ข้อ 3: Thai Gold API Method (10 คะแนน)

Thai Gold API (`https://api.chnwt.dev/thai-gold-api/latest`) ใช้ HTTP Method ใด?

- A) POST
- B) PUT
- C) GET
- D) DELETE

---

## ข้อ 4: LINE Authentication Header (10 คะแนน)

เมื่อเรียก LINE Reply API ต้องใส่ Header ใดสำหรับ Authentication?

- A) `X-API-Key: YOUR_TOKEN`
- B) `Authorization: Bearer YOUR_TOKEN`
- C) `Token: YOUR_TOKEN`
- D) `Auth: YOUR_TOKEN`

---

## ข้อ 5: Gold API Response Structure (10 คะแนน)

จาก Thai Gold API Response ข้อมูลราคา**ทองคำแท่ง**อยู่ใน field ใด?

```json
{
  "response": {
    "price": {
      "gold": { "buy": "71,631.00", "sell": "74,100.00" },
      "gold_bar": { "buy": "73,100.00", "sell": "73,300.00" }
    }
  }
}
```

- A) `response.price.gold`
- B) `response.price.gold_bar`
- C) `response.gold_bar`
- D) `price.gold_bar`

---

## ข้อ 6: LINE replyToken (10 คะแนน)

`replyToken` ใน LINE Webhook Event ใช้ทำอะไร?

- A) ยืนยันตัวตนของ Bot
- B) ใช้ตอบกลับข้อความไปยังผู้ใช้
- C) เข้ารหัสข้อความ
- D) ระบุประเภทของข้อความ

---

## ข้อ 7: LINE Reply API URL (10 คะแนน)

URL ที่ถูกต้องสำหรับส่งข้อความตอบกลับผู้ใช้ LINE คือข้อใด?

- A) `https://api.line.me/v2/bot/message/push`
- B) `https://api.line.me/v2/bot/message/reply`
- C) `https://api.line.me/v2/message/send`
- D) `https://line.me/api/reply`

---

## ข้อ 8: n8n Code Node Language (10 คะแนน)

n8n Code Node ใช้ภาษาอะไรในการเขียน?

- A) Python
- B) Java
- C) JavaScript
- D) PHP

---

## ข้อ 9: Thai Gold API URL (10 คะแนน)

URL ที่ถูกต้องของ Thai Gold API ที่ใช้ใน Lab นี้คือข้อใด?

- A) `https://goldprice.org/api/latest`
- B) `https://api.gold.com/v1/price`
- C) `https://api.chnwt.dev/thai-gold-api/latest`
- D) `https://thai-gold.herokuapp.com/api`

---

## ข้อ 10: Workflow Node Order (10 คะแนน)

ลำดับ Node ที่ถูกต้องใน Workflow ของ Lab นี้คือข้อใด?

- A) Webhook → HTTP Request (Gold) → Code → HTTP Request (LINE)
- B) HTTP Request (Gold) → Webhook → Code → HTTP Request (LINE)
- C) Webhook → Code → HTTP Request (Gold) → HTTP Request (LINE)
- D) Code → Webhook → HTTP Request (Gold) → HTTP Request (LINE)

---

## ส่งคำตอบ

กรอกคำตอบในรูปแบบ:
```
1. _
2. _
3. _
4. _
5. _
6. _
7. _
8. _
9. _
10. _
```
