import requests
import streamlit as st

from login.service import logout


class FilmesRepository:
    def __init__(self):
        self.__base_url = 'https://michelwars.pythonanywhere.com/api/v1/'
        self.__filmes_url = f'{self.__base_url}filmes/'
        self.__headers = {'Authorization': f'Bearer {st.session_state.token}'}

    def get_filmes(self):
        response = requests.get(
            self.__filmes_url,
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

    def create_filme(self, filme):
        response = requests.post(
            self.__filmes_url,
            headers=self.__headers,
            data=filme,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f'Erro ao obter os dados da API. Status code: {response.status_code}'
        )

    def get_stats_filmes(self):
        response = requests.get(
            f'{self.__filmes_url}stats/',
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
