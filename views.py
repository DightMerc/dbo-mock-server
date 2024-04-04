import uuid
from typing import Dict, Union, List

from aiohttp import web

from constants import PHONE, TOKEN, DUMMY_TEXT, DUMMY_URL, CARD_NUMBER, PAYEE_PHONE

mobile_v2 = web.RouteTableDef()


def prepare_response(body: Union[Dict, List, str]):
    result = {}
    result["result"] = True
    result["message"] = "Ok"
    result["error_code"] = 0
    result["data"] = body
    return web.json_response(data=result)


@mobile_v2.get("/api/mobile/v2/registration/code")
@mobile_v2.post("/api/mobile/v2/registration/code")
async def registration_code(_):
    body = {
        "account_number": 1,
        "device": 1,
        "phone": PHONE,
        "token": str(uuid.uuid4()),
        "refresh_token": str(uuid.uuid4()),
        "status": 1,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/registration/confirm/code")
@mobile_v2.post("/api/mobile/v2/registration/confirm/code")
async def registration_confirm_code(_):
    body = {
        "account_number": 1,
        "device": 1,
        "phone": PHONE,
        "token": TOKEN,
        "refresh_token": TOKEN,
        "status": 1,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/device/token")
@mobile_v2.post("/api/mobile/v2/device/token")
async def firebase_token(_):
    body = {"phone": PHONE, "result": DUMMY_TEXT}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/identification/authorize")
@mobile_v2.post("/api/mobile/v2/identification/authorize")
async def identification_passport(_):
    body = {"identification_request_id": TOKEN, "url": DUMMY_URL}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/account/identification/authorize/pinfl")
@mobile_v2.post("/api/mobile/v2/account/identification/authorize/pinfl")
async def identification_pinfl(_):
    body = {"identification_request_id": TOKEN, "url": DUMMY_URL}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/identification/verification")
@mobile_v2.post("/api/mobile/v2/identification/verification")
async def identification_check(_):
    body = {
        "birth_date": "1996-01-01",
        "fio": "JOHN DOE",
        "passport_num": "AA1234567",
        "pinfl": "12345678912345",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/account/limits_info")
@mobile_v2.post("/api/mobile/v2/account/limits_info")
async def limit_info(_):
    body = {"max": 100000000, "min": 100000}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/account/pass_data")
@mobile_v2.post("/api/mobile/v2/account/pass_data")
async def get_passport_data(_):
    body = {
        "birth_date": "1996-01-01",
        "fio": "JOHN DOE",
        "passport_num": "AA1234567",
        "pinfl": "12345678912345",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/offer/link")
@mobile_v2.post("/api/mobile/v2/offer/link")
async def get_oferta_link(_):
    body = {"offer": DUMMY_URL, "referral_offer": DUMMY_URL}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/identification/fields/list")
@mobile_v2.post("/api/mobile/v2/identification/fields/list")
async def get_identification_fields_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/identification/fields/update")
@mobile_v2.post("/api/mobile/v2/identification/fields/update")
async def update_identification_fields(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.post("/api/mobile/v2/login")
async def login(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/account/logout")
@mobile_v2.post("/api/mobile/v2/account/logout")
async def log_out(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.post("/api/mobile/v2/login/code")
async def login_code(_):
    body = {
        "account_number": 1,
        "device": 1,
        "phone": PHONE,
        "token": str(uuid.uuid4()),
        "refresh_token": str(uuid.uuid4()),
        "status": 1,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/token/{refresh_token}")
@mobile_v2.post("/api/mobile/v2/token/{refresh_token}")
async def refresh_token(_):
    body = {"token": TOKEN}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/list")
@mobile_v2.post("/api/mobile/v2/cards/list")
async def get_card_list(_):
    body = [
        {
            "is_standard": False,
            "bank": "AloqaBank",
            "type": "UZCARD",
            "token": "26785c3b7217f8a4a3b0c56e687985b5f0ade76f561f09b8c74cebcf5dc8e6b3",
            "expire": "0227",
            "fullName": "JOHN DOE",
            "status": 0,
            "balance": 1401234096,
            "card_number": "860031******5512",
            "is_main": True,
            "card_name": "Моя основная",
            "background_url": "https://cdn.garantbank.uz:60443/public/cards/backgrounds/image/back8.jpg",
            "humo_customer_id": None,
            "humo_masked_pan": None,
            "background_color_number": None,
            "linked": "LOCAL",
        },
        {
            "is_standard": False,
            "bank": "GARANTBANK",
            "type": "UZCARD",
            "token": "ecd93deb27c476528b07b0883d3204fb1eb147162a59cf976cc7024e1eb89db3",
            "expire": "0227",
            "fullName": "JOHN DOE",
            "status": 0,
            "balance": 6328,
            "card_number": "626296******0407",
            "is_main": True,
            "card_name": "Гарант",
            "background_url": "https://cdn.garantbank.uz:60443/public/cards/backgrounds/image/back7.jpg",
            "humo_customer_id": None,
            "humo_masked_pan": None,
            "background_color_number": None,
            "linked": "LOCAL",
        },
    ]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/registration")
@mobile_v2.post("/api/mobile/v2/cards/registration")
async def card_registration(_):
    body = {"id": TOKEN}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/registration/confirm")
@mobile_v2.post("/api/mobile/v2/cards/registration/confirm")
async def card_registration_confirm(_):
    body = {"card_token": TOKEN}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/registration/foreign")
@mobile_v2.post("/api/mobile/v2/cards/registration/foreign")
async def card_registration_foreign(_):
    body = {"id": TOKEN, "confirm_url": DUMMY_URL}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/card/info")
@mobile_v2.post("/api/mobile/v2/card/info")
async def card_info(_):
    body = "JOHN DOE"
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/remove")
@mobile_v2.post("/api/mobile/v2/cards/remove")
async def card_delete(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/main/set")
@mobile_v2.post("/api/mobile/v2/cards/main/set")
async def card_main_set(_):
    body = {}
    return prepare_response(body=body)


# TODO
@mobile_v2.get("/api/mobile/v2/cards/background_list")
@mobile_v2.post("/api/mobile/v2/cards/background_list")
async def card_background_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/set_background")
@mobile_v2.post("/api/mobile/v2/cards/set_background")
async def set_card_background_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/number")
@mobile_v2.post("/api/mobile/v2/cards/number")
async def get_card_full_number(_):
    body = {"holder": "JOHN DOE", "cardNumber": CARD_NUMBER}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/edit/card_name")
@mobile_v2.post("/api/mobile/v2/cards/edit/card_name")
async def update_card_name(_):
    body = {
        "is_standard": False,
        "bank": "GARANTBANK",
        "type": "UZCARD",
        "token": "ecd93deb27c476528b07b0883d3204fb1eb147162a59cf976cc7024e1eb89db3",
        "expire": "0227",
        "fullName": "JOHN DOE",
        "status": 0,
        "balance": 6328,
        "card_number": "626296******0407",
        "is_main": True,
        "card_name": "Гарант",
        "background_url": "https://cdn.garantbank.uz:60443/public/cards/backgrounds/image/back7.jpg",
        "humo_customer_id": None,
        "humo_masked_pan": None,
        "background_color_number": None,
        "linked": "LOCAL",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/type")
@mobile_v2.post("/api/mobile/v2/cards/type")
async def card_type(_):
    body = {"bank": "KAPITALBANK", "type": "UZCARD"}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/show_in_search/status")
@mobile_v2.post("/api/mobile/v2/cards/show_in_search/status")
async def cardsshowinsearchstatus(_):
    body = {"enable": True}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/show_in_search/change")
@mobile_v2.post("/api/mobile/v2/cards/show_in_search/change")
async def cardsshowinsearchchange(_):
    body = {"enable": 1}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/verify/accounts")
@mobile_v2.post("/api/mobile/v2/verify/accounts")
async def get_contact_list(_):
    body = [{"phone": PHONE, "active": True}]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/wallet/transfer")
@mobile_v2.post("/api/mobile/v2/wallet/transfer")
async def wallet_transfer(_):
    body = {
        "transaction_id": "123",
        "amount": 100000,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/wallet/pre_transfer")
@mobile_v2.post("/api/mobile/v2/wallet/pre_transfer")
async def wallet_pre_transfer(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/wallet/balance")
@mobile_v2.post("/api/mobile/v2/wallet/balance")
async def wallet_balance(_):
    body = {
        "available": 100000000,
        "currency": 860,
        "frozen": 0,
        "hold": 0,
        "account_number": "123",
        "bcu": 33000000,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/categories")
@mobile_v2.post("/api/mobile/v2/vendors/categories")
async def get_categories(_):
    body = [
        {
            "id": 1,
            "logo": "https://cdn.hordor.uz/vendors/categories/mobile.png",
            "value": 1,
            "order_no": 1,
            "title": "Мобильные операторы",
        },
        {
            "id": 6,
            "logo": "https://cdn.hordor.uz/vendors/categories/services.png",
            "value": 6,
            "order_no": 2,
            "title": "Коммунальные услуги",
        },
        {
            "id": 2,
            "logo": "https://cdn.hordor.uz/vendors/categories/internet.png",
            "value": 2,
            "order_no": 3,
            "title": "Интернет-провайдеры",
        },
        {
            "id": 4,
            "logo": "https://cdn.hordor.uz/vendors/categories/credits.png",
            "value": 4,
            "order_no": 4,
            "title": "Погашение кредитов",
        },
        {
            "id": 22,
            "logo": "https://cdn.hordor.uz/vendors/categories/budget.png",
            "value": 22,
            "order_no": 5,
            "title": "Бюджетные платежи",
        },
        {
            "id": 19,
            "logo": "https://cdn.hordor.uz/vendors/categories/education.png",
            "value": 19,
            "order_no": 6,
            "title": "Обучение",
        },
        {
            "id": 13,
            "logo": "https://cdn.hordor.uz/vendors/categories/games.png",
            "value": 13,
            "order_no": 7,
            "title": "Игры и социальные сети",
        },
        {
            "id": 14,
            "logo": "https://cdn.hordor.uz/vendors/categories/online.png",
            "value": 14,
            "order_no": 8,
            "title": "Онлайн-сервисы",
        },
        {
            "id": 7,
            "logo": "https://cdn.hordor.uz/vendors/categories/tv.png",
            "value": 7,
            "order_no": 9,
            "title": "Телевидение и онлайн-вещание",
        },
        {
            "id": 10,
            "logo": "https://cdn.hordor.uz/vendors/categories/charity.png",
            "value": 10,
            "order_no": 10,
            "title": "Благотворительность",
        },
        {
            "id": 12,
            "logo": "https://cdn.hordor.uz/vendors/categories/ecom.png",
            "value": 12,
            "order_no": 11,
            "title": "Интернет-магазины",
        },
        {
            "id": 21,
            "logo": "https://cdn.hordor.uz/vendors/categories/taxi.png",
            "value": 21,
            "order_no": 12,
            "title": "Такси",
        },
        {
            "id": 20,
            "logo": "https://cdn.hordor.uz/vendors/categories/other.png",
            "value": 20,
            "order_no": 1000,
            "title": "Другое",
        },
    ]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/categories/vendors")
@mobile_v2.post("/api/mobile/v2/vendors/categories/vendors")
async def get_vendors_by_category_id(_):
    body = [
        {
            "sub_category_id": 1,
            "sub_category_title": "Национальные операторы",
            "vendors": [
                {
                    "id": 101772,
                    "category": 1,
                    "name": "OOO UNITEL",
                    "short_name": "Beeline ",
                    "logo": "https://cdn.hordor.uz/vendors/logo/101772.png",
                    "url": "https://beeline.uz",
                    "disabled": False,
                    "latest_payment": "03.04.2024",
                },
                {
                    "id": 101904,
                    "category": 1,
                    "name": "Ф-л UZMOBILE АК Узбектелеком",
                    "short_name": "UzMobile ",
                    "logo": "https://cdn.hordor.uz/vendors/logo/101904.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 101906,
                    "category": 1,
                    "name": "ИП OOO RWC (Perfectum)",
                    "short_name": "Perfectum ",
                    "logo": "https://cdn.hordor.uz/vendors/logo/101906.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
            ],
        },
        {
            "sub_category_id": 2,
            "sub_category_title": "Операторы России",
            "vendors": [
                {
                    "id": 103029,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "MATRIX Mobile Россия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103029.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103035,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Волна Россия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103035.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103021,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Goodline Россия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103021.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103019,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Simtravel Россия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103019.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103037,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Seven Sky Россия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103037.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
            ],
        },
        {
            "sub_category_id": 4,
            "sub_category_title": "Операторы других стран",
            "vendors": [
                {
                    "id": 102939,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Билайн Кыргызстан",
                    "logo": "https://cdn.hordor.uz/vendors/logo/102939.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103015,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "O-MOBILE Таджикистан",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103015.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103043,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Magticom Грузия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103043.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 102953,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Билайн Грузия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/102953.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 102957,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "GlobalCell Грузия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/102957.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 102955,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "GeoCell Грузия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/102955.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103039,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "My Profile RUB Грузия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103039.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103041,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "bani Грузия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103041.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103025,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Aquafon Абхазия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103025.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103027,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "а-мобаил Абхазия",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103027.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103051,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Etisalat Афганистан",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103051.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103053,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "MTN Афганистан",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103053.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103055,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Roshan Афганистан",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103055.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103059,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Salaam Афганистан",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103059.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103023,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "United Mobile Payment",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103023.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103031,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "База Мобильная",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103031.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103057,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Восточный Экспресс",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103057.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103061,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Airtel Бангладеш",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103061.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103063,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Banglalink Бангладеш",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103063.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103065,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "GrameenPhone Бангладеш",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103065.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103067,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Robi Axiata Бангладеш",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103067.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103069,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Orange Ботсвана",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103069.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103071,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Anguilla Ангилья",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103071.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103073,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Anguilla and Barbuda AG",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103073.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103075,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Digicel Барбадос",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103075.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
                {
                    "id": 103077,
                    "category": 1,
                    "name": "OOO BRIO GROUP",
                    "short_name": "Lime Барбадос",
                    "logo": "https://cdn.hordor.uz/vendors/logo/103077.png",
                    "url": "https://paynet.uz/services",
                    "disabled": False,
                    "latest_payment": None,
                },
            ],
        },
    ]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/search")
@mobile_v2.post("/api/mobile/v2/vendors/search")
async def vendors_search(_):
    body = [
        {
            "id": 101772,
            "category": 1,
            "name": "OOO UNITEL",
            "short_name": "Beeline ",
            "logo": "https://cdn.hordor.uz/vendors/logo/101772.png",
            "url": "https://beeline.uz",
            "disabled": False,
            "latest_payment": "03.04.2024",
        },
        {
            "id": 102939,
            "category": 1,
            "name": "OOO BRIO GROUP",
            "short_name": "Билайн Кыргызстан",
            "logo": "https://cdn.hordor.uz/vendors/logo/102939.png",
            "url": "https://paynet.uz/services",
            "disabled": False,
            "latest_payment": None,
        },
        {
            "id": 102953,
            "category": 1,
            "name": "OOO BRIO GROUP",
            "short_name": "Билайн Грузия",
            "logo": "https://cdn.hordor.uz/vendors/logo/102953.png",
            "url": "https://paynet.uz/services",
            "disabled": False,
            "latest_payment": None,
        },
    ]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/info")
@mobile_v2.post("/api/mobile/v2/vendors/info")
async def vendor_info(_):
    body = {
        "vendor_form": [
            {
                "label": "Номер телефона",
                "key": "phone_number",
                "element": "input",
                "type": "int",
                "value": "",
                "show": 1,
                "mask": "## ### ## ##",
                "prefix": "+998",
                "regex": "^(90|91)[0-9]{7}$",
                "placeholder": "",
                "size": 9,
                "order": 10,
                "is_required": 1,
            },
            {
                "label": "Сумма",
                "key": "summa",
                "element": "input",
                "type": "int",
                "value": "",
                "show": 1,
                "mask": "",
                "prefix": "",
                "regex": "^[\\d\\.]+$",
                "placeholder": "",
                "size": 0,
                "amount_type": "UZS",
                "min_amount": 1000,
                "max_amount": 1500000,
                "order": 20,
                "is_required": 1,
            },
            {
                "key": "vendor_id",
                "value": 101772,
                "show": 0,
                "is_required": 1,
                "account_field": "phone_number",
                "amount_field": "summa",
            },
        ],
        "request_method": "pam.check",
        "description": "",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/info/by_id")
@mobile_v2.post("/api/mobile/v2/vendors/info/by_id")
async def vendor_info_by_id(_):
    body = {
        "category": 1,
        "id": 101772,
        "logo": "https://cdn.hordor.uz/vendors/logo/101772.png",
        "name": "OOO UNITEL",
        "short_name": "Beeline ",
        "url": "https://beeline.uz",
        "vendor_form": [
            {
                "label": "Номер телефона",
                "key": "phone_number",
                "element": "input",
                "type": "int",
                "value": "",
                "show": 1,
                "mask": "## ### ## ##",
                "prefix": "+998",
                "regex": "^(90|91)[0-9]{7}$",
                "placeholder": "",
                "size": 9,
                "order": 10,
                "is_required": 1,
            },
            {
                "label": "Сумма",
                "key": "summa",
                "element": "input",
                "type": "int",
                "value": "",
                "show": 1,
                "mask": "",
                "prefix": "",
                "regex": "^[\\d\\.]+$",
                "placeholder": "",
                "size": 0,
                "amount_type": "UZS",
                "min_amount": 1000,
                "max_amount": 1500000,
                "order": 20,
                "is_required": 1,
            },
            {
                "key": "vendor_id",
                "value": 101772,
                "show": 0,
                "is_required": 1,
                "account_field": "phone_number",
                "amount_field": "summa",
            },
        ],
        "category_title": "Национальные операторы",
        "description": "",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/repeat/vendor")
@mobile_v2.post("/api/mobile/v2/transactions/repeat/vendor")
async def repeat_payment(_):
    body = {
        "category": 1,
        "id": 101772,
        "logo": "https://cdn.hordor.uz/vendors/logo/101772.png",
        "name": "OOO UNITEL",
        "short_name": "Beeline ",
        "url": "https://beeline.uz",
        "vendor_form": [
            {
                "label": "Номер телефона",
                "key": "phone_number",
                "element": "input",
                "type": "int",
                "value": "901234567",
                "show": 1,
                "mask": "## ### ## ##",
                "prefix": "+998",
                "regex": "^(90|91)[0-9]{7}$",
                "placeholder": "",
                "size": 9,
                "order": 10,
                "is_required": 1,
            },
            {
                "label": "Сумма",
                "key": "summa",
                "element": "input",
                "type": "int",
                "value": "1000",
                "show": 1,
                "mask": "",
                "prefix": "",
                "regex": "^[\\d\\.]+$",
                "placeholder": "",
                "size": 0,
                "amount_type": "UZS",
                "min_amount": 1000,
                "max_amount": 1500000,
                "order": 20,
                "is_required": 1,
            },
            {
                "key": "vendor_id",
                "value": 101772,
                "show": 0,
                "is_required": 1,
                "account_field": "phone_number",
                "amount_field": "summa",
            },
        ],
        "category_title": "Национальные операторы",
        "description": "",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/repeat/w2w")
@mobile_v2.post("/api/mobile/v2/transactions/repeat/w2w")
async def repeat_w2w(_):
    body = {"amount": 1000000, "payee": PAYEE_PHONE}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/splitted/check")
@mobile_v2.post("/api/mobile/v2/vendors/splitted/check")
async def vendor_check(_):
    body = {
        "payment_info": {"wallet": 0, "card": 100000, "splitted": False},
        "check_result": [
            {
                "additional_form": [
                    {
                        "label": "Номер телефона",
                        "key": "phone_number",
                        "value": "90 962 52 88",
                        "show": 1,
                        "is_required": 0,
                    },
                    {
                        "label": "Сумма к получению",
                        "key": "vendor_receive_amount",
                        "value": "1 000,00 UZS",
                        "show": 1,
                        "is_required": 0,
                    },
                ]
            }
        ],
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/balance")
@mobile_v2.post("/api/mobile/v2/vendors/balance")
async def vendor_balance(_):
    body = {"available": False, "balance": 0}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/payment/prepare")
@mobile_v2.post("/api/mobile/v2/vendors/payment/prepare")
async def vendor_payment_prepare(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Номер телефона", "value": "901234567"},
            {"string": "Сумма платежа", "value": "1 000,00 UZS"},
            {"string": "Комиссия", "value": "0,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:52:06"},
            {"string": "ID транзакции", "value": "736336"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "vendor",
        "transaction_group": "vendor",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/payment/perform")
@mobile_v2.post("/api/mobile/v2/vendors/payment/perform")
async def vendor_payment_perform(_):
    body = {
        "transaction_id": "123",
        "amount": 100000,
        "info": [
            {"string": "Номер телефона", "value": "901234567"},
            {"string": "Сумма платежа", "value": "1 000,00 UZS"},
            {"string": "Комиссия", "value": "0,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:52:06"},
            {"string": "ID транзакции", "value": "736336"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "vendor",
        "transaction_group": "vendor",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/payment/by_token/prepare")
@mobile_v2.post("/api/mobile/v2/vendors/payment/by_token/prepare")
async def vendor_pay_prepare_with_card(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Номер телефона", "value": "901234567"},
            {"string": "Сумма платежа", "value": "1 000,00 UZS"},
            {"string": "Комиссия", "value": "0,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:52:06"},
            {"string": "ID транзакции", "value": "736336"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "vendor",
        "transaction_group": "vendor",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/payment/by_token/perform")
@mobile_v2.post("/api/mobile/v2/vendors/payment/by_token/perform")
async def vendor_pay_perform_with_card(_):
    body = {
        "transaction_id": "123",
        "amount": 100000,
        "info": [
            {"string": "Номер телефона", "value": "901234567"},
            {"string": "Сумма платежа", "value": "1 000,00 UZS"},
            {"string": "Комиссия", "value": "0,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:52:06"},
            {"string": "ID транзакции", "value": "736336"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "vendor",
        "transaction_group": "vendor",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/deposit/create")
@mobile_v2.post("/api/mobile/v2/deposit/create")
async def deposit_create(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Номер телефона", "value": "901234567"},
            {"string": "Сумма платежа", "value": "1 000,00 UZS"},
            {"string": "Комиссия", "value": "0,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:52:06"},
            {"string": "ID транзакции", "value": "736336"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "deposit",
        "transaction_group": "deposit",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/deposit/confirm")
@mobile_v2.post("/api/mobile/v2/deposit/confirm")
async def deposit_confirm(_):
    body = {
        "transaction_id": "123",
        "amount": 100000,
        "info": [
            {"string": "Номер телефона", "value": "901234567"},
            {"string": "Сумма платежа", "value": "1 000,00 UZS"},
            {"string": "Комиссия", "value": "0,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:52:06"},
            {"string": "ID транзакции", "value": "736336"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "deposit",
        "transaction_group": "deposit",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/repeat/deposit")
@mobile_v2.post("/api/mobile/v2/transactions/repeat/deposit")
async def repeat_deposit(_):
    body = {"amount": 1000000, "payee": PAYEE_PHONE}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/payment/foreign/course")
@mobile_v2.post("/api/mobile/v2/vendors/payment/foreign/course")
async def foreign_course(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/card/token/pre_transfer")
@mobile_v2.post("/api/mobile/v2/p2p/card/token/pre_transfer")
async def p2p_pre_transfer_lc_c(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/card/token/transfer")
@mobile_v2.post("/api/mobile/v2/p2p/card/token/transfer")
async def p2p_transfer_lc_c(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/card/by_card_id/pre_transfer")
@mobile_v2.post("/api/mobile/v2/p2p/card/by_card_id/pre_transfer")
async def p2p_pre_transfer_lc_ci(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/card/by_card_id/transfer")
@mobile_v2.post("/api/mobile/v2/p2p/card/by_card_id/transfer")
async def p2p_transfer_lc_ci(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/card/by_id/pre_transfer")
@mobile_v2.post("/api/mobile/v2/p2p/card/by_id/pre_transfer")
async def p2p_pre_transfer_lc_lc(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/card/by_id/transfer")
@mobile_v2.post("/api/mobile/v2/p2p/card/by_id/transfer")
async def p2p_transfer_lc_lc(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/wallet/pre_transfer")
@mobile_v2.post("/api/mobile/v2/p2p/wallet/pre_transfer")
async def p2p_pre_wallet_unknown(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/wallet/transfer")
@mobile_v2.post("/api/mobile/v2/p2p/wallet/transfer")
async def p2p_wallet_unknown(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/wallet/to_id/pre_transfer")
@mobile_v2.post("/api/mobile/v2/p2p/wallet/to_id/pre_transfer")
async def p2p_pre_wallet_connected(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/wallet/to_id/transfer")
@mobile_v2.post("/api/mobile/v2/p2p/wallet/to_id/transfer")
async def p2p_wallet_connected(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/bounds")
@mobile_v2.post("/api/mobile/v2/transactions/bounds")
async def transaction_bounds(_):
    body = {"max": 100000000, "min": 100000}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/wallet/by_card_id/pre_transfer")
@mobile_v2.post("/api/mobile/v2/p2p/wallet/by_card_id/pre_transfer")
async def p2p_pre_wallet_card_id(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
        "is_otp": True,
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/wallet/by_card_id/transfer")
@mobile_v2.post("/api/mobile/v2/p2p/wallet/by_card_id/transfer")
async def p2p_wallet_card_id(_):
    body = {
        "transaction_id": 123,
        "info": [
            {"string": "Карта получателя", "value": "9860 14** **** 0036"},
            {"string": "Сумма перевода", "value": "3 000,00 UZS"},
            {"string": "Комиссия", "value": "15,00 UZS"},
            {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
            {"string": "Комментарий (его видите только вы)", "value": "Test"},
            {"string": "Номер терминала", "value": "91600126"},
            {"string": "ID транзакции", "value": "736334"},
            {"string": "Источник перевода", "value": "Моя основная **5512"},
        ],
        "transaction_type": "p2p",
        "transaction_group": "p2p",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/repeat/p2p")
@mobile_v2.post("/api/mobile/v2/transactions/repeat/p2p")
async def p2p_repeat(_):
    body = {
        "amount": 100000,
        "full_name": "JOHN DOE",
        "masked_card_number": "860031******4117",
        "method": "by_number",
        "payee": "8600312916504117",
        "card_type": "UZCARD",
    }
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/card/try")
@mobile_v2.post("/api/mobile/v2/p2p/card/try")
async def p2p_commission(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/wallet/try")
@mobile_v2.post("/api/mobile/v2/p2p/wallet/try")
async def p2p_wallet_commission(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/latest/field/values")
@mobile_v2.post("/api/mobile/v2/vendors/latest/field/values")
async def vendor_latest_values(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/account/passport_open_data")
@mobile_v2.post("/api/mobile/v2/account/passport_open_data")
async def account_open_data(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/limits/check")
@mobile_v2.post("/api/mobile/v2/transactions/limits/check")
async def limits_check(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/list")
@mobile_v2.post("/api/mobile/v2/transactions/list")
async def transaction_list(_):
    body = [
        {
            "id": "736336",
            "amount": 100000,
            "date": "Wed, 03 Apr 2024 07:52:06 GMT",
            "type": 8,
            "refill": False,
            "logo": "https://cdn.hordor.uz/vendors/logo/101772.png",
            "payer": "8600 31** **** 5512",
            "payee": "Beeline",
            "status": 2,
            "info": [
                {"string": "Номер телефона", "value": "901234567"},
                {"string": "Сумма платежа", "value": "1 000,00 UZS"},
                {"string": "Комиссия", "value": "0,00 UZS"},
                {"string": "Дата и время транзакции", "value": "03-04-2024 12:52:06"},
                {"string": "ID транзакции", "value": "736336"},
                {"string": "Источник перевода", "value": "Моя основная **5512"},
            ],
            "is_starred": False,
        },
        {
            "id": "736334",
            "amount": 301500,
            "date": "Wed, 03 Apr 2024 07:49:06 GMT",
            "type": 3,
            "refill": False,
            "logo": "https://cdn.garantbank.uz:60443/public/vendors/categories/p2p-own.png",
            "payer": "8600 31** **** 5512",
            "payee": "9860 14** **** 0036",
            "status": 2,
            "info": [
                {"string": "Карта получателя", "value": "9860 14** **** 0036"},
                {"string": "Сумма перевода", "value": "3 000,00 UZS"},
                {"string": "Комиссия", "value": "15,00 UZS"},
                {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
                {"string": "Комментарий (его видите только вы)", "value": "Test"},
                {"string": "Номер терминала", "value": "91600126"},
                {"string": "ID транзакции", "value": "736334"},
                {"string": "Источник перевода", "value": "Моя основная **5512"},
            ],
            "is_starred": False,
        },
        {
            "id": "736322",
            "amount": 100000,
            "date": "Thu, 28 Mar 2024 12:11:38 GMT",
            "type": 8,
            "refill": False,
            "logo": "https://cdn.hordor.uz/vendors/logo/101772.png",
            "payer": "8600 31** **** 5512",
            "payee": "Beeline",
            "status": 2,
            "info": [
                {"string": "Номер телефона", "value": "901234567"},
                {"string": "Сумма платежа", "value": "1 000,00 UZS"},
                {"string": "Комиссия", "value": "0,00 UZS"},
                {"string": "Дата и время транзакции", "value": "28-03-2024 17:11:38"},
                {"string": "ID транзакции", "value": "736322"},
                {"string": "Источник перевода", "value": "Моя основная **5512"},
            ],
            "is_starred": False,
        },
        {
            "id": "736315",
            "amount": 100500,
            "date": "Tue, 26 Mar 2024 09:00:43 GMT",
            "type": 3,
            "refill": False,
            "logo": "https://cdn.garantbank.uz:60443/public/vendors/categories/p2p-own.png",
            "payer": "8600 31** **** 5512",
            "payee": "6262 96** **** 0407",
            "status": 2,
            "info": [
                {"string": "Карта получателя", "value": "6262 96** **** 0407"},
                {"string": "Сумма перевода", "value": "1 000,00 UZS"},
                {"string": "Комиссия", "value": "5,00 UZS"},
                {"string": "Дата и время транзакции", "value": "26-03-2024 14:00:43"},
                {"string": "Комментарий (его видите только вы)", "value": "test\n\n"},
                {"string": "Номер терминала", "value": "91600261"},
                {"string": "ID транзакции", "value": "736315"},
                {"string": "Источник перевода", "value": "Моя основная **5512"},
            ],
            "is_starred": False,
        },
    ]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/list/by_card")
@mobile_v2.post("/api/mobile/v2/transactions/list/by_card")
async def transaction_list_by_card(_):
    body = [
        {
            "id": "736336",
            "amount": 100000,
            "date": "Wed, 03 Apr 2024 07:52:06 GMT",
            "type": 8,
            "refill": False,
            "logo": "https://cdn.hordor.uz/vendors/logo/101772.png",
            "payer": "8600 31** **** 5512",
            "payee": "Beeline",
            "status": 2,
            "info": [
                {"string": "Номер телефона", "value": "901234567"},
                {"string": "Сумма платежа", "value": "1 000,00 UZS"},
                {"string": "Комиссия", "value": "0,00 UZS"},
                {"string": "Дата и время транзакции", "value": "03-04-2024 12:52:06"},
                {"string": "ID транзакции", "value": "736336"},
                {"string": "Источник перевода", "value": "Моя основная **5512"},
            ],
            "is_starred": False,
        },
        {
            "id": "736334",
            "amount": 301500,
            "date": "Wed, 03 Apr 2024 07:49:06 GMT",
            "type": 3,
            "refill": False,
            "logo": "https://cdn.garantbank.uz:60443/public/vendors/categories/p2p-own.png",
            "payer": "8600 31** **** 5512",
            "payee": "9860 14** **** 0036",
            "status": 2,
            "info": [
                {"string": "Карта получателя", "value": "9860 14** **** 0036"},
                {"string": "Сумма перевода", "value": "3 000,00 UZS"},
                {"string": "Комиссия", "value": "15,00 UZS"},
                {"string": "Дата и время транзакции", "value": "03-04-2024 12:49:06"},
                {"string": "Комментарий (его видите только вы)", "value": "Test"},
                {"string": "Номер терминала", "value": "91600126"},
                {"string": "ID транзакции", "value": "736334"},
                {"string": "Источник перевода", "value": "Моя основная **5512"},
            ],
            "is_starred": False,
        },
        {
            "id": "736322",
            "amount": 100000,
            "date": "Thu, 28 Mar 2024 12:11:38 GMT",
            "type": 8,
            "refill": False,
            "logo": "https://cdn.hordor.uz/vendors/logo/101772.png",
            "payer": "8600 31** **** 5512",
            "payee": "Beeline",
            "status": 2,
            "info": [
                {"string": "Номер телефона", "value": "901234567"},
                {"string": "Сумма платежа", "value": "1 000,00 UZS"},
                {"string": "Комиссия", "value": "0,00 UZS"},
                {"string": "Дата и время транзакции", "value": "28-03-2024 17:11:38"},
                {"string": "ID транзакции", "value": "736322"},
                {"string": "Источник перевода", "value": "Моя основная **5512"},
            ],
            "is_starred": False,
        },
        {
            "id": "736315",
            "amount": 100500,
            "date": "Tue, 26 Mar 2024 09:00:43 GMT",
            "type": 3,
            "refill": False,
            "logo": "https://cdn.garantbank.uz:60443/public/vendors/categories/p2p-own.png",
            "payer": "8600 31** **** 5512",
            "payee": "6262 96** **** 0407",
            "status": 2,
            "info": [
                {"string": "Карта получателя", "value": "6262 96** **** 0407"},
                {"string": "Сумма перевода", "value": "1 000,00 UZS"},
                {"string": "Комиссия", "value": "5,00 UZS"},
                {"string": "Дата и время транзакции", "value": "26-03-2024 14:00:43"},
                {"string": "Комментарий (его видите только вы)", "value": "test\n\n"},
                {"string": "Номер терминала", "value": "91600261"},
                {"string": "ID транзакции", "value": "736315"},
                {"string": "Источник перевода", "value": "Моя основная **5512"},
            ],
            "is_starred": False,
        },
    ]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/details")
@mobile_v2.post("/api/mobile/v2/transactions/details")
async def download_check(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transaction/details/p2p")
@mobile_v2.post("/api/mobile/v2/transaction/details/p2p")
async def download_check_p2p(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transaction/detail")
@mobile_v2.post("/api/mobile/v2/transaction/detail")
async def transaction_detail(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/payment_mobile/info")
@mobile_v2.post("/api/mobile/v2/vendors/payment_mobile/info")
async def get_info_my_phone(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vendors/payment_mobile/pay")
@mobile_v2.post("/api/mobile/v2/vendors/payment_mobile/pay")
async def pay_my_phone(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/account/fio")
@mobile_v2.post("/api/mobile/v2/account/fio")
async def account_fio(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/notifications/list")
@mobile_v2.post("/api/mobile/v2/notifications/list")
async def notification_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/notifications/mark")
@mobile_v2.post("/api/mobile/v2/notifications/mark")
async def notification_mark(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/notifications/active")
@mobile_v2.post("/api/mobile/v2/notifications/active")
async def notification_active(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/notifications/details")
@mobile_v2.post("/api/mobile/v2/notifications/details")
async def notification_detail(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/notifications/count/unread")
@mobile_v2.post("/api/mobile/v2/notifications/count/unread")
async def notification_unread_count(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/core/version")
@mobile_v2.post("/api/mobile/v2/core/version")
async def update_version(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/onboarding/get")
@mobile_v2.post("/api/mobile/v2/onboarding/get")
async def get_onboarding(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/devices/trusted/list")
@mobile_v2.post("/api/mobile/v2/devices/trusted/list")
async def device_trusted_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/devices/trusted/disable")
@mobile_v2.post("/api/mobile/v2/devices/trusted/disable")
async def device_trusted_disable(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/devices/trusted/disable/all")
@mobile_v2.post("/api/mobile/v2/devices/trusted/disable/all")
async def device_all_disable(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/account/change_language")
@mobile_v2.post("/api/mobile/v2/account/change_language")
async def change_language(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/banners/list")
@mobile_v2.post("/api/mobile/v2/banners/list")
async def banner_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/events/metrics/push")
@mobile_v2.post("/api/mobile/v2/events/metrics/push")
async def report_event(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/identification/application/create")
@mobile_v2.post("/api/mobile/v2/identification/application/create")
async def identificationcreate(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/identification/application/check")
@mobile_v2.post("/api/mobile/v2/identification/application/check")
async def identificationcheck(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/identification/application/submit")
@mobile_v2.post("/api/mobile/v2/identification/application/submit")
async def identificationsubmit(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/sdk/identification/authorize")
@mobile_v2.post("/api/mobile/v2/sdk/identification/authorize")
async def sdk_identification_auth(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/accounts/ident/level")
@mobile_v2.post("/api/mobile/v2/accounts/ident/level")
async def account_ident_level(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/otp/send")
@mobile_v2.post("/api/mobile/v2/transactions/otp/send")
async def otp_send(_):
    body = {"code_id": TOKEN}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/otp/resend")
@mobile_v2.post("/api/mobile/v2/transactions/otp/resend")
async def otp_resend(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/otp/check")
@mobile_v2.post("/api/mobile/v2/transactions/otp/check")
async def otp_check(_):
    body = {"result": 1}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/otp/auto/check")
@mobile_v2.post("/api/mobile/v2/transactions/otp/auto/check")
async def otp_auto_check(_):
    body = {"result": 1}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/referral/tasks")
@mobile_v2.post("/api/mobile/v2/referral/tasks")
async def referral_tasks(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/referral/link_account")
@mobile_v2.post("/api/mobile/v2/referral/link_account")
async def referral_link_account(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/referral/referred_accounts")
@mobile_v2.post("/api/mobile/v2/referral/referred_accounts")
async def referred_accounts(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/referral/receive_invite_friend_bonus")
@mobile_v2.post("/api/mobile/v2/referral/receive_invite_friend_bonus")
async def referred_friend_bonus(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/campaigns/status/change")
@mobile_v2.post("/api/mobile/v2/campaigns/status/change")
async def campaigns_status_change(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/campaigns/status")
@mobile_v2.post("/api/mobile/v2/campaigns/status")
async def campaigns_status(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/humopay/register")
@mobile_v2.post("/api/mobile/v2/transactions/humopay/register")
async def humo_pay_transaction_register(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/p2p/recent_payee/list")
@mobile_v2.post("/api/mobile/v2/p2p/recent_payee/list")
async def recent_payee_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/info/by_card_hash")
@mobile_v2.post("/api/mobile/v2/cards/info/by_card_hash")
async def get_card_info_by_hash(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/feature_flags/list")
@mobile_v2.post("/api/mobile/v2/feature_flags/list")
async def feature_flags(_):
    body = [
        {
            "title": "notification",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "banners",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "loyalty",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "nfc",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "vendorinput",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "towallet",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "showinsearch",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "favouritesettings",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "starred_payments",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "add_p2p_to_fav_main",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "history_favourites_p2p",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "ask_for_money",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "russian_numbers",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "push_checkbox",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "invest",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
        {
            "title": "bookhara_aviatickets",
            "description": "колокольчик на главном экране",
            "attributes": {"visible": True},
        },
    ]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/deposit/card_to_wallet/token/create")
@mobile_v2.post("/api/mobile/v2/deposit/card_to_wallet/token/create")
async def depositcardtowallettokencreate(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/deposit/card_to_wallet/token/confirm")
@mobile_v2.post("/api/mobile/v2/deposit/card_to_wallet/token/confirm")
async def depositcardtowallettokenconfirm(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cards/by_phone")
@mobile_v2.post("/api/mobile/v2/cards/by_phone")
async def cards_by_phone(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/transactions/pay_methods")
@mobile_v2.post("/api/mobile/v2/transactions/pay_methods")
async def transaction_pay_methods(_):
    body = ["local-uzcard", "local-humo"]
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cashback/p2p/account_levels")
@mobile_v2.post("/api/mobile/v2/cashback/p2p/account_levels")
async def p2p_bonus_account_levels(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cashback/p2p/account_avatars")
@mobile_v2.post("/api/mobile/v2/cashback/p2p/account_avatars")
async def p2p_bonus_account_avatars(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/cashback/p2p/account_transactions")
@mobile_v2.post("/api/mobile/v2/cashback/p2p/account_transactions")
async def p2p_bonus_history(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/starred/payments/list")
@mobile_v2.post("/api/mobile/v2/starred/payments/list")
async def starred_payments_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/starred/payments/change_active_ordering")
@mobile_v2.post("/api/mobile/v2/starred/payments/change_active_ordering")
async def starred_payments_change_active_ordering(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/starred/payments/change")
@mobile_v2.post("/api/mobile/v2/starred/payments/change")
async def starred_payments_change(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/starred/payments/add")
@mobile_v2.post("/api/mobile/v2/starred/payments/add")
async def starred_payments_add(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/starred/payments/add_from_history")
@mobile_v2.post("/api/mobile/v2/starred/payments/add_from_history")
async def starred_payments_add_from_history(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/starred/payments/delete")
@mobile_v2.post("/api/mobile/v2/starred/payments/delete")
async def starred_payments_delete(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/starred/payments/create_p2p")
@mobile_v2.post("/api/mobile/v2/starred/payments/create_p2p")
async def starred_payments_create_p2p(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bills_v2/create")
@mobile_v2.post("/api/mobile/v2/bills_v2/create")
async def request_amount_create(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bills_v2/{bill_uid}/change")
@mobile_v2.post("/api/mobile/v2/bills_v2/{bill_uid}/change")
async def request_amount_change(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bills_v2/list")
@mobile_v2.post("/api/mobile/v2/bills_v2/list")
async def request_amount_list(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bills_v2/{bill_uid}/delete")
@mobile_v2.post("/api/mobile/v2/bills_v2/{bill_uid}/delete")
async def request_amount_delete(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bills_v2/{bill_uid}/payments/mobile/prepare")
@mobile_v2.post("/api/mobile/v2/bills_v2/{bill_uid}/payments/mobile/prepare")
async def request_amount_prepare(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/receive/{bill_uid}/card_to_wallet/token/create")
@mobile_v2.post("/api/mobile/v2/receive/{bill_uid}/card_to_wallet/token/create")
async def request_amount_c2w_pre_transfer(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/receive/{bill_uid}/card/by_card_id/pre_transfer")
@mobile_v2.post("/api/mobile/v2/receive/{bill_uid}/card/by_card_id/pre_transfer")
async def request_amount_c2c_pre_transfer(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/receive/{bill_uid}/wallet/by_card_id/pre_transfer")
@mobile_v2.post("/api/mobile/v2/receive/{bill_uid}/wallet/by_card_id/pre_transfer")
async def request_amount_w2c_pre_transfer(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/receive/{bill_uid}/wallet/transfer")
@mobile_v2.post("/api/mobile/v2/receive/{bill_uid}/wallet/transfer")
async def request_amount_w2w_transfer(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/tariffs/info")
@mobile_v2.post("/api/mobile/v2/vcards/tariffs/info")
async def visa_virtual_tariffs_info(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/activate")
@mobile_v2.post("/api/mobile/v2/vcards/activate")
async def visa_virtual_activate(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/block")
@mobile_v2.post("/api/mobile/v2/vcards/block")
async def visa_virtual_block(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/client")
@mobile_v2.post("/api/mobile/v2/vcards/client")
async def visa_virtual_client(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/create")
@mobile_v2.post("/api/mobile/v2/vcards/create")
async def visa_virtual_create(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/rename")
@mobile_v2.post("/api/mobile/v2/vcards/rename")
async def visa_virtual_rename(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/transactions")
@mobile_v2.post("/api/mobile/v2/vcards/transactions")
async def visa_virtual_transactions(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/to_card/pre_transfer")
@mobile_v2.post("/api/mobile/v2/vcards/to_card/pre_transfer")
async def visa_virtual_to_card_pre_transfer(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/vcards/to_card/transfer")
@mobile_v2.post("/api/mobile/v2/vcards/to_card/transfer")
async def visa_virtual_to_card_transfer(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/credentials")
@mobile_v2.post("/api/mobile/v2/jett/user/credentials")
async def jett_user_credentials(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/faqs")
@mobile_v2.post("/api/mobile/v2/jett/user/faqs")
async def jett_user_faqs(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/widget")
@mobile_v2.post("/api/mobile/v2/jett/user/widget")
async def jett_user_widget(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/stocks")
@mobile_v2.post("/api/mobile/v2/jett/user/stocks")
async def jett_user_stocks(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/transfer/prepare")
@mobile_v2.post("/api/mobile/v2/jett/transfer/prepare")
async def jett_transfer_prepare(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/transfer/confirm")
@mobile_v2.post("/api/mobile/v2/jett/transfer/confirm")
async def jett_transfer_confirm(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/open_account")
@mobile_v2.post("/api/mobile/v2/jett/user/open_account")
async def jett_open_account(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/status")
@mobile_v2.post("/api/mobile/v2/jett/user/status")
async def jett_user_status(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/balances")
@mobile_v2.post("/api/mobile/v2/jett/user/balances")
async def jett_user_balances(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/info_text")
@mobile_v2.post("/api/mobile/v2/jett/user/info_text")
async def jett_user_info_text(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/withdraw/prepare")
@mobile_v2.post("/api/mobile/v2/jett/user/withdraw/prepare")
async def jett_user_withdraw_prepare(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/withdraw/confirm")
@mobile_v2.post("/api/mobile/v2/jett/user/withdraw/confirm")
async def jett_user_withdraw_confirm(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/brokers")
@mobile_v2.post("/api/mobile/v2/jett/user/brokers")
async def jett_user_brokers(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/jett/user/signin")
@mobile_v2.post("/api/mobile/v2/jett/user/signin")
async def jett_user_signin(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/airports/search")
@mobile_v2.post("/api/mobile/v2/bookhara/airports/search")
async def avia_tickets_airports_search(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/offers/search")
@mobile_v2.post("/api/mobile/v2/bookhara/offers/search")
async def avia_tickets_offers_search(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/offers/info")
@mobile_v2.post("/api/mobile/v2/bookhara/offers/info")
async def avia_tickets_offer_by_id(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/offers/fare")
@mobile_v2.post("/api/mobile/v2/bookhara/offers/fare")
async def avia_tickets_offer_fare(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/refs/countries")
@mobile_v2.post("/api/mobile/v2/bookhara/refs/countries")
async def avia_tickets_refs_countries(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/visa/types")
@mobile_v2.post("/api/mobile/v2/bookhara/visa/types")
async def avia_tickets_visa_types(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/offer/book")
@mobile_v2.post("/api/mobile/v2/bookhara/offer/book")
async def avia_tickets_offer_book(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/offer/book/check_price")
@mobile_v2.post("/api/mobile/v2/bookhara/offer/book/check_price")
async def avia_tickets_offer_check_price(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/offer/book/payment_permission")
@mobile_v2.post("/api/mobile/v2/bookhara/offer/book/payment_permission")
async def avia_tickets_offer_payment_permission(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/account/booked/offers")
@mobile_v2.post("/api/mobile/v2/bookhara/account/booked/offers")
async def avia_tickets_my_tickets(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/account/booked/offer")
@mobile_v2.post("/api/mobile/v2/bookhara/account/booked/offer")
async def avia_tickets_purchased_ticket(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/offer/book/pdf")
@mobile_v2.post("/api/mobile/v2/bookhara/offer/book/pdf")
async def avia_tickets_offer_book_pdf(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/transfer/prepare")
@mobile_v2.post("/api/mobile/v2/bookhara/transfer/prepare")
async def avia_tickets_transfer_prepare(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/transfer/confirm")
@mobile_v2.post("/api/mobile/v2/bookhara/transfer/confirm")
async def avia_tickets_transfer_confirm(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/offers/rules")
@mobile_v2.post("/api/mobile/v2/bookhara/offers/rules")
async def avia_tickets_offer_rules(_):
    body = {}
    return prepare_response(body=body)


@mobile_v2.get("/api/mobile/v2/bookhara/account/update/booked/offers")
@mobile_v2.post("/api/mobile/v2/bookhara/account/update/booked/offers")
async def avia_tickets_update_booked_offers(_):
    body = {}
    return prepare_response(body=body)
