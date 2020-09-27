# coding=utf-8

import allure
from utils.api import *
import json
import datetime

now = datetime.datetime.now()
hero_name = "Black Dragon"
city = "Moscow"
birth_date = now.strftime("%Y-%m-%d")
tomorrow = now + datetime.timedelta(days=1)
main_skill = "QA"
gender = "M"
phone = "+79999999999"
incorrect_date_format = "12-12-2020"
invalid_date_format = "2020-13-20"

new_hero_name = "Black Dragon new"
new_city = "Moscow new"
new_birth_date = tomorrow.strftime("%Y-%m-%d")
new_main_skill = "QA new"
new_gender = "F"
new_phone = "+71111111111"


@allure.feature('Test API Superhero-controller')
@allure.story('1.Create superhero. POST /superheroes')
def test_create_superhero(api_testing):
    endpoint = "https://{}/superheroes".format(api_testing.API_URL_PREFICS)

    with allure.step('Step 1. Incorrect date requests'):
        data = {
            "birthDate": string,
            "city": city,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        assert (response.status_code == 400), create_error_message(response, endpoint, data)
        data = {
            "birthDate": incorrect_date_format,
            "city": city,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        assert (response.status_code == 400), create_error_message(response, endpoint, data)
        data = {
            "birthDate": invalid_date_format,
            "city": city,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        assert (response.status_code == 400), create_error_message(response, endpoint, data)

        data = {
            "birthDate": "",
            "city": city,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO изменить ответ на 400 после фикса
        assert (response.status_code == 403), create_error_message(response, endpoint, data)

        data = {
            "birthDate": new_birth_date,
            "city": city,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO нет валидации birthDate на будущую дату
        assert (response.status_code == 200), create_error_message(response, endpoint, data)

    with allure.step('Step 2. Incorrect city request'):
        data = {
            "birthDate": birth_date,
            "city": integer,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO возможный баг, поле city не думаю что должно позволять int значения
        assert (response.status_code == 200), create_error_message(response, endpoint, data)

    with allure.step('Step 3. Incorrect fullName request'):
        data = {
            "birthDate": birth_date,
            "city": city,
            "fullName": integer,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO возможный баг, поле fullName не думаю что должно позволять int значения
        assert (response.status_code == 200), create_error_message(response, endpoint, data)

    with allure.step('Step 4. Incorrect gender request'):
        data = {
            "birthDate": birth_date,
            "city": city,
            "fullName": hero_name,
            "gender": string,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO исправить код ответа на 400 после фикса бага с gender, gender ["F", "M"]
        assert (response.status_code == 200), create_error_message(response, endpoint, data)

    with allure.step('Step 5. Incorrect mainSkill request'):
        data = {
            "birthDate": birth_date,
            "city": city,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": integer,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO возможный баг, поле mainSkill не думаю что должно позволять int значения
        assert (response.status_code == 200), create_error_message(response, endpoint, data)

    with allure.step('Step 6. Incorrect phone request'):
        data = {
            "birthDate": birth_date,
            "city": city,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": string
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO возможный баг, поле phone не думаю что должно позволять string значения
        assert (response.status_code == 200), create_error_message(response, endpoint, data)

    with allure.step('Step 7. Request with empty body'):
        data = {}
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO изменить ответ после фикса, должнен быть 400
        assert (response.status_code == 403), create_error_message(response, endpoint, data)

    with allure.step('Step 8. Correct request'):
        data = {
            "birthDate": birth_date,
            "city": city,
            "fullName": hero_name,
            "gender": gender,
            "mainSkill": main_skill,
            "phone": phone
        }
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        print(data)
        # TODO код по доке должен быть 201, изменить код ответа на 201 после фикса
        assert (response.status_code == 200), create_error_message(response, endpoint, data)
        data = response.json()
        assert len(data) > 0
        assert birth_date == data["birthDate"]
        assert city == data["city"]
        assert hero_name == data["fullName"]
        assert gender == data["gender"]
        assert birth_date == data["birthDate"]
        # TODO раскоментировать строку после фикса, сейчас Superhero создается с phone null
        # assert phone == data["phone"]
        print(str(response.json()))
        print(response.elapsed.total_seconds())
        global new_hero_id
        new_hero_id = data["id"]


@allure.feature('Test API Superhero-controller')
@allure.story('2.Get all superheroes. GET /superheroes')
def test_get_superheroes(api_testing):
    endpoint = "https://{}/superheroes".format(api_testing.API_URL_PREFICS)
    with allure.step('Step 1. Correct request'):
        response = send_get_request_to_api(endpoint, api_testing.API_TOKEN)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        data = response.json()
        assert len(data) > 0
        i = 0
        while i < len(data):
            if new_hero_id == data[i]["id"]:
                assert new_hero_id == data[i]["id"]
                assert birth_date == data[i]["birthDate"]
                assert city == data[i]["city"]
                assert hero_name == data[i]["fullName"]
                assert gender == data[i]["gender"]
                assert birth_date == data[i]["birthDate"]
                # TODO раскоментировать строку после фикса, сейчас Superhero создается с phone null
                # assert phone == data[i]["phone"]
                break
            else:
                i += 1
        print(str(response.json()))
        print(response.elapsed.total_seconds())


@allure.feature('Test API Superhero-controller')
@allure.story('3.Update of superhero. PUT /superheroes/{id}')
def test_update_superheroes(api_testing):
    endpoint = "https://{}/superheroes/{}"
    data = {
        "birthDate": new_birth_date,
        "city": new_city,
        "fullName": new_hero_name,
        "gender": new_gender,
        "mainSkill": new_main_skill,
        "phone": new_phone
    }
    with allure.step('Step 1. Request incorrect id'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, string)
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        assert (response.status_code == 400), create_error_message(response, final_endpoint, data)

    with allure.step('Step 2. Request not found id'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, max_integer)
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO изменить ответ на 404 после фикса
        assert (response.status_code == 400), create_error_message(response, final_endpoint, data)

    with allure.step('Step 3. Request empty id'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, "")
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        assert (response.status_code == 405), create_error_message(response, final_endpoint, data)

    with allure.step('Step 4. Incorrect date requests'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        data = {
            "birthDate": string,
            "city": new_city,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        assert (response.status_code == 400), create_error_message(response, final_endpoint, data)
        data = {
            "birthDate": incorrect_date_format,
            "city": new_city,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        assert (response.status_code == 400), create_error_message(response, final_endpoint, data)
        data = {
            "birthDate": invalid_date_format,
            "city": new_city,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        assert (response.status_code == 400), create_error_message(response, final_endpoint, data)

        data = {
            "birthDate": "",
            "city": new_city,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO изменить ответ на 400 после фикса
        assert (response.status_code == 403), create_error_message(response, final_endpoint, data)

        data = {
            "birthDate": new_birth_date,
            "city": new_city,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO нет валидации birthDate на будущую дату и периодически 400 что не найден Superhero
        assert (response.status_code in [200, 400]), create_error_message(response, final_endpoint, data)

    with allure.step('Step 5. Incorrect city request'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        data = {
            "birthDate": new_birth_date,
            "city": integer,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO возможный баг, поле city не думаю что должно позволять int значения и
        #  периодически 400 что не найден Superhero
        assert (response.status_code in [200, 400]), create_error_message(response, final_endpoint, data)

    with allure.step('Step 6. Incorrect fullName request'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        data = {
            "birthDate": new_birth_date,
            "city": new_city,
            "fullName": integer,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO возможный баг, поле fullName не думаю что должно позволять int значения и
        #  периодически 400 что не найден Superhero
        assert (response.status_code in [200, 400]), create_error_message(response, final_endpoint, data)

    with allure.step('Step 7. Incorrect gender request'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        data = {
            "birthDate": new_birth_date,
            "city": new_city,
            "fullName": new_hero_name,
            "gender": string,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO исправить код ответа на 400 после фикса бага с gender, gender ["F", "M"] и периодически 400
        #  что не найден Superhero
        assert (response.status_code in [200, 400]), create_error_message(response, final_endpoint, data)

    with allure.step('Step 8. Incorrect mainSkill request'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        data = {
            "birthDate": new_birth_date,
            "city": new_city,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": integer,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO возможный баг, поле mainSkill не думаю что должно позволять int значения и периодически 400
        #  что не найден Superhero
        assert (response.status_code in [200, 400]), create_error_message(response, final_endpoint, data)

    with allure.step('Step 9. Incorrect phone request'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        data = {
            "birthDate": new_birth_date,
            "city": new_city,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": string
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO возможный баг, поле phone не думаю что должно позволять string значения и периодически 400
        #  что не найден Superhero
        assert (response.status_code in [200, 400]), create_error_message(response, final_endpoint, data)

        with allure.step('Step 10. Request empty body'):
            final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
            data = {}
            response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
            # TODO изменить ответ после фикса на 400
            assert (response.status_code == 403), create_error_message(response, final_endpoint, data)

    with allure.step('Step 11. Correct request'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        data = {
            "birthDate": new_birth_date,
            "city": new_city,
            "fullName": new_hero_name,
            "gender": new_gender,
            "mainSkill": new_main_skill,
            "phone": new_phone
        }
        response = send_put_request_to_api(final_endpoint, api_testing.API_TOKEN, data=json.dumps(data, indent=4))
        # TODO периодически 400 что не найден Superhero, поправить после фикса
        assert (response.status_code in [200, 400]), create_error_message(response, final_endpoint, data)
        # TODO убрать if после фикса 400
        if response.status_code == 200:
            pass
            # TODO поступает пустой ответ, раскоментировать как будет возвращаться и убрать pass
            # assert len(response.json()) > 0
            # data = response.json()
            # assert len(data) > 0
            # assert new_birth_date == data["birthDate"]
            # assert new_city == data["city"]
            # assert new_hero_name == data["fullName"]
            # assert new_gender == data["gender"]
            # assert new_birth_date == data["birthDate"]
            # # TODO раскоментировать строку после фикса, сейчас Superhero создается с phone null
            # # assert phone == data["phone"]
            # print(str(response.json()))
            # print(response.elapsed.total_seconds())


@allure.feature('Test API Superhero-controller')
@allure.story('4.Get superhero by id. GET /superheroes/{id}')
def test_get_superhero_by_id(api_testing):
    endpoint = "https://{}/superheroes/{}"
    with allure.step('Step 1. Request incorrect id'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, string)
        response = send_get_request_to_api(final_endpoint, api_testing.API_TOKEN)
        assert (response.status_code == 400), create_error_message(response, final_endpoint)

    with allure.step('Step 2. Request not found id'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, max_integer)
        response = send_get_request_to_api(final_endpoint, api_testing.API_TOKEN)
        # TODO изменить на 404 после фикса
        assert (response.status_code == 400), create_error_message(response, final_endpoint)

    with allure.step('Step 3. Correct requests'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        response = send_get_request_to_api(final_endpoint, api_testing.API_TOKEN)
        # TODO периодически 400 что не найден Superhero, поправить после фикса
        assert (response.status_code in [200, 400]), create_error_message(response, final_endpoint)
        # TODO убрать if после фикса 400
        if response.status_code == 200:
            assert len(response.json()) > 0
            data = response.json()
            assert len(data) > 0
            assert new_birth_date == data["birthDate"]
            assert new_city == data["city"]
            assert new_hero_name == data["fullName"]
            assert new_gender == data["gender"]
            assert new_birth_date == data["birthDate"]
            # TODO раскоментировать строку после фикса, сейчас Superhero создается с phone null
            # assert phone == data["phone"]
            print(str(response.json()))
            print(response.elapsed.total_seconds())


@allure.feature('Test API Superhero-controller')
@allure.story('5.Remove superhero by id. DELETE /superheroes/{id}')
def test_delete_superhero_by_id(api_testing):
    endpoint = "https://{}/superheroes/{}"
    with allure.step('Step 1. Request incorrect id'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, string)
        response = send_delete_request_to_api(final_endpoint, api_testing.API_TOKEN, {})
        assert (response.status_code == 400), create_error_message(response, final_endpoint)

    with allure.step('Step 2. Request not found id'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, max_integer)
        response = send_delete_request_to_api(final_endpoint, api_testing.API_TOKEN, {})
        # TODO изменить на 404 после фикса(возможно особенности реализации из доки непонятно)
        assert (response.status_code == 200), create_error_message(response, final_endpoint)

    with allure.step('Step 3. Correct requests'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        response = send_delete_request_to_api(final_endpoint, api_testing.API_TOKEN, {})
        # TODO изменить на 204 после фикса(возможно особенности реализации из доки непонятно)
        assert (response.status_code == 200), create_error_message(response, final_endpoint)

    with allure.step('Step 4. Check correct delete superhero'):
        final_endpoint = endpoint.format(api_testing.API_URL_PREFICS, new_hero_id)
        response = send_get_request_to_api(final_endpoint, api_testing.API_TOKEN)
        # TODO изменить ответ на 404 после фикса
        # TODO делал 26.09 был ответ 400 и можно было определить что удаление прошло, 27.09 ответ всегда 200 и message
        #  нет, оставил так
        assert (response.status_code == 400), create_error_message(response, final_endpoint)
        assert response.json()["message"] == "Superhero with id '{}' was not found".format(new_hero_id)
