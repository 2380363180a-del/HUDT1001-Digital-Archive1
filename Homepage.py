import streamlit as st
import base64

st.write("""# Shenzhen 1980-2025 Urban Development Digital Archive""")
# ==================== 全屏背景（base64 方法） ====================
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_page_bg(image_file):
    bin_str = get_base64_of_bin_file(image_file)
    page_bg_img = f'''
    <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center top;
            background-repeat: no-repeat;
            background-attachment: fixed;     /* ← 下滑时背景微微往下移动（视差效果） */
            height: 100vh;
        }}
        
        /* 轻量半透明遮罩，让文字清晰又不会变成黑条 */
        [data-testid="stAppViewContainer"] .block-container {{
            background-color: rgba(0, 0, 0, 0.35);
            border-radius: 16px;
            padding: 35px 40px;
            margin: 30px auto;
            max-width: 1100px;
        }}
        
        h1, h2, h3, p, li {{
            text-shadow: 0 2px 10px rgba(0,0,0,0.8);
        }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 调用函数（使用你的图片）
set_page_bg("Commercial_area_of_futian_to_east2020.jpg")
st.markdown("---")

st.subheader("Introduction")
st.write("This digital archive documents the **45-year transformation of Shenzhen** from a small border town to a global hub of innovation and urban development. Through historical photographs, official documents, urban maps, statistical charts, and cultural landmarks, it visualises the city’s rapid growth, industrial evolution, and spatial expansion.")
st.write("Structured chronologically, the archive combines a scrollable timeline with an interactive map slider to illustrate how Shenzhen evolved from a special economic zone into a model of modern urbanisation.")

st.markdown("---")

st.subheader("Key Contents")

st.markdown("""
This archive is structured around **six core dimensions** of Shenzhen’s transformation, using 22 chronologically selected Wikimedia Commons images, an interactive timeline slider, and full Dublin Core metadata.

- **Economic Transformation**  
  From fishing village (1980) to Special Economic Zone (SEZ) pioneer, then from manufacturing hub to global tech powerhouse (Huawei, Tencent, DJI).

- **Urban & Spatial Expansion**  
  Aerial and map views showing explosive land-use change: farmland → industrial zones → dense high-rise skyline and innovation districts.

- **Population & Migration**  
  Influx of millions of migrant workers; the human story behind the rapid urban growth from ~30,000 to over 17 million residents.

- **Technological Innovation**  
  Evolution into “China’s Silicon Valley” — from electronics assembly in the 1980s–90s to AI, drones, and green tech leadership by 2025.

- **Infrastructure & Planning**  
  Development of ports, highways, a metro system, and sustainable urban planning that turned a border town into a model modern metropolis.

- **Environmental & Social Reflection**  
  Early pollution challenges followed by greening efforts, eco-city initiatives, and critical questions about sustainable growth in a hyper-urban context.
""")

st.markdown("---")
