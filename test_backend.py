import pytest
import requests


   # Позитивные тесты
@pytest.mark.usefixtures("message_id")

    # Просмотр созданного сообщения в канале

def test_get_message(base_url, channel_id, headers, message_id):
    url = f"{base_url}/channels/{channel_id}/messages/{message_id}"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json().get('id') == str(message_id)
    # print("Созданное сообщение: " + response.json()['content'])

    # Получение списка сообщений
def test_get_messages_list(base_url, channel_id, headers, message_id):
    url = f"{base_url}/channels/{channel_id}/messages"
    params = {
        "limit": 5
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    messages_list = response.json()
    assert isinstance(messages_list, list)
    assert len(messages_list) != 0


    # Создание сообщения с вложением
def test_message_with_attachment(base_url, channel_id, headers):
    url = f"{base_url}/channels/{channel_id}/messages"
    files = {
        'files[0]': ('test_image.png', open('test_image.png', 'rb'))
    }

    data = {
        'content': "Alpine skiing!!!"
    }

    # Удаление Content-Type
    headers.pop('Content-Type', None)
    response = requests.post(url, headers=headers, files=files, data=data)
    assert response.status_code == 200
    message_id = response.json().get('id')
    assert message_id != 0
    assert 'attachments' in response.json()


    # Создание сообщения с упоминанием пользователя
def test_mentioned_user(base_url, channel_id, headers):
    url = f"{base_url}/channels/{channel_id}/messages"
    mentioned_user_id = "1184822550052741220"
    data = {
        "content": f"New car, caviar, four-star day dream...<@{mentioned_user_id}>"
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json()["mentions"][0]["id"] == mentioned_user_id

    # Добавление реакции на сообщение и удаление ее
def test_add_reaction(base_url, channel_id, headers, message_id):
    emoji = "☠️"
    emoji_encoded = requests.utils.quote(emoji)
    url = f"{base_url}/channels/{channel_id}/messages/{message_id}/reactions/{emoji_encoded}/@me"
    add_reaction = requests.put(url, headers=headers)
    assert add_reaction.status_code == 204

    remove_reaction_url = f"{base_url}/channels/{channel_id}/messages/{message_id}/reactions/{emoji_encoded}/@me"
    delete_reaction = requests.delete(remove_reaction_url, headers=headers)
    assert delete_reaction.status_code == 204


  # Негативные тесты

  # Отправка пустого сообщения
def test_invalid_message(base_url, channel_id, headers):
    url = f"{base_url}/channels/{channel_id}/messages"
    data = {
        "content": "       "
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    assert response.json()["message"] == "Cannot send an empty message"


    # Просмотр сообщения с несуществующим Id
def test_non_existing_id_message(base_url, channel_id, headers):
    invalid_message_id = "666"
    url = f"{base_url}/channels/{channel_id}/messages/{invalid_message_id}"
    response = requests.get(url, headers=headers)
    assert response.status_code == 404
    assert response.json()["message"] == "Unknown Message"

    # Добавление реакции на несуществующее сообщение
def test_add_reaction_to_non_existing_message(base_url, channel_id, headers):
    invalid_message_id = "666"
    emoji = "👹"
    emoji_encoded = requests.utils.quote(emoji)
    url = f"{base_url}/channels/{channel_id}/messages/{invalid_message_id}/reactions/{emoji_encoded}/@me"
    response = requests.put(url, headers=headers)
    assert response.status_code == 404
    assert response.json()["message"] == "Unknown Message"