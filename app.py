import streamlit as st
import random

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Simulacros LIPASAM",
    page_icon="🚛",
    layout="centered"
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #0083B8;
        color: white;
        font-weight: bold;
    }
    .correct {
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        color: #155724;
        margin-top: 5px;
    }
    .incorrect {
        background-color: #f8d7da;
        padding: 10px;
        border-radius: 5px;
        color: #721c24;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIONES DE GENERACIÓN DE PREGUNTAS ---
def generar_pregunta(texto, correcta, distractores, tema):
    opciones = distractores + [correcta]
    random.shuffle(opciones)
    return {
        "pregunta": texto,
        "opciones": opciones,
        "correcta": correcta,
        "tema": tema
    }

def obtener_banco_preguntas():
    banco = []
    
    # === BLOQUE PRL ===
    # Distancias
    banco.append(generar_pregunta("¿Distancia mínima de seguridad con tendidos eléctricos (grúa)?", "7 metros", ["3 metros", "5 metros", "10 metros"], "PRL"))
    banco.append(generar_pregunta("¿Distancia mínima respecto a una carga suspendida?", "2 metros", ["1 metro", "5 metros", "No hay distancia"], "PRL"))
    
    # Viento y Grúa
    banco.append(generar_pregunta("¿Velocidad máxima de viento permitida para usar la grúa?", "50 km/h", ["30 km/h", "80 km/h", "40 km/h"], "PRL"))
    
    # RCP y Emergencias
    banco.append(generar_pregunta("Ritmo de RCP según el manual:", "1 insuflación : 5 compresiones", ["2 : 30", "2 : 15", "Solo compresiones"], "PRL"))
    banco.append(generar_pregunta("Significado de P.A.S.:", "Proteger, Avisar, Socorrer", ["Prevenir, Ayudar, Salvar", "Parar, Avisar, Salir", "Proteger, Ayudar, Socorrer"], "PRL"))
    
    # Incendios
    banco.append(generar_pregunta("Al usar extintor al aire libre, atacar el fuego:", "A favor del viento", ["Contra el viento", "Verticalmente", "Desde cualquier lado"], "PRL"))
    banco.append(generar_pregunta("Color de las señales de lucha contra incendios:", "Rojo (cuadrada/rectangular)", ["Verde", "Amarillo", "Azul"], "PRL"))
    
    # Señales
    banco.append(generar_pregunta("Señal redonda azul con pictograma blanco:", "Obligación", ["Prohibición", "Peligro", "Información"], "PRL"))
    banco.append(generar_pregunta("Señal triangular amarilla con borde negro:", "Advertencia de Peligro", ["Prohibición", "Socorro", "Obligación"], "PRL"))
    
    # Prohibiciones
    banco.append(generar_pregunta("Uso del móvil durante el repostaje:", "Terminantemente prohibido", ["Permitido para pagar", "Permitido si no hablas", "Solo para GPS"], "PRL"))
    banco.append(generar_pregunta("Fumar en el interior de vehículos:", "Prohibido", ["Permitido con ventana abierta", "Permitido si está parado", "Solo vapeadores"], "PRL"))
    banco.append(generar_pregunta("¿Se puede transportar gasolina en la cabina?", "No, prohibido", ["Sí, en envases homologados", "Sí, poca cantidad", "En el asiento copiloto"], "PRL"))
    
    # Químicos y Salud
    banco.append(generar_pregunta("Pictograma 'Llama sobre círculo':", "Comburente", ["Inflamable", "Explosivo", "Gas a presión"], "PRL"))
    banco.append(generar_pregunta("Vacunas recomendadas para riesgo biológico:", "Tétanos y Hepatitis B", ["Gripe", "COVID-19", "Fiebre Amarilla"], "PRL"))
    
    # Otros PRL
    banco.append(generar_pregunta("Distancia seguridad descarga en vertedero:", "Vehículo nivelado y distancia prudencial al borde", ["Inclinado hacia atrás", "Cerca del borde", "Motor apagado"], "PRL"))
    banco.append(generar_pregunta("Mascarilla para polvo:", "FFP2 (EN149)", ["Quirúrgica", "De tela", "FFP1"], "PRL"))
    banco.append(generar_pregunta("¿Qué es un Incidente?", "Suceso peligroso sin daños reales", ["Accidente con baja", "Enfermedad profesional", "Una avería mecánica"], "PRL"))
    
    # === BLOQUE CONDUCCIÓN EFICIENTE (ECO) ===
    banco.append(generar_pregunta("Temperatura ideal climatizador:", "23 - 24 ºC", ["18 - 20 ºC", "21 - 22 ºC", "25 - 26 ºC"], "ECO"))
    banco.append(generar_pregunta("Apagar motor en paradas superiores a:", "60 segundos", ["10 segundos", "30 segundos", "2 minutos"], "ECO"))
    banco.append(generar_pregunta("Uso de la 1ª marcha:", "Solo para iniciar el movimiento (2-3 metros)", ["Para subir cuestas", "Hasta 20 km/h", "Para aparcar"], "ECO"))
    banco.append(generar_pregunta("Aumento consumo por falta presión neumáticos:", "5 - 7%", ["1 - 2%", "10 - 15%", "No afecta"], "ECO"))
    banco.append(generar_pregunta("Aumento consumo al pasar de 90 a 100 km/h:", "5%", ["10%", "15%", "2%"], "ECO"))
    banco.append(generar_pregunta("Consumo nulo se logra:", "Más de 20km/h, marcha engranada, sin acelerar", ["En punto muerto", "Al ralentí", "Frenando fuerte"], "ECO"))
    banco.append(generar_pregunta("En bajadas se recomienda:", "Aprovechar inercia con marcha puesta", ["Poner punto muerto", "Apagar motor", "Pisar embrague"], "ECO"))
    banco.append(generar_pregunta("Arranque motor diésel moderno:", "Esperar unos segundos sin acelerar", "Acelerar a fondo", "Bombear acelerador", "ECO"))

    return banco

def crear_examen_nuevo():
    # Obtener banco completo
    banco = obtener_banco_preguntas()
    
    # Separar por temas
    prl = [p for p in banco if p['tema'] == "PRL"]
    eco = [p for p in banco if p['tema'] == "ECO"]
    
    # Seleccionar aleatoriamente (asegurando unicidad si hay suficientes)
    # Nota: Aquí simulamos selección. En producción, expandir el banco para tener >20 PRL y >4 ECO únicas.
    # Usamos random.choices si el banco es pequeño para permitir repetir, o sample si es grande.
    # Dado el ejemplo pequeño arriba, usaremos choices para que no falle el código, 
    # pero TU OBJETIVO es añadir más preguntas al banco.
    
    seleccion_prl = random.choices(prl, k=20) 
    seleccion_eco = random.choices(eco, k=4)
    
    examen = seleccion_prl + seleccion_eco
    random.shuffle(examen)
    return examen

# --- GESTIÓN DEL ESTADO (MEMORIA DE LA APP) ---
if 'examen_actual' not in st.session_state:
    st.session_state.examen_actual = None
if 'respuestas_usuario' not in st.session_state:
    st.session_state.respuestas_usuario = {}
if 'corregido' not in st.session_state:
    st.session_state.corregido = False

# --- INTERFAZ BARRA LATERAL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2933/2933116.png", width=100) # Icono genérico test
    st.title("Panel de Control")
    st.write("Genera test infinitos basados en el manual de Conductor de LIPASAM.")
    
    if st.button("🔄 GENERAR NUEVO SIMULACRO"):
        st.session_state.examen_actual = crear_examen_nuevo()
        st.session_state.respuestas_usuario = {}
        st.session_state.corregido = False
        st.rerun()

    st.info("💡 **Tip:** Usa este menú para crear un examen distinto cada vez.")

# --- INTERFAZ PRINCIPAL ---
st.title("🚛 Simulacro Examen Conductor")

if st.session_state.examen_actual is None:
    st.info("👋 ¡Bienvenido! Pulsa el botón en el menú lateral o abajo para comenzar un examen.")
    if st.button("INICIAR PRIMER TEST"):
        st.session_state.examen_actual = crear_examen_nuevo()
        st.rerun()

else:
    # Mostrar Preguntas
    st.write(f"📝 **Simulacro Generado** (24 Preguntas)")
    st.write("---")
    
    examen = st.session_state.examen_actual
    aciertos = 0
    
    with st.form("form_examen"):
        for i, p in enumerate(examen):
            # Etiqueta de tema
            color_tag = "orange" if p['tema'] == "PRL" else "green"
            st.markdown(f"**:{color_tag}[{p['tema']}] Pregunta {i+1}:** {p['pregunta']}")
            
            # Opciones (Radio button)
            # Usamos una clave única para mantener la selección
            seleccion = st.radio(
                "Selecciona una opción:", 
                p['opciones'], 
                key=f"p_{i}", 
                index=None,
                disabled=st.session_state.corregido,
                label_visibility="collapsed"
            )
            
            # Lógica de corrección visual (solo si está corregido)
            if st.session_state.corregido:
                if seleccion == p['correcta']:
                    st.markdown(f"<div class='correct'>✅ ¡Correcto!</div>", unsafe_allow_html=True)
                    aciertos += 1
                else:
                    st.markdown(f"<div class='incorrect'>❌ Tu respuesta: {seleccion if seleccion else 'En blanco'}<br>👉 <b>Correcta:</b> {p['correcta']}</div>", unsafe_allow_html=True)
            
            st.write("---")
        
        # Botón de corrección
        enviado = st.form_submit_button("✅ CORREGIR EXAMEN", disabled=st.session_state.corregido)
        
        if enviado:
            st.session_state.corregido = True
            st.rerun()

    # Mostrar Nota Final
    if st.session_state.corregido:
        nota = (aciertos / 24) * 10
        st.header(f"📊 RESULTADO FINAL: {aciertos} / 24")
        st.subheader(f"Nota: {nota:.2f}")
        
        if aciertos >= 12:
            st.balloons()
            st.success("🎉 ¡ENHORABUENA! HAS APROBADO.")
        else:
            st.error("⚠️ NO APTO. Necesitas repasar un poco más.")
        
        if st.button("🔄 INTENTAR OTRO EXAMEN"):
            st.session_state.examen_actual = crear_examen_nuevo()
            st.session_state.respuestas_usuario = {}
            st.session_state.corregido = False
            st.rerun()