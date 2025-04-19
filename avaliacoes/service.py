import streamlit as st
from avaliacoes.repository import AvaliacoesRepository


class AvaliacaoService:

    def __init__(self):
        self.avaliacao_repository = AvaliacoesRepository()

    def get_avaliacoes(self):
        if 'avaliacoes' in st.session_state:
            return st.session_state.avaliacao
        avaliacoes = self.avaliacao_repository.get_avaliacoes()
        st.session_state.avaliacao = avaliacoes
        return avaliacoes

    def create_avaliacao(self, filme, estrelas, comentario):
        avaliacao = dict(
            filme=filme,
            estrelas=estrelas,
            comentario=comentario,
        )
        nova_avaliacao = self.avaliacao_repository.create_avaliacao(avaliacao)
        st.session_state.avaliacao.append(nova_avaliacao)
        return nova_avaliacao
