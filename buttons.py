from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests

main = KeyboardButton("🔝 Asosiy Menyu")
back = KeyboardButton("⬅️ Orqaga")

r = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json").json()

sura_name = []
for sura in r['chapters']:
    sura_name.append(sura['name'])
  
sura_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)

for i in range(len(sura_name)):
    sura_markup.insert(f"{i+1}.{sura_name[i]}")
    
sura_markup.add(main)

main_markup = ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.add(KeyboardButton("Umumiy izlash🔎"), KeyboardButton("Oyatlar"))
main_markup.add(KeyboardButton("Suradan izlash"), KeyboardButton("Sozlamalar"))
main_markup.add(KeyboardButton("Fikr bildirish✍️"))

oyatinfo = ReplyKeyboardMarkup(resize_keyboard=True)
oyatinfo.add(back, main)

