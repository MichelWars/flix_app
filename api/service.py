import requests


class Auth:

    # acessa URL de autenticação e gera um token

    def __init__(self):
        self.__base_url = 'https://michelwars.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'

    # Repassa as credenciais e recebe um token

    def get_token(self, username, password):
        auth_payload = {'username': username, 'password': password}
        auth_response = requests.post(self.__auth_url, json=auth_payload)
        if auth_response.status_code == 200:
            return auth_response.json()
        return {
            'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'
        }
