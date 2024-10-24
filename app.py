import streamlit as st
from datetime import date, datetime

def main ():
    st.title('PipLine-V')
    email = st.text_input('E-mail: ')
    data = st.date_input('Data de Venda', datetime.now())
    hora = st.time_input('Hora da Venda', value=datetime.today())
    valor = st.number_input('Valor da Venda ', min_value=0.0,  format="%.2f", step= 0.50)
    quantidade = st.number_input('Quantidade de Produtos ', min_value = 0, step= 1)
    produto = st.selectbox(' Produto Vendido', ['','Camista', 'Cueca', 'Bermuda'])
    
    if st.button('Salvar'):
        st.write(email)
        st.write('f {data}')

if __name__ == '__main__':
    main()