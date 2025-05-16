import requests
import streamlit as st

from login.service import logout


class GenerosRepository:
    def __init__(self):
        self.__base_url = 'https://michelwars.pythonanywhere.com/api/v1/'
        self.__generos_url = f'{self.__base_url}generos/'
        self.__headers = {'Authorization': f'Bearer {st.session_state.token}'}

    def get_generos(self):
        response = requests.get(
            self.__generos_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f'Erro ao obter os dados da API. Status code: {response.status_code}'
        )

    def create_genero(self, genero):
        response = requests.post(
            self.__generos_url,
            headers=self.__headers,
            data=genero,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f'Erro ao obter os dados da API. Status code: {response.status_code}'
        )
