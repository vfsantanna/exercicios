import streamlit as st
import pandas as pd
import numpy as np



# 1. Adicionar um título
st.header('O que podemos fazer com o Streamlit?')

# 2. Adicionar um subtítulo
st.subheader('Caderno de exercícios EBAC - Aluna: Vivian Sant Anna!!!')

# 3. Adicionar um texto
st.text('Streamlit transforma scripts em web apps compartilháveis em minutos. ')

# 4 Adicionar um link
st.markdown('[Ir para a página inicial do Google](https://www.google.com)')

# 5. Adicionar um botão
if st.button('Clique aqui'):
    st.write('Botão clicado!')

# 6. Adicionar uma caixa de seleção
option = st.checkbox('Opção')
if option:
    st.write('Opção selecionada!')

# 7. Adicionar um campo de texto
text_input = st.text_input('Digite algo')
st.write('Você digitou:', text_input)

# 8. Adicionar um campo de senha
password_input = st.text_input('Digite sua senha', type='password')

# 9. Adicionar um campo de número
number_input = st.number_input('Digite um número')
st.write('O número digitado é:', number_input)

# 10. Adicionar um campo de data
date_input = st.date_input('Selecione uma data')
st.write('A data selecionada é:', date_input)

# 11. Adicionar um campo de hora
time_input = st.time_input('Selecione uma hora')
st.write('A hora selecionada é:', time_input)

# 12. Adicionar um campo de seleção
option = st.selectbox('Selecione uma opção', ['Opção 1', 'Opção 2', 'Opção 3'])
st.write('A opção selecionada é:', option)

# 13. Adicionar um campo de seleção múltipla
options = st.multiselect('Selecione uma ou mais opções', ['Opção 1', 'Opção 2', 'Opção 3'])
st.write('As opções selecionadas são:', options)

# 14. Adicionar um slider
slider_value = st.slider('Selecione um valor', min_value=0, max_value=100, step=1)
st.write('O valor selecionado é:', slider_value)

# 15. Adicionar um gráfico de linha
data = [1, 2, 3, 4, 5]
st.line_chart(data)

# 16. Adicionar um gráfico de barras
data = {'Categoria 1': 10, 'Categoria 2': 20, 'Categoria 3': 30}
st.bar_chart(data)

# 17. Adicionar um gráfico de área
data = [1, 2, 3, 4, 5]
st.area_chart(data)

# 18. Adicionar uma tabela
data = {'Coluna 1': [1, 2, 3], 'Coluna 2': [4, 5, 6], 'Coluna 3': [7, 8, 9]}
st.table(data)

# 19. Adicionar um campo de arquivo
file = st.file_uploader('Selecione um arquivo')

# 20. Adicionar um botão de rádio
radio_option = st.radio('Selecione uma opção', ['Opção 1', 'Opção 2', 'Opção 3'])
st.write('A opção selecionada é:', radio_option)

# 21. Adicionar um botão de alternância
toggle_option = st.checkbox('Alternar')
if toggle_option:
    st.write('Alternância ativada!')

# 22. Adicionar um campo de seleção de cor
color_option = st.color_picker('Selecione uma cor', '#FF0000')
st.write('A cor selecionada é:', color_option)

# 23. Adicionar um campo de seleção de arquivo
file_option = st.file_selector('Selecione um arquivo')
st.write('O arquivo selecionado é:', file_option)

# 24. Adicionar um campo de seleção de intervalo
range_option = st.slider('Selecione um intervalo', min_value=0.0, max_value=1.0, step=0.1)
st.write('O intervalo selecionado é:', range_option)

# 25. Adicionar um campo de seleção de data e hora
datetime_option = st.datetime_input('Selecione uma data e hora')
st.write('A data e hora selecionadas são:', datetime_option)

# 26. Adicionar um campo de seleção de número com incremento
number_option = st.number_input('Selecione um número', min_value=0, max_value=10, step=0.5)
st.write('O número selecionado é:', number_option)

# 27. Adicionar um campo de seleção de opções com pesquisa
search_option = st.selectbox('Selecione uma opção', ['Opção 1', 'Opção 2', 'Opção 3'], index=0)
st.write('A opção selecionada é:', search_option)

# 28. Adicionar um campo de seleção de arquivo com múltipla escolha
files_option = st.multiselect('Selecione um ou mais arquivos', ['Arquivo 1', 'Arquivo 2', 'Arquivo 3'])
st.write('Os arquivos selecionados são:', files_option)