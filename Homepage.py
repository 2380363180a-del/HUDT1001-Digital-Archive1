import streamlit as st
import base64
from PIL import Image
import os 
import json
import pandas as pd
import streamlit.components.v1 as components

st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: #fafafa; }
    .object-card { 
        background-color: #161b22; 
        padding: 20px; 
        border-radius: 12px; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    img { border-radius: 8px; }
    h3 { color: #58a6ff !important; }
</style>
""", unsafe_allow_html=True)

st.write("""# Shenzhen 1980-2025 Urban Development Digital Archive""")

st.subheader("Introduction")
st.write("This digital archive documents the **45-year transformation of Shenzhen** from a small border town to a global hub of innovation and urban development by listing the city's key development milestones in chronological order.")

st.markdown("---")

available_years = [1979] + list(range(1984, 2021))

def get_images_base64():
    img_dict = {}
    for year in available_years:
        path = f"images/{year}.jpg"
        if os.path.exists(path):
            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
                img_dict[year] = f"data:image/jpeg;base64,{encoded}"
        else:
            img_dict[year] = None
    return img_dict
with st.spinner("⏳ 正在打包历史影像，初次加载请稍候..."):
    images_b64 = get_images_base64()
    js_images = json.dumps(images_b64)
    js_captions = json.dumps({y: f"Shenzhen in the year {y}" for y in available_years})
    js_years = json.dumps(available_years)

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ font-family: sans-serif; text-align: center; color: #FAFAFA; background-color: transparent; margin: 0; padding: 0; }}
    #year-display {{ font-size: 2.5em; font-weight: 800; color: white; margin-bottom: 10px; text-shadow: 2px 2px 5px rgba(0,0,0,0.5); }}
    #slider {{ width: 100%; margin: 20px 0; cursor: pointer; accent-color: #ff4b4b; height: 6px; }}
    #image-container {{ width: 100%; min-height: 400px; display: flex; align-items: center; justify-content: center; background-color: #1E1E1E; border-radius: 8px; overflow: hidden; }}
    #display-image {{ max-width: 100%; max-height: 600px; object-fit: contain; }}
    #caption-display {{ font-size: 1.1em; color: #ccc; margin-top: 15px; padding: 0 10px; }}
    .warning {{ color: #ff4b4b; font-weight: bold; }}
</style>
</head>
<body>
    <div id="year-display">1979</div>
    
    <input type="range" id="slider" min="0" max="{len(available_years)-1}" value="0" step="1">
    
    <div id="image-container">
        <img id="display-image" src="" alt="Shenzhen Archive">
        <div id="no-img-text" class="warning" style="display:none;">
            📸 The image for this year is not yet available in the archive.
        </div>
    </div>
    
    <div id="caption-display">Loading...</div>

    <script>
        const images = {js_images};
        const captions = {js_captions};
        const years = {js_years};
        
        const slider = document.getElementById('slider');
        const img = document.getElementById('display-image');
        const noImgText = document.getElementById('no-img-text');
        const caption = document.getElementById('caption-display');
        const yearDisplay = document.getElementById('year-display');

        // 更新视图的核心函数
        function updateView(index) {{
            const year = years[index];
            yearDisplay.innerText = year;
            caption.innerText = captions[year]; 
            if (images[year]) {{
                img.src = images[year];
                img.style.display = 'block';
                noImgText.style.display = 'none';
            }} else {{
                img.style.display = 'none';
                noImgText.style.display = 'block';
            }}
        }}
        updateView(slider.value);
        slider.addEventListener('input', function() {{
            updateView(this.value);
        }});
    </script>
</body>
</html>
"""
components.html(html_code, height=750)

st.markdown("---")

st.title("Shenzhen 1980-2025 Development Milestones")

st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: #fafafa; }
    img { border-radius: 12px; }
    h3 { color: #58a6ff !important; margin-bottom: 4px; }
    .light-text {
        color: #aaaaaa !important;
        opacity: 0.75;
        font-size: 0.95em;
        margin-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

def display_object(year, title, description, image_path, source, license_text, 
                   caption="", extra_sections=None):
    st.markdown(f"### {year}")
    st.markdown(f"#### {title}")
    
    st.image(image_path, use_container_width=True, caption=caption)
    
    st.markdown("**Description:**")
    st.write(description)
    
    if extra_sections:
        for section_title, section_text in extra_sections:
            st.markdown(f"**{section_title}:**")
            st.markdown(section_text)
    

    st.markdown("---")
    st.markdown(f'<p class="light-text"><strong>Source:</strong> {source}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="light-text"><strong>License:</strong> {license_text}</p>', unsafe_allow_html=True)
    
    st.markdown("---")   
    # ============================================
display_object(
    year="1979",
    title="Shenzhen Municipality was Officially Established",
    description="The State Council of the People's Republic of China issued Document No. [1979] 63, officially establishing Shenzhen Municipality as a prefecture-level city.",
    image_path="Milestone Sources/1979_State_Council_Document.png",
    source="Wikimedia Commons - State Council Document No. [1979] 63",
    license_text="Public Domain in mainland China according to Article 5 of the Copyright Law of the People's Republic of China. This official government document is not subject to copyright.",
    caption="1979·State Council Document",
    extra_sections=[
    ("Translation", """State Council Document. State Council [1979] No. 63. Reply of the State Council on Approving the Establishment of Shenzhen Municipality and Zhuhai Municipality in Guangdong Province
To the Revolutionary Committee of Guangdong Province: Your report dated January 13, 1979, has been received and is hereby approved as follows:
1.  Bao’an County shall be converted into Shenzhen Municipality, with the administrative area of Bao’an County serving as the administrative area of Shenzhen Municipality. The Municipal Revolutionary Committee shall be stationed in Shenzhen.
2.  Zhuhai County shall be converted into Zhuhai Municipality, with the administrative area of Zhuhai County serving as the administrative area of Zhuhai Municipality. The Municipal Revolutionary Committee shall be stationed in Xiangzhou.""")
]
)

# ============================================
display_object(
    year="1982",
    title="Shenzhen in 1982",
    description="A construction site in Shenzhen 1982",
    image_path="Milestone Sources/1982_Shenzhen_in_1982.jpg",         
    source="https://en.wikipedia.org/wiki/File:Shenchen_in_1982.jpg",
    license_text="CC BY-SA 3.0",
    caption="1982·Shenzhen",
    extra_sections=[
        ("Historical Significance", """In 1982, the slogan "Time is money, efficiency is life" was proposed in Shenzhen, 
        breaking the ideological barriers and became the spiritual symbol of China’s reform and opening-up era.""")
    ]
)
# ============================================
display_object(
    year="1985",
    title="Guomao Building Completed",
    description="The International Trade Building in Shenzhen, China",
    image_path="Milestone Sources/1985_Guomao_Building_2006.jpeg",         
    source="https://zh.wikipedia.org/wiki/File:SZITB.JPG",
    license_text="CC BY-SA 2.5",
    caption="2006·Guomao Building",
    extra_sections=[
        ("Historical Significance", """Construction of the Guomao Building began in 1982 and was completed in just 37 months by 1985. 
    Known as "Shenzhen Speed", it became China’s tallest building at the time and a national symbol of the 
    city’s rapid development in the early reform era.""")
    ]
)
# ============================================
display_object(
    year="1990",
    title="Shenzhen Stock Exchange Launch",
    description="The Shenzhen stock market",
    image_path="Milestone Sources/1990_Shenzhen_Stock_Exchange_2005.png",
    source="https://zh.wikipedia.org/wiki/File:Shenzhen_walk_02.JPG",
    license_text="CC BY-SA 3.0",
    caption="2005·Shenzhen Stock Exchange",
    extra_sections=[
        ("Historical Significance", """The Shenzhen Stock Exchange was formally launched in 1990. 
        It established Shenzhen as a national financial center and created China’s second major capital market, 
        accelerating the city’s shift from manufacturing to modern finance. In the same year, Shenzhen became 
        an important export processing base, and its ports are developing rapidly.""")
    ]
)
# ============================================
display_object(
    year="1991",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/1991_Shenzhen_Baoan_International_Airport_Opening.JPG",         
    source="source link",
    license_text="license statement",
    caption="caption",
    extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="1996",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/1996_Shun_Hing_Square_Complete.jpg",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="1997",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/1997_ ChinaSARHongKong_border.png",         
    source="source link",
    license_text="license statement",
    caption="caption"
)
# ============================================
display_object(
    year="1999",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/1999_First_China_HiTech_Fair.jpg",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2000",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2000_Shenzhen_University_Town_Founding.jpg",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2004",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2004_Shenzhen_Metro_Line_1_Opening.jpeg",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2006",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2006_DJI.png",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2010",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2010_SEZ_Expansion_to_Entire_City.png",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Interpretation", """Interpretation"""),
        
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2011",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2011_Kingkey_100_Completion.jpg",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2014",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2014_Ping_An_Finance_Center_Topping_Out.jpg",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2016",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2016_ShenzhenHongKong_Stock_Connect_Open.png",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2018",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2018_HongKongZhuhaiMacao_Bridge.jpeg",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2023",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2023_Intelligent_Connected_Vehicles_Regulation.png",         
    source="source link",
    license_text="license statement",
    caption="caption",
        extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2024",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2024_ShenzhenZhongshan_Link_Opening.jpg",         
    source="source link",
    license_text="license statement",
    caption="caption",
    extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
# ============================================
display_object(
    year="2025",
    title="title",
    description="description(must match Excel)...",
    image_path="Milestone Sources/2025_Qianhai_Huafa_Ice_Snow_World_Opening.jpg",         
    source="source link",
    license_text="license statement",
    caption="caption",
    extra_sections=[
        ("Historical Significance", """historical significance...""")
    ]
)
