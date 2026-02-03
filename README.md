scout-platform/
│
├── app/ # FastAPI uygulaması
│ │
│ ├── main.py # FastAPI giriş noktası
│ ├── dependencies.py # sayfadaki tüm bağımılıkları yönetiyor.
│ │
│ ├── core/ # config & ayarlar
│ │ ├── config.py
│ │ └── database.py
│ │
│ ├── db/
│ │ ├── base.py
│ │ └──
│ │
│ ├── models/ # SQLAlchemy modelleri
│ │ ├── user.py
│ │ ├── league.py
│ │ ├── team.py
│ │ ├── player.py
│ │ ├── season.py
│ │ └── stats.py
│ │
│ │
│ ├── routers/ # get - post methodları
├── league.py
│ │ ├── pages.py
│ │ ├── auth.py
│ │ ├── players.py
│ │ └──
│ │
│ ├── schemas/ # Pydantic response modelleri
│ │ ├── player.py
│ │ └── team.py
│ │
│ ├── api/ # API route'ları
│ │ ├── players.py
│ │ ├── teams.py
│ │ └── leagues.py
│ │
│ ├── services/ # iş mantığı
│ │ ├── scouting.py
│ │ └── ranking.py
│ │
│ ├── templates/ # HTML sayfaları
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── players.html
│ │ └── player_detail.html
│ │
│ └── static/ # JS / CSS / görseller
│ ├── css/
│ │ └── style.css
│ ├── js/
│ │ ├── players.js
│ │ └── charts.js
│ └── img/
│
├── ingest/ # veri çekme scriptleri
│ ├── ingest_fbref.py
│ └── update_stats.py
│
├── scripts/ # yardımcı scriptler
│ ├── create_db.py
│ └── cron_update.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md

python -m venv venv  
venv311\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

#Serveri Çalıştırmak için : uvicorn app.main:app --reload

#otomatik eposta için https://resend.com/ pip install resend python-dotenv

🔐 Giriş Sistemi (Login)

Bu projede email + tek kullanımlık kod (OTP) ile giriş sistemi kullanılmaktadır.
Email gönderimi için [Resend.com](https://resend.com/) servisi üzerinden alınan API anahtarı kullanılmaktadır.

✅ Mevcut Durum

Kullanıcı email adresini girer

Resend.com API ile 6 haneli OTP kodu gönderilir

Kod 5 dakika geçerlidir

Aynı login sayfası içinde:

Email alanı gizlenir

Kod giriş alanı ve sayaç gösterilir

Doğrulama başarılıysa:

HTTP-only cookie set edilir

Kullanıcı ana sayfaya yönlendirilir

Logout işleminde cookie silinir

🧠 Neden OTP?

Şifre saklanmaz

Basit ve hızlı kullanıcı deneyimi

MVP aşaması için yeterli güvenlik

🧩 dependencies.py Yapısı

Uygulama genelinde kullanılacak ortak güvenlik kontrolleri burada toplanır.

Sağladıkları:

Login kontrolü

Cookie veya (ileride) Bearer Token ile kullanıcı doğrulama

Domain kontrolü

API çağrıları yalnızca .env içindeki BASE_URL domain’inden kabul edilir

Bearer Token (JWT) taslağı

Şu an aktif değil, ileride kolayca açılacak şekilde hazır

🛡️ API Kullanımı

Endpoint’ler Depends() ile korunur

Örnek:

Sadece giriş yapan kullanıcı erişebilir

Domain dışı istekler otomatik engellenir

Router bazlı koruma ile tüm endpoint’ler tek seferde güvene alınabilir

🔜 İleride Planlanan

JWT (Bearer Token) ile tam API auth

Rate limiting (login ve API için)

API Key (public / partner erişimi)

Swagger üzerinden Bearer Auth desteği
