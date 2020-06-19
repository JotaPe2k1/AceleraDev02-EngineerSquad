import streamlit as st
import pandas as pd


def main():
    st.image('logo.png')
    st.title('AceleraDev Data Science')
    st.header('Pré-processamento de dados em Python')
    file = st.file_uploader('Seleciona a base de dados (black_friday.csv)', type='csv')
    if file is not None:
        black_friday = pd.read_csv(file)
        st.header('Vizualização do DataFrame')
        numeros = st.slider('Escolha o numero de colunas que deseja ver', min_value=1, max_value=20)
        st.dataframe(black_friday.head(numeros))
        st.subheader('Questão 1')
        st.markdown('Quantas observações e quantas colunas há no dataset?')
        st.write(black_friday.shape)
        st.subheader('Questão 2')
        st.markdown('Há quantas mulheres com idade entre 26 e 35 anos no dataset?')
        st.write(black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age'] == '26-35')].shape[0])
        st.subheader('Questão 3')
        st.markdown('Quantos usuários únicos há no dataset?')
        st.write(black_friday['User_ID'].nunique())
        st.subheader('Questão 4')
        st.markdown('Quantos tipos de dados diferentes existem no dataset?')
        st.write(black_friday.dtypes.nunique())
        st.subheader('Questão 5')
        st.markdown('Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)?')
        st.write(float(black_friday.isna().any(axis=1).mean()))
        st.subheader('Questão 6')
        st.markdown('Quantos valores null existem na variável (coluna) com o maior número de null?')
        valores =  black_friday['Product_Category_3'].isna().sum()
        st.write(int(valores))
        st.subheader('Questão 7')
        st.markdown('Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`?')
        frequente = black_friday['Product_Category_3'].value_counts()
        st.write(int(frequente.index[0]))
        st.subheader('Questão 8')
        st.markdown('Qual a nova média da variável (coluna) `Purchase` após sua normalização?')
        normalizacao = ((black_friday['Purchase'] - black_friday['Purchase'].min()) / (
                    black_friday['Purchase'].max() - black_friday['Purchase'].min()))
        resposta = normalizacao.mean()
        st.write(float(resposta))
        st.subheader('Questão 9')
        st.markdown('Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização?')
        padronizacao = ((black_friday['Purchase'] - black_friday['Purchase'].mean()) / black_friday['Purchase'].std())
        resposta = ((padronizacao >= -1) & (padronizacao <= 1)).sum()
        st.write(int(resposta))
        st.subheader('Questão 10')
        st.markdown('Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`?')
        categoria_2 = black_friday['Product_Category_2'].isna()
        categoria_3 = black_friday['Product_Category_3'].isna()
        iguais = (categoria_2 & categoria_3)
        st.write(bool((iguais == categoria_2).all()))




if __name__ == '__main__':
    main()
