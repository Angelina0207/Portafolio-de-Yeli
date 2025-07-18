import streamlit as st

# -------------------- CONFIGURACIÓN GENERAL --------------------
st.set_page_config(page_title="Portafolio de Yeli", page_icon="🌿", layout="wide")

# -------------------- ESTILO PERSONALIZADO --------------------
st.markdown("""
<style>
    body {
        background-color: #ecf7f5;
    }
    .block-container {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #00897b;
    }
    hr {
        border: 1px solid #b2dfdb;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- PORTADA --------------------
st.title("🌿 Portafolio de Angelina Contreras (Yeli)")
st.markdown("### Comunicadora y publicista con alma creativa, social y artística 💭")

st.image("images/perfil.png", caption="👩‍🎤 Foto de perfil", width=200)

st.markdown("""
Soy **Angelina Alessandra Contreras Bravo**, aunque la mayoría me conoce como **Angie** o **Yeli**.  
Nací un **2 de julio** y desde pequeña he estado rodeada de historias, creatividad y ganas de comunicar desde el corazón.  
Estudio **Comunicación** y me especializo en crear contenido que conecte, emocione y proponga una mirada crítica del mundo.
""")

st.markdown("""
Trabajo en la **empresa familiar vendiendo kekes** (y con amor, claro 🍰), y además manejo la **imagen digital de una empresa en surgimiento**.  
Formo parte de **Empoderate.Pe**, una organización que impulsa el empoderamiento juvenil, el pensamiento crítico y la comunicación con enfoque social.

Me encanta **grabar**, **tocar la guitarra** y perderme investigando cosas que me hacen pensar distinto.  
También realizo **edición de videos musicales, videodocumentales, entrevistas y reels reflexivos**, adaptando el contenido visual y narrativo al gusto y necesidades del consumidor.  
Además, desarrollo **posts y piezas gráficas** pensadas para comunicar de forma clara, atractiva y personalizada.
""")

st.markdown("---")

# -------------------- CONTACTO --------------------
st.header("📬 Contacto")
st.markdown("""
- 📸 [Instagram](https://www.instagram.com/wwkangie)
- ✉️ Correo: a20231270@pucp.edu.pe
- 🎓 Código PUCP: 20231270
""")

st.markdown("---")

# -------------------- PROYECTOS --------------------
st.header("✨ Proyectos personales")

st.subheader("💃 Danzas tradicionales")
st.markdown("He participado en concursos culturales representando danzas tradicionales.")
st.image("images/danza.png", caption="🩰 Presentación artística", width=600)

st.subheader("🎥 Videos con conciencia social")
st.markdown("He creado videos que abordan temas sensibles como género, salud mental y desigualdad, desde una mirada sensible.")
st.image("images/video.png", caption="🎬 Captura de un video social", width=600)

st.markdown("---")

# -------------------- GALERÍA PERSONAL --------------------
st.header("📸 Mi universo visual")

st.markdown("""
A continuación comparto algunos momentos y procesos que reflejan mi camino como comunicadora: desde escenas detrás de cámaras, fragmentos de presentaciones, hasta pequeños detalles que me inspiran día a día 💚
""")

col1, col2 = st.columns(2)

with col1:
    st.image("images/foto_extra_1.png", caption="🎬 En proceso de edición")
    st.image("images/foto_extra_3.png", caption="🌈 Creación visual desde casa")

with col2:
    st.image("images/foto_extra_2.png", caption="🩰 Ensayo previo a concurso de danza")
    st.image("images/foto_extra_4.png", caption="🧠 Jornada de formación en Empoderate.Pe")

st.markdown("---")

# -------------------- BLOG --------------------
st.header("🖊️ Blog y publicaciones")
st.components.v1.html("""<div style="overflow-y: scroll; height:500px; background-color:white;">
  <div id="retainable-rss-embed" 
       data-rss="https://medium.com/feed/@yeli-blog"
       data-maxcols="3" 
       data-layout="grid"
       data-poststyle="inline" 
       data-readmore="Leer más" 
       data-buttonclass="btn btn-primary" 
       data-offset="0">
  </div>
</div>
<script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>
""", height=550)

st.markdown("---")

# -------------------- BIO --------------------
st.header("📚 Mi biografía profesional")
with st.expander("📖 Haz clic aquí para leerla completa"):
    st.markdown("""
**🌼 Sobre mí:**  
Soy Yeli, comunicadora en formación con una mirada crítica, creativa y empática. Estudio en la PUCP, participo en el voluntariado Empodérate.Pe y disfruto combinar mis estudios con proyectos sociales, culturales y digitales. Me interesa especialmente trabajar desde la intersección entre narrativa, identidad, emociones y análisis social. Además, tengo experiencia gestionando contenidos para redes, realizando proyectos de comunicación con enfoque de género, y promoviendo la participación joven.

**💼 Experiencia laboral:**  
- Asistente de proyectos comunitarios – PUCP (2023)  
- Creación de contenido en redes y proyectos sociales independientes (2022–actualidad)  
- Voluntaria en Empodérate.Pe (2022–2024)

**🎯 Objetivo profesional:**  
Quiero usar la comunicación como herramienta de transformación social, apostando por formatos que inviten a cuestionar y construir colectivamente. Me interesa desarrollar proyectos colaborativos donde confluyan lo visual, lo narrativo y lo humano.

**🛠️ Habilidades:**  
- Redacción creativa  
- Producción audiovisual  
- Edición de videos musicales, entrevistas, reels y documentales  
- Análisis de género y estrategia en redes sociales  
- Investigación social y storytelling  
- Diseño de posts adaptados a públicos específicos

**📚 Formación complementaria:**  
- Taller de Narrativas Visuales – PUCP (2023)  
- Curso de Comunicación y Género – UCA El Salvador (2024)

**🏅 Logros y reconocimientos:**  
- Finalista en concursos de danza tradicional representando a mi comunidad.  
- Realización de videos sobre salud mental y roles de género, presentados en muestras estudiantiles.  
- Participación activa en iniciativas de formación y voluntariado.

**🌟 Fortalezas:**  
Soy organizada, comprometida y multitasking. Me gusta escuchar, aportar ideas y adaptarme a diferentes dinámicas de grupo. Tengo sensibilidad por los detalles y siempre busco que los proyectos tengan impacto y coherencia.

**🌀 Áreas de mejora:**  
A veces dedico mucho tiempo a revisar mis ideas para que reflejen bien lo que quiero decir. Pero esta búsqueda constante me permite entregar propuestas sólidas y bien pensadas.

**🎨 Intereses y hobbies:**  
Me encanta bailar, editar videos, ver películas sociales, escribir en mi diario, aprender cosas nuevas y pasar tiempo con mi gente. También disfruto mucho observar lo cotidiano y transformarlo en historias.

**📬 Disponibilidad:**  
Estoy abierta a colaborar, aprender y participar en proyectos creativos, sociales o de investigación.

**📌 Referencias:**  
Disponibles si se solicitan.
""")

st.markdown("---")

# -------------------- CIERRE --------------------
st.markdown("""
🌱 Gracias por visitar mi portafolio.  
Estoy creciendo, explorando y aprendiendo constantemente 💚  
""")
 
