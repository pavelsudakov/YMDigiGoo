import requests
import json
from datetime import date, timedelta

# Ваш OAuth-токен
token = "ваш_токен"

# URL для обращения к API Яндекс.Маркета
base_url = "https://api.partner.market.yandex.ru/v2"

# Заголовки для запроса
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

def handle_cart_request(campaignId, cart):
    # Здесь мы предполагаем, что функция handle_cart_request вызывается, когда вы получаете POST /cart запрос от Яндекс.Маркета

    # Ответ на запрос POST /cart
    response = {
        "cart": {
            "deliveryOptions": [
                {
                    "type": "DIGITAL",
                    "serviceName": "Доставка на электронную почту",
                    "dates": {
                        "fromDate": str(date.today()), 
                    }
                }
            ],
            "paymentMethods": ["YANDEX", "APPLE_PAY", "GOOGLE_PAY", "TINKOFF_CREDIT", "SBP"],
            # другие поля здесь...
        }
    }

    return response

def deliver_digital_goods(campaignId, orderId, digital_goods):
    # Здесь мы предполагаем, что функция deliver_digital_goods вызывается, когда заказ переходит в статус PROCESSING

    url = f"{base_url}/campaigns/{campaignId}/orders/{orderId}/deliverDigitalGoods.json"

    data = {
        "order": {
            "items": digital_goods,  # массив цифровых товаров с полями "offerId", "count" и "codes"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Проверка статуса запроса
    if response.status_code == 200:
        print("Успешно отправлено!")
    else:
        print(f"Ошибка! Код ответа: {response.status_code}, Сообщение: {response.text}")

    return response.status_code
