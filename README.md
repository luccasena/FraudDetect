# 

# 🕵️‍♂️ DFraudDetect

## 📘 Visão Geral  
O **Detector de Licitações Fraudulentas** é um projeto de **Inteligência Artificial aplicada à Transparência Pública**, cujo objetivo é **identificar possíveis indícios de fraude em licitações públicas**.  

A aplicação combina **Modelos de Machine Learning** para **prever a probabilidade de fraude** em uma licitação e um **modelo de linguagem (LLM)** que **gera relatórios explicativos** sobre quais informações influenciaram a decisão do modelo.  

> ⚠️ Este é um projeto **em desenvolvimento** e ainda passa por melhorias de desempenho, precisão e usabilidade.


--- 

## 🧠 Objetivos do Projeto

- **Analisar registros de licitações públicas** e identificar possíveis indícios de irregularidades.  
- **Prever se uma compra pública pode ser considerada fraudulenta** com base em dados históricos e características do edital.  
- **Gerar relatórios automáticos com suporte de IA**, explicando de forma interpretável quais variáveis influenciaram a decisão do modelo.  
- **Auxiliar órgãos de controle, jornalistas e cidadãos** no monitoramento e análise de compras governamentais.  

---

## ⚙️ Arquitetura do Sistema

O projeto é dividido em **duas camadas principais**:

1. **Modelo de Machine Learning (Preditor de Fraude)**  
   - Treinado com dados históricos de licitações rotuladas (fraudulentas e legítimas).  
   - Utiliza técnicas de engenharia de atributos e algoritmos supervisionados.
   - Retorna a **probabilidade de fraude** para cada registro.

2. **Relatório de IA (LLM Explicativo)**  
   - Implementado com um modelo de linguagem (LLM) como Groq.  
   - Recebe a entrada do modelo de ML e o registro analisado.  
   - Gera um **relatório textual explicativo**, indicando:
     - Quais informações mais influenciaram a predição.
     - Qual o contexto e justificativa da classificação.
     - Recomendações para investigação adicional.

---

## 📅 Status do Projeto: Em desenvolvimento...

