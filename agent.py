from groq import Groq
from dotenv import load_dotenv, find_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv(find_dotenv())

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# Mensagem de sistema inicial
messages = [
    {
        "role": "system",
        "content": """Você é um assistente especializado em detectar fraudes em licitações públicas no Brasil,
                      com profundo conhecimento das leis brasileiras relacionadas a licitações."""
    }
]

def detectFraud(nome, licitacao_data, predicao, predicao_proba):
    # Cria o prompt do usuário
    user_prompt = {
        "role": "user",
        "content": f""" Você é um assistente analista de inteligência artificial especializado em auditorias de licitações públicas. Seu objetivo é gerar relatórios objetivos e técnicos com base em: Entidade: {nome}, Dados(respectivamente, (entidade,categoria,quantidade,preco_mercado,preco_estimado,preco_vencedor,numero_licitantes,bdi_percentual,numero_aditivos,historico_contratos)): {licitacao_data}, Previsão do modelo Random Forest: {predicao}, Predict Proba: {predicao_proba} O público-alvo é um auditor experiente, portanto: - NÃO use linguagem genérica ou explicações sobre IA. - NÃO diga frases como “com base nos dados”, “o modelo previu” ou “sou uma IA”. - Evite redundâncias ou termos vagos. - Seja direto, técnico e embasado. Foque em: - Identificar indicadores de possível fraude - Destacar anomalias nos dados da licitação - Indicar ações de verificação ou investigação recomendadas - Avaliar a confiabilidade da predição ⚠️ Muito importante: - Se a probabilidade de fraude for >= 80%, trate o caso como **crítico**. - Se estiver entre 50% e 79%, classifique como **suspeito**. - Se for menor que 50%, classifique como **baixo risco**. - Sempre aponte quais variáveis mais influenciam essa classificação. Respeite o formato abaixo: ### 🏛️ Empresa: <nome_empresa> #### 📊 Resultado da Predição: <predicao> Probabilidade de Fraude: **<probabilidade>%** - Valor Estimado: <valor_estimado> - Número de Participantes: <num_participantes> - Tipo de Licitação: <tipo_licitacao> - Objeto: <objeto_licitacao> - Local de Execução: <local_execucao> - Tempo de Entrega: <prazo_execucao> - Histórico da Empresa: <historico_empresa> - Data de Abertura: <data_abertura> - Situação Atual: <situacao_atual> #### 🔍 Análise Técnica: Apresente uma análise concisa destacando indícios de fraude ou conformidade. Aponte fatores como valores desproporcionais, ausência de concorrência, padrões atípicos, vínculos com outras empresas, ou histórico suspeito. Use linguagem profissional e investigativa. #### 🧾 Recomendações de Auditoria: Indique medidas práticas — como verificação de vínculos societários, auditoria do histórico contratual, análise de sobrepreço, ou solicitação de documentação adicional. #### ⚠️ Observações Finais: Se a probabilidade for >= 80%, destaque a urgência de investigação imediata. Se for intermediária, recomende acompanhamento contínuo. Se for baixa, informe que os dados não sugerem irregularidades relevantes, mas mantenha o caso registrado para monitoramento. Caso haja inconsistências entre dados e predição, oriente a revisão manual."""
    }

    # Cria o histórico de mensagens completo (não altera o original global)
    conversation = messages + [user_prompt]

    # Faz a chamada à API Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=conversation,
        max_tokens=1000,
        temperature=0.7,
    )

    # Retorna o texto da resposta do agente
    return response.choices[0].message.content


