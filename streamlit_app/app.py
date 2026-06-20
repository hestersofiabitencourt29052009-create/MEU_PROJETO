import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="CRUD Manager",
    page_icon="👨‍💻",
    layout="wide"
)

st.title("👨‍💻 CRUD Manager - Sistema de Gerenciamento de Usuários e Produtos")

# MENU
menu = st.sidebar.selectbox(
    "Selecione uma opção",
    ["Usuários", "Produtos"]
)

# ==========================
# USUÁRIOS
# ==========================
if menu == "Usuários":

    st.header("👤 Gerenciamento de Usuários")

    with st.form("form_usuario", clear_on_submit=True):

        id_usuario = st.number_input(
            "ID do Usuário",
            min_value=0,
            value=0
        )

        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        col1, col2, col3 = st.columns(3)

        with col1:
            criar_usuario = st.form_submit_button("Criar")

        with col2:
            atualizar_usuario = st.form_submit_button("Atualizar")

        with col3:
            excluir_usuario = st.form_submit_button("Excluir")

    # CREATE
    if criar_usuario:
        dados = {
            "nome": nome,
            "email": email,
            "senha": senha
        }

        resposta = requests.post(
            f"{API_URL}/usuarios/",
            json=dados
        )

        if resposta.status_code in [200, 201]:
            st.success("Usuário criado com sucesso!")
        else:
            st.error("Erro ao criar usuário.")

    # UPDATE
    if atualizar_usuario and id_usuario > 0:

        dados = {
            "nome": nome,
            "email": email,
            "senha": senha
        }

        resposta = requests.put(
            f"{API_URL}/usuarios/{id_usuario}",
            json=dados
        )

        if resposta.status_code == 200:
            st.success("Usuário atualizado!")
        else:
            st.error("Erro ao atualizar usuário.")

    # DELETE
    if excluir_usuario and id_usuario > 0:

        resposta = requests.delete(
            f"{API_URL}/usuarios/{id_usuario}"
        )

        if resposta.status_code == 200:
            st.success("Usuário removido!")
        else:
            st.error("Erro ao remover usuário.")

    st.subheader("Lista de Usuários")

    try:
        resposta = requests.get(f"{API_URL}/usuarios/")

        if resposta.status_code == 200:
            st.dataframe(
                resposta.json(),
                use_container_width=True
            )

    except:
        st.error("API indisponível.")

# ==========================
# PRODUTOS
# ==========================
if menu == "Produtos":

    st.header("📦 Gerenciamento de Produtos")

    with st.form("form_produto", clear_on_submit=True):

        id_produto = st.number_input(
            "ID do Produto",
            min_value=0,
            value=0
        )

        nome_produto = st.text_input("Nome do Produto")

        preco = st.number_input(
            "Preço",
            min_value=0.0,
            format="%.2f"
        )

        descricao = st.text_area("Descrição")

        col1, col2, col3 = st.columns(3)

        with col1:
            criar_produto = st.form_submit_button("Criar")

        with col2:
            atualizar_produto = st.form_submit_button("Atualizar")

        with col3:
            excluir_produto = st.form_submit_button("Excluir")

    # CREATE
    if criar_produto:

        dados = {
            "nome": nome_produto,
            "preco": preco,
            "descricao": descricao
        }

        resposta = requests.post(
            f"{API_URL}/produtos/",
            json=dados
        )

        if resposta.status_code in [200, 201]:
            st.success("Produto criado!")
        else:
            st.error("Erro ao criar produto.")

    # UPDATE
    if atualizar_produto and id_produto > 0:

        dados = {
            "nome": nome_produto,
            "preco": preco,
            "descricao": descricao
        }

        resposta = requests.put(
            f"{API_URL}/produtos/{id_produto}",
            json=dados
        )

        if resposta.status_code == 200:
            st.success("Produto atualizado!")
        else:
            st.error("Erro ao atualizar produto.")

    # DELETE
    if excluir_produto and id_produto > 0:

        resposta = requests.delete(
            f"{API_URL}/produtos/{id_produto}"
        )

        if resposta.status_code == 200:
            st.success("Produto removido!")
        else:
            st.error("Erro ao remover produto.")

    st.subheader("Lista de Produtos")

    try:
        resposta = requests.get(
            f"{API_URL}/produtos/"
        )

        if resposta.status_code == 200:
            st.dataframe(
                resposta.json(),
                use_container_width=True
            )

    except:
        st.error("API indisponível.")
