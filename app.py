import streamlit as st
import random

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Simulacros LIPASAM",
    page_icon="🚛",
    layout="centered"
)

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #0083B8;
        color: white;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
    }
    .correct {
        background-color: #d4edda;
        padding: 15px;
        border-radius: 8px;
        color: #155724;
        margin-top: 10px;
        border: 1px solid #c3e6cb;
    }
    .incorrect {
        background-color: #f8d7da;
        padding: 15px;
        border-radius: 8px;
        color: #721c24;
        margin-top: 10px;
        border: 1px solid #f5c6cb;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIONES ---
def generar_pregunta(texto, correcta, distractores, tema):
    opciones = distractores + [correcta]
    random.shuffle(opciones)
    return {
        "pregunta": texto,
        "opciones": opciones,
        "correcta": correcta,
        "tema": tema
    }

def obtener_banco_preguntas_ampliado():
    banco = []
    
    # =================================================
    # BANCO DE PREGUNTAS (AMPLIADO PARA EVITAR REPETICIONES)
    # =================================================
    
    # --- BLOQUE PRL (Necesitamos al menos 20, ponemos 30+) ---
    
    # Distancias y Grúa
    banco.append(generar_pregunta("¿Distancia mínima de seguridad con tendidos eléctricos (grúa)?", "7 metros", ["3 metros", "5 metros", "10 metros"], "PRL"))
    banco.append(generar_pregunta("¿Distancia mínima respecto a una carga suspendida?", "2 metros", ["1 metro", "5 metros", "No hay distancia"], "PRL"))
    banco.append(generar_pregunta("¿Velocidad máxima de viento permitida para usar la grúa?", "50 km/h", ["30 km/h", "80 km/h", "40 km/h"], "PRL"))
    banco.append(generar_pregunta("Si la carga oscila durante la maniobra con grúa:", "Usar cuerdas guía desde distancia segura", ["Sujetarla con las manos", "Acelerar la maniobra", "Subirse a la carga"], "PRL"))

    # Emergencias (PAS, RCP, Fuego)
    banco.append(generar_pregunta("Ritmo de RCP según el manual:", "1 insuflación : 5 compresiones", ["2 : 30", "2 : 15", "Solo compresiones"], "PRL"))
    banco.append(generar_pregunta("Secuencia correcta P.A.S.:", "Proteger, Avisar, Socorrer", ["Prevenir, Ayudar, Salvar", "Parar, Avisar, Salir", "Proteger, Ayudar, Socorrer"], "PRL"))
    banco.append(generar_pregunta("Al usar extintor al aire libre, atacar el fuego:", "A favor del viento", ["Contra el viento", "Verticalmente", "Desde cualquier lado"], "PRL"))
    banco.append(generar_pregunta("El extintor de CO2 se caracteriza por:", "No tener manómetro", ["Ser de color verde", "Ser exclusivo para madera", "Tener manguera transparente"], "PRL"))
    banco.append(generar_pregunta("Ante una hemorragia externa:", "Presión directa sobre la herida con gasas", ["Hacer torniquete inmediato", "Dar alcohol", "Dejar secar al aire"], "PRL"))
    banco.append(generar_pregunta("Posición de espera ante un desmayo (sin traumatismo):", "Tumbado con piernas elevadas", ["Sentado", "De pie", "Boca abajo"], "PRL"))

    # Señalización
    banco.append(generar_pregunta("Señal redonda azul con pictograma blanco:", "Obligación", ["Prohibición", "Peligro", "Información"], "PRL"))
    banco.append(generar_pregunta("Señal triangular amarilla con borde negro:", "Advertencia de Peligro", ["Prohibición", "Socorro", "Obligación"], "PRL"))
    banco.append(generar_pregunta("Señal cuadrada o rectangular ROJA:", "Lucha contra incendios", ["Salvamento", "Prohibición", "Obligación"], "PRL"))
    banco.append(generar_pregunta("Señal cuadrada o rectangular VERDE:", "Salvamento y socorro", ["Incendios", "Peligro", "Información turística"], "PRL"))
    banco.append(generar_pregunta("Señal redonda blanca con borde rojo:", "Prohibición", ["Peligro", "Obligación", "Fin de prohibición"], "PRL"))
    
    # Riesgos Específicos y Normas
    banco.append(generar_pregunta("Uso del móvil durante el repostaje:", "Terminantemente prohibido", ["Permitido para pagar", "Permitido si no hablas", "Solo para GPS"], "PRL"))
    banco.append(generar_pregunta("Fumar en el interior de vehículos:", "Prohibido", ["Permitido con ventana abierta", "Permitido si está parado", "Solo vapeadores"], "PRL"))
    banco.append(generar_pregunta("¿Se puede transportar gasolina en la cabina?", "No, prohibido", ["Sí, en envases homologados", "Sí, poca cantidad", "En el asiento copiloto"], "PRL"))
    banco.append(generar_pregunta("Al bajar de la cabina del camión:", "De cara al interior, usando asideros", ["De cara al exterior", "Saltando con cuidado", "Deslizándose"], "PRL"))
    banco.append(generar_pregunta("¿Qué es un 'Incidente'?", "Suceso peligroso sin daños reales", ["Accidente con baja", "Enfermedad profesional", "Una avería mecánica"], "PRL"))
    banco.append(generar_pregunta("Si un contenedor vuelca dentro de la tolva:", "Usar procedimiento de rescate (Prohibido entrar)", ["Entrar a sacarlo rápido", "Empujarlo con los pies", "Subirse al borde"], "PRL"))
    banco.append(generar_pregunta("Antes de cerrar el portón trasero (tailgate):", "Separar el camión del obstáculo/muelle", ["Acelerar", "Pitar 3 veces", "Mirar solo el espejo derecho"], "PRL"))
    banco.append(generar_pregunta("Subir personas en la cuchara de la pala cargadora:", "Totalmente prohibido", ["Permitido si es poca altura", "Permitido con arnés", "Solo encargados"], "PRL"))

    # Salud y EPIs
    banco.append(generar_pregunta("Vacunas recomendadas para riesgo biológico:", "Tétanos y Hepatitis B", ["Gripe", "COVID-19", "Fiebre Amarilla"], "PRL"))
    banco.append(generar_pregunta("Mascarilla recomendada para polvo:", "FFP2 (EN149)", ["Quirúrgica", "De tela", "FFP1"], "PRL"))
    banco.append(generar_pregunta("Norma del calzado de seguridad:", "EN 20345", ["EN 388", "EN 166", "EN 397"], "PRL"))
    banco.append(generar_pregunta("¿Cuándo usar chaleco de alta visibilidad?", "Siempre en zonas de tráfico (día y noche)", ["Solo de noche", "Solo con niebla", "Es opcional"], "PRL"))
    banco.append(generar_pregunta("Riesgo 'Cronoestrés' se asocia a:", "Trabajo a turnos y nocturnidad", ["Trabajo físico", "Conducción en lluvia", "Ruido"], "PRL"))
    banco.append(generar_pregunta("Pictograma 'Llama sobre círculo':", "Comburente", ["Inflamable", "Explosivo", "Gas a presión"], "PRL"))
    banco.append(generar_pregunta("Al manipular cargas manualmente, la espalda debe estar:", "Recta", ["Curvada", "Girada", "Relajada"], "PRL"))

    # --- BLOQUE CONDUCCIÓN EFICIENTE (Necesitamos al menos 4, ponemos 10) ---
    banco.append(generar_pregunta("Temperatura ideal climatizador:", "23 - 24 ºC", ["18 - 20 ºC", "21 - 22 ºC", "25 - 26 ºC"], "ECO"))
    banco.append(generar_pregunta("Apagar motor en paradas superiores a:", "60 segundos", ["10 segundos", "30 segundos", "2 minutos"], "ECO"))
    banco.append(generar_pregunta("Uso de la 1ª marcha:", "Solo para iniciar el movimiento (2-3 metros)", ["Para subir cuestas", "Hasta 20 km/h", "Para aparcar"], "ECO"))
    banco.append(generar_pregunta("Aumento consumo por falta presión neumáticos:", "5 - 7%", ["1 - 2%", "10 - 15%", "No afecta"], "ECO"))
    banco.append(generar_pregunta("Aumento consumo al pasar de 90 a 100 km/h:", "5%", ["10%", "15%", "2%"], "ECO"))
    banco.append(generar_pregunta("Consumo nulo se logra:", "Más de 20km/h, marcha engranada, sin acelerar", ["En punto muerto", "Al ralentí", "Frenando fuerte"], "ECO"))
    banco.append(generar_pregunta("En bajadas se recomienda:", "Aprovechar inercia con marcha puesta", ["Poner punto muerto", "Apagar motor", "Pisar embrague"], "ECO"))
    banco.append(generar_pregunta("Arranque motor diésel moderno:", "Esperar unos segundos sin acelerar", ["Acelerar a fondo", "Bombear acelerador"], "ECO"))
    banco.append(generar_pregunta("En subidas, usar:", "Marcha más larga posible + acelerador pisado", ["Marcha corta + revoluciones altas", "Punto muerto", "Acelerador a fondo en 1ª"], "ECO"))
    banco.append(generar_pregunta("Anticipación en la conducción:", "Evita frenazos y acelerones (ahorra combustible)", ["Permite llegar antes", "Es más peligroso", "Aumenta el estrés"], "ECO"))

    return banco

def crear_examen_nuevo():
    banco = obtener_banco_preguntas_ampliado()
    
    # Separar temas
    prl = [p for p in banco if p['tema'] == "PRL"]
    eco = [p for p in banco if p['tema'] == "ECO"]
    
    # === LA CLAVE: USAR RANDOM.SAMPLE PARA EVITAR REPETICIONES ===
    # Tomamos 20 de PRL y 4 de ECO sin reemplazo (no se repiten)
    # Si por error el banco fuera pequeño, cogemos el máximo posible para no dar error
    num_prl = min(len(prl), 20)
    num_eco = min(len(eco), 4)
    
    seleccion_prl = random.sample(prl, k=num_prl)
    seleccion_eco = random.sample(eco, k=num_eco)
    
    examen = seleccion_prl + seleccion_eco
    random.shuffle(examen)
    return examen

# --- GESTIÓN DE SESIÓN ---
if 'examen_actual' not in st.session_state:
    st.session_state.examen_actual = None
if 'corregido' not in st.session_state:
    st.session_state.corregido = False
if 'num_test' not in st.session_state:
    st.session_state.num_test = 0

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("Panel de Control")
    st.write(f"Test realizados en esta sesión: **{st.session_state.num_test}**")
    
    if st.button("🔄 GENERAR NUEVO SIMULACRO", type="primary"):
        st.session_state.examen_actual = crear_examen_nuevo()
        st.session_state.corregido = False
        st.session_state.num_test += 1
        st.rerun()

    st.info("ℹ️ Cada vez que pulsas el botón, se eligen 24 preguntas nuevas y únicas.")

# --- CUERPO PRINCIPAL ---
st.title("🚛 Simulacro Conductor LIPASAM")

if st.session_state.examen_actual is None:
    st.info("👋 Bienvenido. Pulsa el botón para generar tu primer examen sin preguntas repetidas.")
    if st.button("INICIAR"):
        st.session_state.examen_actual = crear_examen_nuevo()
        st.session_state.num_test += 1
        st.rerun()

else:
    examen = st.session_state.examen_actual
    
    # Formulario
    with st.form("form_examen"):
        aciertos = 0
        total = len(examen)
        
        for i, p in enumerate(examen):
            # Etiqueta visual
            color = "orange" if p['tema'] == "PRL" else "green"
            st.markdown(f"**:{color}[{p['tema']}] Pregunta {i+1}:** {p['pregunta']}")
            
            # Selección
            key_name = f"resp_{st.session_state.num_test}_{i}"
            seleccion = st.radio(
                "Opciones:", 
                p['opciones'], 
                key=key_name, 
                index=None,
                disabled=st.session_state.corregido,
                label_visibility="collapsed"
            )
            
            # Corrección
            if st.session_state.corregido:
                if seleccion == p['correcta']:
                    st.markdown(f"<div class='correct'>✅ ¡Correcto!</div>", unsafe_allow_html=True)
                    aciertos += 1
                else:
                    st.markdown(f"<div class='incorrect'>❌ Tu respuesta: {seleccion if seleccion else 'En blanco'}<br>👉 <b>Correcta:</b> {p['correcta']}</div>", unsafe_allow_html=True)
            
            st.write("---")
        
        # Botón enviar
        texto_boton = "✅ CORREGIR EXAMEN" if not st.session_state.corregido else "RESULTADOS VISIBLES"
        enviado = st.form_submit_button(texto_boton, disabled=st.session_state.corregido)
        
        if enviado:
            st.session_state.corregido = True
            st.rerun()

    # Resultados
    if st.session_state.corregido:
        st.header(f"📊 NOTA FINAL: {aciertos} / {total}")
        nota_numerica = (aciertos / total) * 10
        
        if aciertos >= 12:
            st.success(f"🎉 APROBADO (Nota: {nota_numerica:.2f})")
            st.balloons()
        else:
            st.error(f"⚠️ SUSPENSO (Nota: {nota_numerica:.2f}) - Se necesita 12/24")
            
        if st.button("🔄 INTENTAR OTRO EXAMEN (Diferente)"):
            st.session_state.examen_actual = crear_examen_nuevo()
            st.session_state.corregido = False
            st.session_state.num_test += 1
            st.rerun()
