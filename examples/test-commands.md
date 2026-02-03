# 🧪 คำสั่งทดสอบ Lab 03

## ทดสอบ Thai Gold API

### ด้วย curl
```bash
curl -X GET https://api.chnwt.dev/thai-gold-api/latest
```

### ด้วย PowerShell
```powershell
Invoke-RestMethod -Uri "https://api.chnwt.dev/thai-gold-api/latest" -Method Get
```

## ทดสอบ LINE Reply API

### ด้วย curl
```bash
curl -X POST https://api.line.me/v2/bot/message/reply \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_CHANNEL_ACCESS_TOKEN" \
  -d '{
    "replyToken": "YOUR_REPLY_TOKEN",
    "messages": [
      {
        "type": "text",
        "text": "Hello, World!"
      }
    ]
  }'
```

### ด้วย PowerShell
```powershell
$headers = @{
    "Content-Type" = "application/json"
    "Authorization" = "Bearer YOUR_CHANNEL_ACCESS_TOKEN"
}

$body = @{
    replyToken = "YOUR_REPLY_TOKEN"
    messages = @(
        @{
            type = "text"
            text = "Hello, World!"
        }
    )
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Uri "https://api.line.me/v2/bot/message/reply" -Method Post -Headers $headers -Body $body
```

## ทดสอบ Webhook ใน n8n (ผ่าน ngrok)

### ด้วย curl
```bash
curl -X POST https://YOUR-NGROK-URL.ngrok-free.app/webhook/gold-bot \
  -H "Content-Type: application/json" \
  -d '{
    "events": [{
      "type": "message",
      "replyToken": "test-token",
      "message": {
        "type": "text",
        "text": "ราคาทอง"
      }
    }]
  }'
```

## หมายเหตุ

- แทนที่ `YOUR_CHANNEL_ACCESS_TOKEN` ด้วย Token จริง
- แทนที่ `YOUR_REPLY_TOKEN` ด้วย replyToken จริง (ได้จาก LINE Event)
- แทนที่ `YOUR-NGROK-URL` ด้วย URL จาก ngrok
