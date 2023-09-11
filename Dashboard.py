import streamlit as st
import pandas as pd


st.set_page_config(layout= 'wide')

st.title('Pelada de Sábado')



# importar os dados

tabela = pd.read_csv('https://raw.githubusercontent.com/Fernando-Almeida23/Pelada_sabado/main/pelada_sabado_02_semestre.csv')
tabela.drop(axis = 1, columns = 'Unnamed: 0', inplace = True)

# # Arrumando tabela

# Somar todos as colunas de acordo com os jogadores
tabela = tabela.groupby('Jogadores').sum()


# Somar os pontos
tabela['Pontos'] = (tabela['Vitorias'] * 3) + tabela['Empate'] - tabela['Derrotas']

# Resetar os indice colocando os jogadores como coluna
tabela.reset_index(inplace= True)

numero_tabela_geral = tabela['Jogadores'].count()
numero_tabela_geral

# Lista de jogadores mensais
mensal = ['David',
    'Marcelão',
    'Boneco',
    'Marcos',
    'Ismael',
    'Leandrinho',
    'Guinha',
    'Philipe',
    'Cabeleira',
    'Corinthiano',
    'Peixe',
    'Joazinho',
    'Athos',
    'Jorge',
    'Euller',
    'Juscielio',
    'Michel',
    'Davidson',
    'Du',
    'Ranyeri']
mensal_selecao = tabela['Jogadores'].isin(mensal)
tabela_mensal = tabela[mensal_selecao]
tabela_mensal.drop(axis = 1, columns = 'Gols Sofridos', inplace = True)

numero_jogadores = tabela['Jogadores'].count()

# Separando baseado em melhor jogador do sabado
craque_do_dia = tabela.loc[:,['Jogadores','Craque do Dia']]
craque_do_dia.sort_values(by = 'Craque do Dia', ascending= False, inplace = True)
craque_do_dia.index = range(1, (numero_jogadores+1))

# Lista de goleiros
goleiros = ['Matheus',
            'Alan',
            'Igor',
            'Ochoa',
            'Marco Aurelio',
           'Milton',
            'Caio',
            'Lucian',
            'Chelin']
goleiro_selecao = tabela['Jogadores'].isin(goleiros)
tabela_goleiro = tabela[goleiro_selecao]
tabela_goleiro.drop(axis = 1, columns = ['Tarde de Vitoria', 'La barca', 'Craque do Dia'], inplace = True)
tabela_goleiro['Media Gols'] = tabela_goleiro['Gols Sofridos'] / tabela_goleiro['Partidas']
tabela_goleiro['Media Gols'] = round(tabela_goleiro['Media Gols'], 2)

tabela_selecao_avulso = tabela['Jogadores'].isin(goleiros)
tabela = tabela[-tabela_selecao_avulso]

tabela.drop(axis = 1, columns = 'Gols Sofridos', inplace = True)

# contando quantos jogadores tem em cada tabela
numero_jogadores = tabela['Jogadores'].count()
numero_jogadores_mensal = tabela_mensal['Jogadores'].count()
numero_goleiro = tabela_goleiro['Jogadores'].count()

# Ordenando de acordo com os pontos do maior para o menor
tabela_mensal.sort_values(by = 'Pontos', ascending= False, inplace = True)
tabela.sort_values(by = 'Pontos', ascending= False, inplace = True)
tabela_goleiro.sort_values(by = 'Pontos', ascending= False, inplace = True)

# Resetando os indices comecando do 1
tabela.index = range(1,(numero_jogadores+1))
tabela_mensal.index = range(1,(numero_jogadores_mensal+1))
tabela_goleiro.index = range(1,(numero_goleiro+1))

# Separando baseado em gols
artileiro = tabela.loc[:,['Jogadores','Gols']]
artileiro.sort_values(by = 'Gols', ascending= False, inplace = True)
artileiro.index = range(1, (numero_jogadores+1))

artileiro_mensal = tabela_mensal.loc[:,['Jogadores','Gols']]
artileiro_mensal.sort_values(by = 'Gols', ascending= False, inplace = True)
artileiro_mensal.index = range(1, (numero_jogadores_mensal+1))

# Separando baseado em tarde de vitorias
tarde_vitoria = tabela.loc[:,['Jogadores','Tarde de Vitoria']]
tarde_vitoria.sort_values(by = 'Tarde de Vitoria', ascending= False, inplace = True)
tarde_vitoria.index = range(1, (numero_jogadores+1))

tarde_vitoria_mensal = tabela_mensal.loc[:,['Jogadores','Tarde de Vitoria']]
tarde_vitoria_mensal.sort_values(by = 'Tarde de Vitoria', ascending= False, inplace = True)
tarde_vitoria_mensal.index = range(1, (numero_jogadores_mensal+1))

# Separando baseado em la barca
la_barca = tabela.loc[:,['Jogadores','La barca']]
la_barca.sort_values(by = 'La barca', ascending= False, inplace = True)
la_barca.index = range(1, (numero_jogadores+1))

la_barca_mensal = tabela_mensal.loc[:,['Jogadores','La barca']]
la_barca_mensal.sort_values(by = 'La barca', ascending= False, inplace = True)
la_barca_mensal.index = range(1, (numero_jogadores_mensal+1))

# Separando baseado em gols sofridos
gols_sofridos_media = tabela_goleiro.loc[:,['Jogadores','Media Gols']]
gols_sofridos_media.sort_values(by = 'Media Gols', ascending= True, inplace = True)
gols_sofridos_media.index = range(1, (numero_goleiro+1))


# # Funções Colorir tabela

def mudar_cor_tabela(linha):
    if linha['Jogadores'] == tabela['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == tabela['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,10):
                    if linha['Jogadores'] == tabela['Jogadores'][numero_jogadores-w]:
                        return ['background-color: red'] * len(linha)


def mudar_cor_goleiro(linha):
    if linha['Jogadores'] == tabela_goleiro['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        if linha['Jogadores'] == tabela_goleiro['Jogadores'][numero_goleiro]:
                return ['background-color: red'] * len(linha)

def mudar_cor_mensal(linha):
    if linha['Jogadores'] == tabela_mensal['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == tabela_mensal['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,4):
                    if linha['Jogadores'] == tabela_mensal['Jogadores'][numero_jogadores_mensal-w]:
                        return ['background-color: red'] * len(linha)


def mudar_cor_artileiro(linha):
    if linha['Jogadores'] == artileiro['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == artileiro['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,10):
                    if linha['Jogadores'] == artileiro['Jogadores'][numero_jogadores-w]:
                        return ['background-color: red'] * len(linha)


def mudar_cor_artileiro_mensal(linha):
    if linha['Jogadores'] == artileiro_mensal['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == artileiro_mensal['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,4):
                    if linha['Jogadores'] == artileiro_mensal['Jogadores'][numero_jogadores_mensal-w]:
                        return ['background-color: red'] * len(linha)


def mudar_cor_tarde_vitoria(linha):
    if linha['Jogadores'] == tarde_vitoria['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == tarde_vitoria['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,10):
                    if linha['Jogadores'] == tarde_vitoria['Jogadores'][numero_jogadores-w]:
                        return ['background-color: red'] * len(linha)


def mudar_cor_tarde_vitoria_mensal(linha):
    if linha['Jogadores'] == tarde_vitoria_mensal['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == tarde_vitoria_mensal['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,4):
                    if linha['Jogadores'] == tarde_vitoria_mensal['Jogadores'][numero_jogadores_mensal-w]:
                        return ['background-color: red'] * len(linha)


def mudar_cor_la_barca(linha):
    if linha['Jogadores'] == la_barca['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == la_barca['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,10):
                    if linha['Jogadores'] == la_barca['Jogadores'][numero_jogadores-w]:
                        return ['background-color: red'] * len(linha)


def mudar_cor_la_barca_mensal(linha):
    if linha['Jogadores'] == la_barca_mensal['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == la_barca_mensal['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,4):
                    if linha['Jogadores'] == la_barca_mensal['Jogadores'][numero_jogadores_mensal-w]:
                        return ['background-color: red'] * len(linha)

def mudar_cor_craque_do_dia(linha):
    if linha['Jogadores'] == craque_do_dia['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        for i in range(2,6):
            if linha['Jogadores'] == craque_do_dia['Jogadores'][i]:
                return ['background-color: yellow'] * len(linha)
            else:
                for w in range(0,10):
                    if linha['Jogadores'] == craque_do_dia['Jogadores'][numero_tabela_geral-w]:
                        return ['background-color: red'] * len(linha)

def mudar_cor_goleiro_gols_sofrido(linha):
    if linha['Jogadores'] == gols_sofridos_media['Jogadores'][1]:
        return ['background-color: lime'] * len(linha)
    else:
        if linha['Jogadores'] == gols_sofridos_media['Jogadores'][numero_goleiro]:
                return ['background-color: red'] * len(linha)

aba1, aba2, aba3 = st.tabs(['Mensal','Goleiro','Geral'])


# # Tabela Mensal Visualização
with aba1:
    st.write('Tabela Mensal')
    st.dataframe(data=tabela_mensal.style.apply(axis=1, func=mudar_cor_mensal), height=750)
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.write('Artileiro')
        st.dataframe(data = artileiro_mensal.style.apply(axis=1, func = mudar_cor_artileiro_mensal), height= 750)
        st.write('La barca')
        st.dataframe(data=la_barca_mensal.style.apply(axis=1, func=mudar_cor_la_barca_mensal), height=750)
    with coluna2:
        st.write('Tarde de Vitoria')
        st.dataframe(data = tarde_vitoria_mensal.style.apply(axis=1, func = mudar_cor_tarde_vitoria_mensal), height=750)
        st.write('Craque do Dia')
        st.dataframe(data=craque_do_dia.style.apply(axis=1, func=mudar_cor_craque_do_dia), height=1400)

with aba2:
    st.write('Goleiros Geral')
    st.dataframe(data = tabela_goleiro.style.apply(axis=1, func = mudar_cor_goleiro), height=250)
    st.write('Media de gols sofridos')
    st.dataframe(data = gols_sofridos_media.style.apply(axis=1, func = mudar_cor_goleiro_gols_sofrido), height=250)

with aba3:
    st.write('Tabela Geral')
    st.dataframe(data=tabela.style.apply(axis=1, func = mudar_cor_tabela), height=1200)
    coluna1, coluna2, coluna3 = st.columns(3)
    with coluna1:
        st.write('Artileiro Geral')
        st.dataframe(data = artileiro.style.apply(axis=1, func = mudar_cor_artileiro), height= 1200)

    with coluna2:
        st.write('Tarde de Vitoria Geral')
        st.dataframe(data = tarde_vitoria.style.apply(axis=1, func = mudar_cor_tarde_vitoria), height=1200)

    with coluna3:
        st.write('La barca Geral')
        st.dataframe(data=la_barca.style.apply(axis=1, func = mudar_cor_la_barca), height=1200)

