# Port Express · Hamster Hub

หน้าขายคอร์ส **Port Express** คอร์สทำพอร์ตเกม 2 เดือนสำหรับน้อง ม.6 โดย Hamster Hub

- `index.html` หน้าเว็บที่พร้อมใช้ เปิดไฟล์เดียวได้เลย (รูปทั้งหมดฝังอยู่ในไฟล์)
- `src/port-express.tpl.html` ต้นฉบับ HTML/CSS/JS
- `src/data.json` รูปทั้งหมดแบบ data URI ที่ template เรียกใช้
- `src/build.py` สร้าง `index.html` ใหม่จาก template
- `assets/logo-aurora.png` โลโก้ Port Express พื้นใส

## แก้แล้วสร้างใหม่

```
python src/build.py
```

## ข้อมูลที่ต้องเช็กก่อนขึ้นจริง

อยู่ใน `CONFIG` ใน template: วันปิดรับสมัคร (`closeAt`), LINE ID และตัวเลขสถิติ 50% / 15%
รวมถึงวันเริ่มเรียน 1 ธ.ค. ในหน้าแรก

## เปิดเป็นเว็บด้วย GitHub Pages

Settings → Pages → Deploy from a branch → `main` / root
