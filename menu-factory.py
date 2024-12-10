from config import DevelopmentConfig
from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

ENV = os.getenv("FLASK_ENV", "development")

if ENV == "development":
    app.config.from_object(DevelopmentConfig)

client = MongoClient(app.config['MONGODB_URI'])
db = client[app.config['DB_NAME']]

print("run menu migration...")

db.menu.drop()
db.carts.drop()
db.wishlists.drop()
db.orders.drop()

doc = [
  {"image": "uploads/menu/favyasaka.jpg",
    "name": "Ayam Bakar Crispy", "price": 15000, "category" : "Ayam Spicy", "description" : "Nikmati kelezatan sempurna dari Ayam Bakar Crispy yang menggugah selera! Perpaduan unik antara daging ayam lembut yang dibakar dengan bumbu rempah khas dan kulit luar yang crispy memberikan sensasi rasa yang tak terlupakan. Disajikan dengan sambal pedas manis dan pelengkap segar seperti lalapan, menu ini cocok untuk Anda yang menginginkan hidangan spesial di setiap momen. Cocok disantap bersama keluarga atau teman-teman!"},
  {"image": "uploads/menu/chicken.jpg",
    "name": "Chicken + Nasi", "price": 20000, "category" : "Paket Hemat", "description" : "Nikmati hidangan lengkap dengan Chicken Crispy yang renyah di luar dan lembut di dalam, disajikan bersama nasi putih hangat yang pulen. Paket ini dilengkapi dengan sambal pilihan untuk sensasi rasa yang sempurna. Cocok untuk mengisi energi Anda kapan saja!"},
  {"image": "uploads/menu/mentai.jpg",
    "name": "Ayam Bakar Mentai + Nasi", "price": 15000, "category" : "Paket Hemat", "description" : "Hadirkan cita rasa unik dengan Ayam Mentai! Potongan ayam lembut yang dipadukan dengan saus mentai creamy bercita rasa gurih dan sedikit pedas, kemudian dipanggang hingga menghasilkan aroma yang menggoda. Disajikan dengan nasi hangat dan topping keju meleleh, menu ini siap memanjakan lidah Anda. Pilihan sempurna untuk penggemar hidangan modern yang kaya rasa!"},
  {"image": "uploads/menu/geprek.jpg",
    "name": "Ayam Geprek + Nasi", "price": 17000, "category" : "Paket Hemat", "description" : "Nikmati paket komplit yang penuh kenikmatan! Ayam Geprek dengan ayam crispy yang digeprek bersama sambal pedas khas, disajikan dengan nasi putih hangat yang pulen. Lengkapi pengalaman makan Anda dengan lalapan segar yang membuat setiap gigitan semakin sempurna. Pilihan pas untuk pencinta makanan pedas dan lezat!"},
  {"image": "uploads/menu/selimut.jpg",
    "name": "Ayam Selimut + Nasi", "price": 18000, "category" : "Paket Hemat", "description" : "Hadirkan pengalaman rasa baru dengan Ayam Selimut! Daging ayam yang juicy dibalut dengan lapisan kulit renyah dan dilumuri saus creamy spesial yang kaya rasa. Disajikan bersama nasi hangat dan pelengkap segar, menu ini memberikan kombinasi sempurna antara tekstur lembut, renyah, dan rasa gurih manis yang memanjakan lidah. Pilihan istimewa untuk setiap momen makan Anda!"},
  {"image": "uploads/menu/paket.jpg",
    "name": "Paket Extra Puas", "price": 17000, "category" : "Paket Hemat", "description" : "Puaskan selera makan Anda dengan Paket Extra Puas! Paket spesial ini terdiri dari ayam crispy yang renyah, nasi putih hangat, sambal pedas khas, serta tambahan lauk pilihan seperti telur dadar atau tahu dan tempe goreng. Tidak ketinggalan lalapan segar yang melengkapi kelezatannya. Cocok untuk Anda yang ingin porsi lebih besar dan rasa lebih puas!"},
  {"image": "uploads/menu/big.jpg",
    "name": "Chicken Big", "price": 65000, "category" : "Paket Hemat", "description" : "Rasakan kenikmatan maksimal dengan Chicken Big! Potongan ayam super besar yang juicy, dilapisi tepung berbumbu khas dan digoreng hingga renyah keemasan. Setiap gigitan menghadirkan kombinasi tekstur crispy di luar dan daging lembut di dalam. Cocok untuk Anda yang mencari porsi ekstra dengan rasa yang luar biasa nikmat!"},
  {"image": "uploads/menu/mala.jpg",
    "name": "Ayam Bakar Mala", "price": 20000, "category" : "Paket Hemat", "description" : "Siap untuk tantangan rasa? Ayam Mala hadir dengan sensasi pedas dan sedikit rasa pahit khas sambal mala yang menggugah selera! Potongan ayam crispy disiram dengan saus mala yang kaya rempah dan bumbu, memberikan rasa pedas menggigit dan aroma yang khas. Disajikan dengan nasi hangat, menu ini cocok bagi Anda yang suka tantangan rasa pedas yang luar biasa!"},
  {"image": "uploads/menu/sayap.jpg",
    "name": "Paket Winger", "price": 7500, "category" : "Paket Hemat", "description" : "Nikmati kelezatan yang penuh rasa dalam Paket Winger! Terdiri dari potongan sayap ayam yang dibumbui khas dan digoreng renyah, disajikan dengan nasi putih pulen, serta pilihan saus pendamping yang menggoda. Anda juga bisa memilih level pedas sesuai selera. Lengkap dengan pelengkap segar, paket ini siap memanjakan lidah Anda dalam setiap gigitan!"},
  {"image": "uploads/menu/nasi.jpg",
    "name": "Nasi Putih", "price": 3000, "category" : "Paket Hemat", "description" : "Hadirkan kelezatan dalam setiap suapan dengan Nasi hangat yang pulen. Disiapkan dengan sempurna untuk melengkapi hidangan Anda, nasi ini cocok disantap bersama berbagai lauk dan sambal pilihan. Menjadi pendamping yang pas untuk segala hidangan, memberi kenyamanan dan kepuasan setiap kali dinikmati."}
]

db.menu.insert_many(doc)

print("Migration Complete")