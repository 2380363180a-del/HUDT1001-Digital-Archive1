import streamlit as st
import base64
from PIL import Image
import os 
st.write("""# Shenzhen 1980-2025 Urban Development Digital Archive""")

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

st.subheader("Time Slider")
st.title("🏙️ Shenzhen: 45 Years of Transformation")
st.markdown("""
Welcome to the Shenzhen Digital Archive. 
Use the slider below to journey through time and witness the incredible evolution of Shenzhen from 1979 to the present day.
""")

st.divider()

# 3. Interactive Timeline Slider
# 1979 is widely considered the starting point of Shenzhen's rapid development
available_years = [1979] + list(range(1984, 2021))
selected_year = st.select_slider(
    "Select a Year:", 
    options=available_years, 
    value=1979
)

# 4. Data Dictionary for Captions (Optional but recommended)
# You can expand this dictionary as you gather more information for each specific year.
captions = {
    1979: "1979: Bao'an County is promoted to Shenzhen City.",
    1980: "1980: Shenzhen becomes China's first Special Economic Zone.",
    1990: "1990: The Shenzhen Stock Exchange is established.",
    1999: "1999: The first China High-Tech Fair is held in Shenzhen.",
    2010: "2010: The Special Economic Zone is expanded to cover the whole city.",
    2024: "2024: Shenzhen today — a global hub for technology, finance, and innovation."
}

# ----------------- 新增的缓存加速黑科技 -----------------
@st.cache_data
def load_image(path):
    """读取并缓存图片，避免每次滑动都去读取硬盘"""
    if os.path.exists(path):
        return Image.open(path)
    return None
# ---------------------------------------------------------

# 5. Image Display Logic
image_path = f"images/{selected_year}.jpg"

# 调用缓存函数来加载图片
img = load_image(image_path)

# Check if the image exists and display it
if img is not None:
    # Fetch the caption if it exists, otherwise use a default one
    caption_text = captions.get(selected_year, f"Shenzhen in the year {selected_year}.")
    
    st.image(img, caption=caption_text, use_column_width=True)
else:
    # Fallback message if the image for that year hasn't been added to the archive yet
    st.warning(f"📸 The image for **{selected_year}** is not yet available in the archive.")
    st.info(f"**To fix this:** Add an image named `{selected_year}.jpg` to the `images/` folder in your GitHub repository.")

st.divider()
#end of timeline slider

st.subheader("1980: The Establishment of Shenzhen Special Zone")
st.image("pages/Shenzhen1979.png")
st.write("On March 5, 1979, the State Council of the People's Republic of China issued Document No. [1979] 63, officially approving the establishment of Shenzhen (formerly Bao'an County), marking the legal starting point for Shenzhen's transformation from a border town to a modern city, and paving the way for it to be designated as China's first special economic zone in 1980.")

st.markdown("---")
