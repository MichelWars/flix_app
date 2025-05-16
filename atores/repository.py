import requests
import streamlit as st

from login.service import logout


class AtorRepository:
    def __init__(self):
        self.__base_url = 'https://michelwars.pythonanywhere.com/api/v1/'
        self.__atores_url = f'{self.__base_url}atores/'
        self.__headers = {'Authorization': f'Bearer {st.session_state.token}'}

    def get_atores(self):
        response = requests.get(
            self.__atores_url,
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

    def create_ator(self, ator):
        response = requests.post(
            self.__atores_url,
            headers=self.__headers,
            data=ator,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f'Erro ao obter os dados da API. Status code: {response.status_code}'
        )
