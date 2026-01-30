scout-platform/
│
├── app/ # FastAPI uygulaması
│ │
│ ├── main.py # FastAPI giriş noktası
│ │
│ ├── core/ # config & ayarlar
│ │ ├── config.py
│ │ └── database.py
│ │
│ ├── models/ # SQLAlchemy modelleri
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
│ │ ├──
│ │ ├──
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

#Serveri Çalıştırmak için : uvicorn app.main:app --reload
