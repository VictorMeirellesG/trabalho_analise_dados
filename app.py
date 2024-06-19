import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


metricas_traduzidas = {
    'mean': 'Média',
    'median': 'Mediana',
    'std': 'Desvio Padrão'
}


def traduzir_metrica(metrica_original):
    return metricas_traduzidas[metrica_original]


 # URL do arquivo CSV no GitHub
    url_csv = https://github.com/VictorMeirellesG/trabalho_analise_dados/blob/main/data.csv

    # Leitura do CSV e armazenamento em 'df'
    df = pd.read_csv(url_csv)

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)

    
    st.title('Análise Descritiva dos Dados de Qualidade da Água em São José dos Campos')

    
    st.header('Dados Brutos')
    st.write(df)


    sistemas = df['Sistema de abastecimento'].unique()
    sistema_selecionado = st.selectbox('Selecione o sistema de abastecimento:', sistemas)


    df_sem_mes = df.drop(columns=['MES'])

    
    df_filtrado = df[df['Sistema de abastecimento'] == sistema_selecionado]


    st.header('Métricas por Sistema de Abastecimento')

    col1, col2 = st.columns([2, 1])
    with col1:
        metricas = df_filtrado.describe().transpose()
        st.write(metricas)

    tratamentos = {
        "ETA II - São José dos Campos": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Jardim Sta Inês III": "Desinfecção e Fluoretação",
        "ETA São Francisco Xavier": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Pousada do Vale": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Colinas do Parayba": "Desinfecção e Fluoretação",
        "Vista Verde I": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Jardim Satélite": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Eugênio de Mello": "Desinfecção e Fluoretação",
        "Jardim Motorama": "Desinfecção e Fluoretação",
        "Vista Verde II": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Bosque dos Eucaliptos": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Jardim Sta Inês II": "Desinfecção e Fluoretação",
        "Jd. Americano": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Jardim das Colinas": "Desinfecção e Fluoretação",
        "Bairro Putim": "Desinfecção e Fluoretação",
        "Jardim Sta Inês I": "Desinfecção e Fluoretação",
        "Jardim Morumbi": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Jardim Paraiso do Sol": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Novo Horizonte": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Parque Interlagos": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Vila Tatetuba": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Jardim das Indústrias": "Gradeamento, Pré-Cloração, Coagulação, Floculação, Decantação, Filtração, Desinfecção e Fluoretação",
        "Galo Branco": "Desinfecção e Fluoretação"
    }

    with col2:
        st.subheader('Tratamento de Água')
        st.write(f"{tratamentos.get(sistema_selecionado, 'Informação não disponível')}")

    
    st.header('Gráficos')

    col1, col2 = st.columns(2)
    with col1:
        categoria_selecionada = st.selectbox('Selecione a categoria para o gráfico:', df_sem_mes.columns[1:])
    with col2:
        metrica_original = st.selectbox('Selecione a métrica para os gráficos:', list(metricas_traduzidas.keys()), format_func=traduzir_metrica)
        metrica_traduzida = metricas_traduzidas[metrica_original]


    metricas_por_sistema = df.groupby('Sistema de abastecimento')[categoria_selecionada].agg(metrica_original)

    fig, ax = plt.subplots(figsize=(8, 6))
    metricas_por_sistema.plot(kind='bar', ax=ax)
    ax.set_title(categoria_selecionada)
    ax.set_xlabel('Sistema de abastecimento')
    ax.set_ylabel(metrica_traduzida) 
    st.pyplot(fig)
