import configuration
import requests
import data


# создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body)


order_track = post_new_order(data.order_body).json()["track"]


# получение данных о заказе по треку api/v1/orders/track?t=NNNNNN
def get_info_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(track))