# coding=utf-8
import requests

incorrect_id = "tt"
max_integer = 2147483647
integer = 1
string = "tt"


def send_get_request_to_api(endpoint, api_token):
    headers = {"Authorization": "Bearer {0}".format(api_token), 'Content-type': 'application/json'}
    response = requests.get(endpoint, headers=headers)
    return response


def send_put_request_to_api(endpoint, api_token, data):
    headers = {"Authorization": "Bearer {0}".format(api_token), 'Content-type': 'application/json'}
    response = requests.put(endpoint, data=str(data).encode('utf-8'), headers=headers)
    return response


def send_post_request_to_api(endpoint, api_token, data):
    headers = {"Authorization": "Bearer {0}".format(api_token), 'Content-type': 'application/json'}
    response = requests.post(endpoint, data=str(data).encode('utf-8'), headers=headers)
    return response


def send_delete_request_to_api(endpoint, api_token, data):
    headers = {"Authorization": "Bearer {0}".format(api_token), 'Content-type': 'application/json'}
    response = requests.delete(endpoint, headers=headers,  data=str(data).encode('utf-8'))
    return response


def send_patch_request_to_api(endpoint, api_token, data):
    headers = {"Authorization": "Bearer {0}".format(api_token), 'Content-type': 'application/json'}
    response = requests.patch(endpoint, data=str(data).encode('utf-8'), headers=headers)
    return response


def get_error_message(response):
    try:
        data = response.json()
        message = data["message"]
    except:
        print(response)
        message = ""
    return message


def create_error_message(response, endpoint, params=dict()):
    message = "Message: {};".format(get_error_message(response))
    message += " endpoint: {};".format(endpoint)
    message += ''.join(' {}: {};'.format(key, val) for key, val in params.items())
    return message

