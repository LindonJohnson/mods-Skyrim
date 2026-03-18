import streamlit as st
import pandas as pd
df = pd.read_csv("mods.txt", sep=',')
df = df.drop(["#Mod_Status", "#Note", "#Download_File_Name", "#Mod_Priority"], axis = 1)

def Hlink():
 return {"#Mod_Nexus_URL": st.column_config.LinkColumn("Download",display_text="Abrir")}

st.markdown("""
<h1 style='text-align: center;
           font-size: 40px;
           margin-bottom: 30px;'>
⚔️ Mods Skyrim ⚔️
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# st.dataframe(df,column_config=Hlink())

def separadores(titulo, inicio, fim):
  with st.expander(titulo):
    st.dataframe(df.iloc[inicio:fim], column_config=Hlink())

separadores("📦 Skyrim", 0, 8)
separadores("🛠️ Tools", 8, 14)
separadores("🐛🌍 Bug Fixes - Expansões", 15, 122)
separadores("🎬 Animações", 124, 200)
separadores("🔊 Audio Fix", 202, 207)
separadores("🎨🧱 Texturas e Malhas", 209, 291)
separadores("✨ Community Shaders", 293, 304)
separadores("🧍 NPCs", 306, 316)
separadores("💪 Corpos e Texturas", 318, 331)
separadores("⚔️🛡️ Armas, Armaduras e Roupas", 333, 376)
separadores("🔥 OSTIM", 378, 404)
separadores("⚔️ Combate", 406, 470)
separadores("🖥️ UI Menu", 472, 500)
separadores("📤 Outputs", 502, 532)
separadores("🎙️ DUBLAGEM E TRADUÇÃO", 513, 534)
