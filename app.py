import streamlit as st
import random
import requests

 
st.set_page_config(
    page_title='🎯 Rick y Morty',
    page_icon='🏆',
    layout='centered'
)

# funcion que devuelve el id
def get_rick_morty_id(id):
    resp = requests.get(f'https://rickandmortyapi.com/api/character/{id}')
    return resp.json() if resp.status_code == 200 else None

# funcion para obtener el nombre
def get_rick_morty_data(name_filter):
    url = 'https://rickandmortyapi.com/api/character'
    params = {'name': name_filter}
    results = []
    
    while url:
        resp = requests.get(url, params=params)
        if resp.status_code != 200:
            return []
        data = resp.json()
        results.extend(data.get('results', []))
        url= data['info']['next']
        params= None
    return results

# función para obtener un personaje aleatorio 
def get_random_rick_morty():
    random_id = random.randint(1,826)
    return get_rick_morty_id(str(random_id))    

# Título y descripción
st.title('🧬🧪 Rick y Morty 🧫🔬')
st.markdown('Descubre información sobre tu personaje favorito o encuentra uno al azar')


# columnas para la busqueda y el botón aleatorio
col1,col2 = st.columns([2,1])
with col1:
    rick_and_morty_name = st.text_input('Ingresa el Nombre del personaje: ', '')
    
with col2:
    random_button = st.button('🎲 Personaje Aleatorio')    

rick_morty = None

# Manejar la búsqueda y el boton aleatorio
if rick_and_morty_name:
    results = get_rick_morty_data(rick_and_morty_name)
    if results:
        rick_morty = results[0]
elif random_button:
    rick_morty = get_random_rick_morty()

# Mostrar la información del personje
if rick_morty:
    # Crear dos columnas para la imagen y la información
    
    img_col, info_col = st.columns([3,2])
    
    with img_col:
        st.image(
            rick_morty['image'], 
            caption=f'# {rick_morty['id']} {rick_morty['name']}',
            use_container_width=True    
        )
    
    with info_col:
        
        # Estilo CSS para los textos
        st.markdown(
            """
            <style>
            .custom-label {
                font-size: 14px;
                color: gray;
                margin: 0;
            }
            .custom-value {
                font-size: 18px;
                color: skyblue;
                font-weight: bold;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        for label, value in [
            ("Nombre", rick_morty["name"]),
            ("Status", rick_morty["status"]),
            ("Especie", rick_morty["species"]),
            ("Género", rick_morty["gender"]),
            ("Origen", rick_morty["origin"]["name"]),
            ("Ubicación", rick_morty["location"]["name"]),
            ("Episodios", len(rick_morty["episode"]))
        ]:
            st.markdown(
                f'<p class="custom-label">{label}:</p>'
                f'<p class="custom-value">{value}</p>',
                unsafe_allow_html=True
            )

elif rick_and_morty_name:
    st.error('No se encontró ningún personaje con ese nombre.')
else:
    st.info('✍ Ingresa el Nombre de un Personaje o intenta con uno aleatorio')
