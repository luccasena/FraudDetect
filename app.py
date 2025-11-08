import streamlit as st
import numpy as np
import joblib
from agent import detectFraud

st.title("Detecção de Licitações Fraudulentas")


col1, col2 = st.columns(2)

with col1:

    nome = st.text_input("Digite o nome do orgão:", key="nome")

    categoria = st.selectbox("1. Digite a categoria da compra", options=["Material de Escritório", "Mobiliário", "Transporte Escolar", "Consultoria Técnica", "Medicamento", "Serviço de Limpeza", "Serviço de Engenharia", "Equipamento de Informática"], key="categoria")

    quantidade = st.number_input("2. Digite a quantidade da compra", key="quantidade", format="%.0f")

    preco_mercado = st.number_input("3. Digite o preço de mercado", key="preco_mercado", format="%.2f")

    preco_estimado = st.number_input("4. Digite o preço estimado", key="preco_estimado", format="%.2f")




with col2:

    preco_vencedor = st.number_input("5. Digite o preço do vencedor", key="preco_vencedor", format="%.2f")

    numero_licitante = st.number_input("6. Digite o número do licitante", format="%.0f", key="numero_licitante")

    bdi_percentual = st.number_input("7. Digite o BDI percentual", key="bdi_percentual")

    numero_aditivos = st.number_input("8. Digite o numero de aditivos", format="%.0f", key="numero_aditivos")

    historico_contratos = st.number_input("9. Digite o histórico de contrato em anos", format="%.0f", key="historico_contratos")


licitacao_data = np.array([categoria,quantidade,preco_mercado,preco_estimado,preco_vencedor,numero_licitante,bdi_percentual,numero_aditivos,historico_contratos])

st.markdown("---")

if st.button("Gerar detecções e análise"):

    
    if len(licitacao_data) == 9:

        # Carregando o modelo e o pré-processador:
        random_forest = joblib.load("models/modelRF.pkl")
        transformer = joblib.load("models/preprocessor.pkl")

        # Transformando os dados de entrada usando o pré-processador:
        user_info_transformer = transformer.transform([licitacao_data])

        # Fazendo a previsão:
        prediction = random_forest.predict(user_info_transformer)
        prediction_proba = random_forest.predict_proba(user_info_transformer)

        st.session_state['prediction'] = prediction
        st.session_state['licitacao_data'] = licitacao_data

        if prediction == 'Não Fraudulenta':
            proba = prediction_proba[0][0]
            
            st.session_state['proba'] = proba

        elif prediction == 'Fraudulenta':
            proba = prediction_proba[0][1]
            st.session_state['proba'] = proba                

        response_agent = detectFraud(nome, st.session_state['licitacao_data'], st.session_state['prediction'], st.session_state['proba'])
        
        st.markdown("---")
        st.subheader("Relatório:")
        st.session_state.relatorio_gerado = False
        st.markdown(response_agent)

    else:
        st.warning("Por favor, preencha todos os campos antes de fazer a previsão.")