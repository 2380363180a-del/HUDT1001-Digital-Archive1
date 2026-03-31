import streamlit as st
import base64
from PIL import Image
import os 
import json
import pandas as pd
import streamlit.components.v1 as components
st.write("""# Shenzhen 1980-2025 Urban Development Digital Archive""")

st.subheader("Introduction")
st.write("This digital archive documents the **45-year transformation of Shenzhen** from a small border town to a global hub of innovation and urban development by listing the city's key development milestones in chronological order.")

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

st.title("Map of Shenzhen 1979 — 2020")
# 2. 准备数据
available_years = [1979] + list(range(1984, 2021))

# 3. 核心黑科技：图片 Base64 预加
def get_images_base64():
    """将所有存在的图片一次性读取并转为 Base64，避免滑动时读取硬盘"""
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

st.divider()

st.subheader("1980: The Establishment of Shenzhen Special Zone")
st.image("pages/Shenzhen1979.png")
st.write("On March 5, 1979, the State Council of the People's Republic of China issued Document No. [1979] 63, officially approving the establishment of Shenzhen (formerly Bao'an County), marking the legal starting point for Shenzhen's transformation from a border town to a modern city, and paving the way for it to be designated as China's first special economic zone in 1980.")

st.markdown("---")





st.set_page_config(page_title="Shenzhen 1980-2025 Digital Archive", layout="wide")

st.title("Shenzhen 1980-2025 Urban Development Digital Archive")
st.subheader("Interactive Chronological Archive")

# ==================== 读取 CSV（解决中文编码） ====================
csv_file = "Milestones.csv"

try:
    df = pd.read_csv(csv_file, encoding='utf-8-sig')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(csv_file, encoding='gbk')
        except UnicodeDecodeError:
            df = pd.read_csv(csv_file, encoding='gb18030')

# ==================== 关键改进：按 Date 从小到大排序 ====================
# 支持 1979、1982、2023.1、2023.2 等格式
df['Date'] = df['Date'].astype(str).str.strip()
df['sort_key'] = pd.to_numeric(df['Date'], errors='coerce')   # 把 2023.1 转为 2023.1，2023 转为 2023.0
df = df.sort_values(by='sort_key').reset_index(drop=True)

# ==================== 自动显示每个对象 ====================
for idx, row in df.iterrows():
    date_str = str(row['Date']).strip()
    title = str(row.get('Title', '')).strip()
    description = str(row.get('Description', '')).strip()

    # Date 作为 subheader
    st.subheader(date_str)

    # 如果 Title 不是 NA/空值，才尝试显示图片
    if title and title.lower() != "na" and title.lower() != "nan":
        folder = "Milestone Sources"
        found = False
        for ext in ['.jpg', '.JPG', '.png', '.PNG', '.pdf']:
            filename = os.path.join(folder, title + ext)
            if os.path.exists(filename):
                if ext.lower() == '.pdf':
                    st.write(f"📄 PDF Document: {title + ext}")
                    st.markdown(f"[📥 下载 PDF]({filename})")
                else:
                    st.image(filename, use_column_width=True)   # 横向铺满
                found = True
                break
        if not found:
            st.warning(f"⚠️ 未找到图片: {title}")

    # 显示描述
    st.markdown(description)
    st.divider()

# 可选：完整元数据表
with st.expander("📊 查看完整 Dublin Core 元数据表"):
    st.dataframe(df, use_container_width=True)

