import requests
import streamlit as st

from login.service import logout


class AvaliacoesRepository:
    def __init__(self):
        self.__base_url = 'https://michelwars.pythonanywhere.com/api/v1/'
        self.__avaliacoes_url = f'{self.__base_url}avaliacoes/'
        self.__headers = {'Authorization': f'Bearer {st.session_state.token}'}

    def get_avaliacoes(self):
        response = requests.get(
            self.__avaliacoes_url,
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

    def create_avaliacao(self, avaliacao):
        response = requests.post(
            self.__avaliacoes_url,
            headers=self.__headers,
            data=avaliacao,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f'Erro ao obter os dados da API. Status code: {response.status_code}'
        )
