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
with st.spinner("loading..."):
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
             The image for this year is not yet available in the archive.
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

def display_object(year, title, description, image_path, Source, license_text, 
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
    
    with st.expander("About", expanded=False):
        st.markdown(f"**Source:** {Source}")
        st.markdown(f"**License:** {license_text}")
    
    # ============================================
display_object(
    year="1979",
    title="Shenzhen Municipality was Officially Established",
    description="The State Council of the People's Republic of China issued Document No. [1979] 63, officially establishing Shenzhen Municipality as a prefecture-level city.",
    image_path="Milestone Sources/1979_State_Council_Document.png",
    Source="Wikimedia Commons - State Council Document No. [1979] 63 (https://upload.wikimedia.org/wikipedia/commons/6/6f/%E5%9B%BD%E5%8F%91%E3%80%941979%E3%80%9563%E5%8F%B7.webp)",
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
    Source="Wikimedia Commons - Shenzhen in 1982 (https://en.wikipedia.org/wiki/File:Shenchen_in_1982.jpg)",
    license_text="Creative Commons Attribution-Share Alike 3.0 Unported",
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
    Source="Wikimedia Commons - Guomao Building (International Trade Centre) (https://zh.wikipedia.org/wiki/File:SZITB.JPG)",
    license_text="Creative Commons Attribution-Share Alike 2.5 Generic",
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
    Source="Wikimedia Commons - Shenzhen Stock Exchange (https://zh.wikipedia.org/wiki/File:Shenzhen_walk_02.JPG)",
    license_text="Creative Commons Attribution-Share Alike 3.0 Unported",
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
    title="Shenzhen Bao’an International Airport Opening",
    description="Shenzhen Airport Terminal A",
    image_path="Milestone Sources/1991_Shenzhen_Baoan_International_Airport_Opening.JPG",         
    Source="Wikimedia Commons - Shenzhen Bao'an International Airport Terminal A (https://zh.wikipedia.org/wiki/File:Shenzhen_Airport_Terminal_A.JPG)",
    license_text="Creative Commons Attribution-Share Alike 4.0 International",
    caption="1991·Shenzhen Bao’an International Airport Opening",
    extra_sections=[
        ("Historical Significance", """Shenzhen Bao’an International Airport opened in 1991. 
         This new aviation hub greatly improved the city’s global connectivity and supported its 
         rapid economic integration with Hong Kong and the international market.""")
    ]
)
# ============================================
display_object(
    year="1996",
    title="Shun Hing Square Complete",
    description="Shun Hing Square, Shenzhen, China, 2001",
    image_path="Milestone Sources/1996_Shun_Hing_Square_Complete.jpg",         
    Source="Wikimedia Commons - Shun Hing Square (https://commons.wikimedia.org/wiki/File:Shun_Hing_Square.jpg)",
    license_text="Creative Commons Attribution-ShareAlike 3.0 Unported and GNU Free Documentation License",
    caption="1996·Shun Hing Square Complete",
    extra_sections=[
        ("Historical Significance", """Shun Hing Square (Di Wang Tower) was completed in 1996 at 384 meters. 
         It became China’s tallest building at the time and symbolized Shenzhen’s economic rise while defining the Luohu Central Business District.""")
    ]
)
# ============================================
display_object(
    year="1997",
    title="China-SAR-HongKong border",
    description="Shenzhen & S.A.R. Hong Kong border - view from Shenzhen, Luo Hu District - July 2005",
    image_path="Milestone Sources/1997_ ChinaSARHongKong_border.png",          
    Source="Wikimedia Commons - Shenzhen-Hong Kong border view from Luohu (https://zh.wikipedia.org/wiki/File:China-SAR-HongKong_border_view-from-Shenzhen1.jpg)",
    license_text="Creative Commons CC0 1.0 Universal Public Domain Dedication",
    caption="1997·China-SAR-HongKong border",
    extra_sections=[
        ("Historical Significance", """On 1 July 1997, Hong Kong was handed over to China under “One Country, Two Systems.” 
         The smooth transition greatly boosted international confidence in Shenzhen, strengthening its role as the
          mainland's gateway to global capital and investment.""")
   ]
)
# ============================================
display_object(
    year="1999",
    title="First China Hi-Tech Fair (CHTF)",
    description="Shenzhen Convention and Exhibition Center seen from the Free Sky observation deck at Ping An Finance Centre in Shenzhen, China.",
    image_path="Milestone Sources/1999_First_China_HiTech_Fair.jpg",             
    Source="Wikimedia Commons - Cloud View Light Layer 2019 (https://en.wikipedia.org/wiki/File:%E4%BA%91%E9%99%85%E8%A7%82%E5%85%89%E5%B1%82_2019_-_07.jpg)",
    license_text="Creative Commons CC0 1.0 Universal Public Domain Dedication.",
    caption="1999·First China Hi-Tech Fair (CHTF)",
    extra_sections=[
        ("Historical Significance", """The first China Hi-Tech Fair was held in Shenzhen in 1999. 
         It established the city as a national platform for technology exchange and innovation, 
         attracting capital and startups while building Shenzhen’s reputation as a tech hub.""")
    ]
)
# ============================================
display_object(
    year="2000",
    title="Shenzhen University Town Founding",
    description="University Town Shenzhen main entrance.",
    image_path="Milestone Sources/2000_Shenzhen_University_Town_Founding.jpg",         
    Source="Wikimedia Commons - Shenzhen University Town main entrance (https://en.wikipedia.org/wiki/File:Umversitytownszmainentrance.jpg)",
    license_text="Creative Commons Attribution-Share Alike 3.0 Unported",
    caption="2000·Shenzhen University Town Founding",
    extra_sections=[
        ("Historical Significance", """Shenzhen University Town was founded in 2000. 
         It attracted top universities and research institutes, creating a strong local higher-education and R&D base 
         that supported the city’s transition into a knowledge economy.""")
    ]
)
# ============================================
display_object(
    year="2004",
    title="Shenzhen Metro Line 1 Opening",
    description="Train 126 of Shenzhen Metro Line 1",
    image_path="Milestone Sources/2004_Shenzhen_Metro_Line_1_Opening.jpeg",         
    Source="Wikimedia Commons - Shenzhen Metro Line 1 (https://commons.wikimedia.org/wiki/File:ShenzhenMetro-L1-126.jpeg)",
    license_text="Creative Commons Attribution-Share Alike 4.0 International (CC BY-SA 4.0) / GNU Free Documentation License, version 1.2 or later.",
    caption="2004·Shenzhen Metro Line 1 Opening",
    extra_sections=[
        ("Historical Significance", """Shenzhen Metro Line 1 opened in 2004. This marked the beginning of the city’s modern rail 
         transit era and formed the backbone of its urban transportation network.""")
    ]
)
# ============================================
display_object(
    year="2006",
    title="DJI",
    description="DJI Innovations logo. Extracted from a DJI Quick Start Guide.",
    image_path="Milestone Sources/2006_DJI.png",         
    Source="Wikimedia Commons - DJI Innovations logo (https://en.wikipedia.org/wiki/File:DJI_Innovations_logo.svg)",
    license_text="Public Domain",
    caption="2006·DJI Innovations logo",
    extra_sections=[
        ("Historical Significance", """DJI (Da-Jiang Innovations) was founded in a small apartment in Shenzhen in 2006. 
         The company grew into the global leader in drones, establishing Shenzhen’s worldwide reputation for hardware innovation and entrepreneurship.""")
    ]
)
# ============================================
display_object(
    year="2010",
    title="SEZ Expansion to Entire City",
    description="Subdivision of Shenzhen (French version). A map showing the administrative districts of Shenzhen as of the end of 2009, with labels in French.",
    image_path="Milestone Sources/2010_SEZ_Expansion_to_Entire_City.png",            
    Source="Wikimedia Commons - Shenzhen administrative divisions (2009) (https://commons.wikimedia.org/wiki/File:Shenzhen_administrative_divisions_(end_2009,_fr).svg)",
    license_text="Creative Commons Attribution-Share Alike 2.5 Generic (CC BY-SA 2.5).",
    caption="2010·SEZ Expansion to Entire City",
    extra_sections=[
        ("Translation", """**Sub-provincial city of Shenzhen (Guangdong Province)**
         - Light pink: urban district outside the SEZ 
         - Dark pink: urban district of the SEZ
         **Note:** The districts of Guangming and Pingshan were established by local authorities and do not have official existence at the national level."""),

        ("Historical Significance", """In 2010, the Special Economic Zone was expanded to cover the entire city (from 395 km² to 1,953 km²). 
         This major policy change enabled unified urban planning and city-wide integrated development.""")
    ]
)
# ============================================
display_object(
    year="2011",
    title="Kingkey 100 Completion",
    description="A photograph of the Kingkey 100 Tower in Shenzhen, China.",
    image_path="Milestone Sources/2011_Kingkey_100_Completion.jpg",         
    Source="Wikimedia Commons - Kingkey 100 (https://en.wikipedia.org/wiki/File:Kingkey-100-5.jpg)",
    license_text="Creative Commons CC0 1.0 Universal Public Domain Dedication.",
    caption="2011·Kingkey 100 Completion",
    extra_sections=[
        ("Historical Significance", """Kingkey 100 (441.8 m) was completed in 2011. 
         It became a landmark of Futian CBD and demonstrated Shenzhen's growing financial and economic strength.""")
    ]
)
# ============================================
display_object(
    year="2014",
    title="Ping An Finance Center Topping Out",
    description="Centre commercial area of Futian district",
    image_path="Milestone Sources/2014_Ping_An_Finance_Center_Topping_Out.jpg",         
    Source="Wikimedia Commons - Futian commercial area 2020 (https://commons.wikimedia.org/wiki/File:Commercial_area_of_futian_to_east2020_(4to3).jpg)",
    license_text="Creative Commons Attribution-Share Alike 4.0 International (CC BY-SA 4.0).",
    caption="2014·Ping An Finance Center Topping Out",
    extra_sections=[
        ("Historical Significance", """Ping An Finance Center (599.1 m) was topped out in 2014. 
         It became Shenzhen's new skyline icon and significantly enhanced the city's global image as a modern metropolis.""")
    ]
)
# ============================================
display_object(
    year="2016",
    title="Shenzhen-Hong Kong Stock Connect Open",
    description="An interior view photograph of the Shenzhen Stock Exchange.",
    image_path="Milestone Sources/2016_ShenzhenHongKong_Stock_Connect_Open.png",         
    Source="Wikimedia Commons - Shenzhen Stock Exchange (https://commons.wikimedia.org/wiki/File:Shenzhen_Stock_Exchange.jpg)",
    license_text="Creative Commons Attribution-Share Alike 3.0 Unported",
    caption="2016·Shenzhen-Hong Kong Stock Connect Open",
    extra_sections=[
        ("Historical Significance", """Shenzhen-Hong Kong Stock Connect was launched in 2016. 
         It deepened financial integration between Shenzhen and Hong Kong, further strengthening the city’s position as a regional financial hub.""")
    ]
)
# ============================================
display_object(
    year="2018",
    title="Hong Kong-Zhuhai-Macao Bridge",
    description="Taken from a TurboJET after leaving Macau.",
    image_path="Milestone Sources/2018_HongKongZhuhaiMacao_Bridge.jpeg",         
    Source="Wikimedia Commons - Hong Kong-Zhuhai-Macao Bridge (west section) (https://commons.wikimedia.org/wiki/File:West_section_of_Hong_Kong-Zhuhai-Macau_Bridge_(20180902174105).jpg)",
    license_text="Creative Commons Attribution-Share Alike 4.0",
    caption="2018·Hong Kong-Zhuhai-Macao Bridge",
    extra_sections=[
        ("Historical Significance", """The Hong Kong-Zhuhai-Macao Bridge was opened in 2018. 
         While bypassing the city directly, it accelerated the broader economic integration of the Greater Bay Area, driving Shenzhen to expedite the Shenzhen-Zhongshan Source and further solidifying its competitive edge as a core regional transport and innovation hub.""")
    ]
)
# ============================================
display_object(
    year="2020",
    title="Shenzhen Achieved Nationwide Full 5G Standalone Coverage First",
    description="Shenzhen achieved nationwide full 5G standalone coverage first in 2020",
    image_path="Milestone Sources/2020_Full_5G_Standalone_Coverage.jpg",         
    Source="Wikimedia Commons - 5G base stations of China Mobile and China Unicom (https://commons.wikimedia.org/wiki/File:5G_Base_Stations_of_China_Mobile_and_China_Unicom_in_Expo_2019_(20191005182324).jpg)",
    license_text="Creative Commons Attribution-Share Alike 4.0 International",
    caption="2020·Full 5G Standalone Coverage",
    extra_sections=[
        ("Historical Significance", """Shenzhen achieved nationwide full 5G standalone coverage first in 2020. This milestone established the city as a leader in digital infrastructure and laid the foundation for its smart-city development.""")
    ]
)
# ============================================
display_object(
    year="2023",
    title="Intelligent Connected Vehicles Regulation",
    description="Regulations of Shenzhen Special Economic Zone on the Administration of Intelligent Connected Vehicles",
    image_path="Milestone Sources/2023_Intelligent_Connected_Vehicles_Regulation.png",         
    Source="Official Website of Shenzhen Municipal Government (https://sf.sz.gov.cn/fggzywyb/content/mpost_11216374.html)",
    license_text="Public information provided by the Shenzhen Municipal Government; Subject to Chinese government information disclosure and copyright laws",
    caption="2023·Intelligent Connected Vehicles Regulation",
    extra_sections=[
        ("Historical Significance", """Shenzhen issued China’s first local regulation on Intelligent Connected Vehicles in 2023.
         It pioneered autonomous driving legislation and positioned the city as a global leader in future mobility industries.""")
    ]
)
# ============================================
display_object(
    year="2024",
    title="Shenzhen-Zhongshan Link Opening",
    description="Shenzhen-Zhongshan Link in June 2025",
    image_path="Milestone Sources/2024_ShenzhenZhongshan_Link_Opening.jpg",         
    Source="Wikimedia Commons - Shenzhen-Zhongshan Link (https://en.wikipedia.org/wiki/File:Shenzhen-Zhongshan_Link_2025.06.jpg)",
    license_text="Creative Commons Attribution-Share Alike 4.0 International",
    caption="2024·Shenzhen-Zhongshan Link Opening",
    extra_sections=[
        ("Historical Significance", """The Shenzhen-Zhongshan Link opened in June 2024. 
         This 24 km mega-bridge strengthened connectivity with western Guangdong and accelerated integration within the Greater Bay Area.""")
    ]
)
# ============================================
display_object(
    year="2025",
    title="Qianhai Huafa Ice & Snow World Opening",
    description="The design of Shenzhen Qianhai Huafa Snow World by 10 Design",
    image_path="Milestone Sources/2025_Qianhai_Huafa_Ice_Snow_World_Opening.jpg",         
    Source="Wikimedia Commons - Shenzhen Bao'an District buildings 2024 (https://commons.wikimedia.org/wiki/File:GD_%E5%BB%A3%E6%9D%B1_Guangdong_%E8%B7%A8%E5%B8%82%E5%A4%A7%E5%B7%B4_intercity_bus_tour_view_%E6%B7%B1%E5%9C%B3_Shenzhen_%E5%AF%B6%E5%AE%89%E5%8D%80_BaoAn_District_buildings_1123am_October_2024_R12S_436.jpg",
    license_text="Creative Commons CC0 1.0 Universal Public Domain Dedication)",
    caption="2025·Qianhai Huafa Ice & Snow World Opening",
    extra_sections=[
        ("Historical Significance", """Qianhai Ice & Snow World (430,000 m²) opened in 2025. 
         It boosted cultural and tourism development while upgrading Shenzhen’s urban service functions and quality of life.""")
    ]
)

st.markdown("### Thank you for exploring.")

