import streamlit as st

# Navigation dictionary to structure pages and their titles/icons
pages = {
    "Información": [
        {"page": "vistas/home.py", "title": "Inicio", "icon": "🏠"},
        {"page": "vistas/acerca_de.py", "title": "Acerca de", "icon": "👤"},
    ],
    "Proyectos": [
        {"page": "vistas/ventas.py", "title": "Ventas", "icon": "💼"},
        {"page": "vistas/chatbot.py", "title": "Chat Bot", "icon": "🤖"},
    ]
}

# Sidebar with navigation
st.sidebar.title("Navegación")
selection = st.sidebar.radio(
    "Seleccione una página:",
    [page["title"] for category in pages.values() for page in category]
)

# Page content logic
if selection == "Inicio":
    st.title("Inicio")
    # Include content or import for `home.py`
    # Example: st.write("Welcome to the home page.")
elif selection == "Acerca de":
    st.title("Acerca de")
    # Include content or import for `acerca_de.py`
elif selection == "Ventas":
    st.title("Ventas")
    # Include content or import for `ventas.py`
elif selection == "Chat Bot":
    st.title("Chat Bot")
    # Include content or import for `chatbot.py`

# --- Logo and Credits ---
st.sidebar.image("img/chatbot.png", use_column_width=True)
st.sidebar.markdown("Elaborado con ❤️ por [Streamlit](https://streamlit.io/gallery)")
