import streamlit as st
from atores.page import mostrar_atores
from avaliacoes.page import mostrar_avaliacoes
from home.page import show_home
from login.page import show_login
from login.service import logout
from filmes.page import mostrar_filmes
from generos.page import mostrar_generos


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        # Inicializa o estado do menu se ainda não existir
        if 'menu' not in st.session_state:
            st.session_state.menu = 'Inicio'

        # Selectbox que atualiza a session_state
        st.session_state.menu = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Inicio', 'Generos', 'Atores', 'Filmes', 'Avaliações'],
            index=['Inicio', 'Generos', 'Atores', 'Filmes', 'Avaliações'].index(st.session_state.menu)
        )

        # Botão de logout
        if st.sidebar.button("Logout"):
            logout()

        # Renderiza a página correta
        if st.session_state.menu == 'Inicio':
            show_home()

        elif st.session_state.menu == 'Generos':
            mostrar_generos()

        elif st.session_state.menu == 'Atores':
            mostrar_atores()

        elif st.session_state.menu == 'Filmes':
            mostrar_filmes()

        elif st.session_state.menu == 'Avaliações':
            mostrar_avaliacoes()


if __name__ == "__main__":
    main()
