import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8662192303:AAHXmWUXXNEidYvHvOTEKbayw0mzG487-N0"
bot = telebot.TeleBot(TOKEN)

# Каталог товаров
GAMES = {
    "cs2": {
        "name": "🔫 CS2",
        "accounts": [
            {"name": "Silver Elite", "price": "500₽", "desc": "1200 часов, без банов"},
            {"name": "Gold Nova 3", "price": "800₽", "desc": "2000 часов, инвентарь"},
            {"name": "AK-47 Redline FT", "price": "300₽", "desc": "Скин Field-Tested"},
            {"name": "Нож Butterfly Safari Mesh", "price": "2500₽", "desc": "Редкий скин"},
        ]
    },
    "dota2": {
        "name": "🗡️ Dota 2",
        "accounts": [
            {"name": "Аккаунт 3000 MMR", "price": "600₽", "desc": "Стабильный рейтинг"},
            {"name": "Аккаунт 5000 MMR", "price": "1500₽", "desc": "Высокий рейтинг"},
            {"name": "Скин Arcana Pudge", "price": "1200₽", "desc": "Легендарный скин"},
            {"name": "Скин Persona Juggernaut", "price": "900₽", "desc": "Редкий образ"},
        ]
    },
    "valorant": {
        "name": "🎯 Valorant",
        "accounts": [
            {"name": "Аккаунт Silver", "price": "400₽", "desc": "Все агенты открыты"},
            {"name": "Аккаунт Platinum", "price": "1200₽", "desc": "Много скинов"},
            {"name": "Скин Phantom Prime", "price": "700₽", "desc": "Топовый скин"},
            {"name": "Скин Vandal RGX", "price": "800₽", "desc": "Эксклюзивный скин"},
        ]
    },
    "pubg": {
        "name": "🪂 PUBG",
        "accounts": [
            {"name": "Аккаунт Gold", "price": "500₽", "desc": "200+ побед"},
            {"name": "Скин Pan Frying", "price": "350₽", "desc": "Редкий скин сковороды"},
        ]
    },
    "fortnite": {
        "name": "🏗️ Fortnite",
        "accounts": [
            {"name": "Аккаунт OG скины", "price": "2000₽", "desc": "Редкие OG скины"},
            {"name": "Скин Skull Trooper", "price": "1500₽", "desc": "Легендарный скин"},
        ]
    },
    "warzone": {
        "name": "💥 Warzone",
        "accounts": [
            {"name": "Аккаунт с камуфляжами", "price": "700₽", "desc": "Много открытого"},
            {"name": "Скин Ghost", "price": "400₽", "desc": "Популярный оператор"},
        ]
    },
    "apex": {
        "name": "🦾 Apex Legends",
        "accounts": [
            {"name": "Аккаунт Diamond", "price": "900₽", "desc": "Высокий ранг"},
            {"name": "Скин Wraith Kunai", "price": "600₽", "desc": "Редкий скин"},
        ]
    },
    "lol": {
        "name": "⚔️ League of Legends",
        "accounts": [
            {"name": "Аккаунт Gold", "price": "700₽", "desc": "Все чемпионы"},
            {"name": "Скин Prestige", "price": "500₽", "desc": "Эксклюзивный скин"},
        ]
    },
    "minecraft": {
        "name": "⛏️ Minecraft",
        "accounts": [
            {"name": "Java аккаунт", "price": "300₽", "desc": "Лицензионный аккаунт"},
            {"name": "Java + Bedrock", "price": "500₽", "desc": "Два издания"},
        ]
    },
    "gta": {
        "name": "🚗 GTA Online",
        "accounts": [
            {"name": "Аккаунт 500 млн $", "price": "800₽", "desc": "Много денег в игре"},
            {"name": "Аккаунт MAX прокачка", "price": "1500₽", "desc": "Всё открыто"},
        ]
    },
}

def main_menu():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🎮 Каталог игр", callback_data="catalog"))
    kb.add(InlineKeyboardButton("ℹ️ О магазине", callback_data="about"))
    kb.add(InlineKeyboardButton("📞 Написать менеджеру", url="https://t.me/Res_Dark"))
    return kb

def catalog_menu():
    kb = InlineKeyboardMarkup()
    for key, game in GAMES.items():
        kb.add(InlineKeyboardButton(game["name"], callback_data=f"game_{key}"))
    kb.add(InlineKeyboardButton("🔙 Назад", callback_data="back_main"))
    return kb

def game_menu(game_key):
    game = GAMES[game_key]
    kb = InlineKeyboardMarkup()
    for i, item in enumerate(game["accounts"]):
        kb.add(InlineKeyboardButton(
            f"{item['name']} — {item['price']}",
            callback_data=f"buy_{game_key}_{i}"
        ))
    kb.add(InlineKeyboardButton("🔙 Назад к играм", callback_data="catalog"))
    return kb

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👾 Добро пожаловать в *CyberCrym Shop*!\n\n"
        "🔥 Продаём аккаунты и скины для топовых игр\n"
        "✅ Быстрая доставка\n"
        "✅ Гарантия на все товары\n"
        "✅ Лучшие цены\n\n"
        "Выбери раздел:",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda c: c.data == "catalog")
def catalog(call):
    bot.edit_message_text(
        "🎮 *Каталог игр*\n\nВыбери игру:",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=catalog_menu()
    )

@bot.callback_query_handler(func=lambda c: c.data == "back_main")
def back_main(call):
    bot.edit_message_text(
        "👾 *CyberCrym Shop*\n\nВыбери раздел:",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda c: c.data.startswith("game_"))
def show_game(call):
    game_key = call.data.replace("game_", "")
    game = GAMES[game_key]
    bot.edit_message_text(
        f"{game['name']}\n\n*Доступные товары:*",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=game_menu(game_key)
    )

@bot.callback_query_handler(func=lambda c: c.data.startswith("buy_"))
def buy_item(call):
    parts = call.data.split("_")
    game_key = parts[1]
    item_idx = int(parts[2])
    game = GAMES[game_key]
    item = game["accounts"][item_idx]

    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("💬 Купить / написать менеджеру", url="https://t.me/Res_Dark"))
    kb.add(InlineKeyboardButton("🔙 Назад", callback_data=f"game_{game_key}"))

    bot.edit_message_text(
        f"*{item['name']}*\n\n"
        f"💰 Цена: {item['price']}\n"
        f"📋 Описание: {item['desc']}\n\n"
        f"Нажми кнопку ниже чтобы связаться с менеджером и оформить заказ!",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=kb
    )

@bot.callback_query_handler(func=lambda c: c.data == "about")
def about(call):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 Назад", callback_data="back_main"))
    bot.edit_message_text(
        "ℹ️ *О магазине CyberCrym*\n\n"
        "Мы продаём аккаунты и скины для 10 популярных игр.\n\n"
        "✅ Гарантия на все товары\n"
        "✅ Быстрая передача после оплаты\n"
        "✅ Поддержка 24/7\n"
        "✅ Лучшие цены в Крыму\n\n"
        "📞 Менеджер: @Res_Dark",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=kb
    )

print("Бот запущен!")
bot.infinity_polling()
