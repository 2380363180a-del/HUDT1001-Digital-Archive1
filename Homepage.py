import streamlit as st

st.write("""# Shenzhen 1980-2025 Urban Development Digital Archive""")

st.markdown("---")

st.subheader("Introduction")
st.write("This digital archive documents the 45-year transformation of Shenzhen from a small border town to a global hub of innovation and urban development. Through historical photographs, official documents, urban maps, statistical charts, and cultural landmarks, it visualises the city’s rapid growth, industrial evolution, and spatial expansion.")
st.write("Structured chronologically, the archive combines a scrollable timeline with an interactive map slider to illustrate how Shenzhen evolved from a special economic zone into a model of modern urbanisation.")

st.markdown("---")

st.subheader("Key Contents")

st.markdown("---")

# 核心：点击展开/折叠
if st.button("Explore the Archive ↓", use_container_width=True):
    st.session_state.expand_archive = not st.session_state.get("expand_archive", False)

# 控制是否展开
if st.session_state.get("expand_archive", False):
    st.markdown("## Timeline & Archival Items")
    st.markdown("Your 1980s / 1990s / 2000s / 2010s / 2020s sections go here.")
    st.markdown("Your map slider, images, charts, metadata table…")

    st.markdown("---")
    st.caption("Course: Digital Archives | Group Members: [Your Names] | 2025")
