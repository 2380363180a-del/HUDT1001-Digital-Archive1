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

st.title("Map of Shenzhen 1979 — 2020")

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



st.title("Shenzhen Development Milestones from 1980 to 2025")

# ==================== 读取 CSV ====================
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

# ==================== 排序（保留 .1 .2 用于正确顺序） ====================
df['Date'] = df['Date'].astype(str).str.strip()

# 用于排序的 key（支持 2023.1、2023.2）
df['sort_key'] = pd.to_numeric(df['Date'].str.split('.').str[0], errors='coerce') + \
                 pd.to_numeric(df['Date'].str.split('.').str[1], errors='coerce').fillna(0) / 10

# 用于显示的干净年份（去掉 .1 .2）
df['display_date'] = df['Date'].str.split('.').str[0]

df = df.sort_values(by='sort_key').reset_index(drop=True)

# ==================== 显示每个对象 ====================
for idx, row in df.iterrows():
    date_str = str(row['display_date']).strip()      # ← 只显示纯年份
    title = str(row.get('Title', '')).strip()
    description = str(row.get('Description', '')).strip()

    st.header(date_str)   # 只显示年份，例如 2023

    # 如果有 Title 且不是 NA，才显示图片
    if title and title.lower() not in ['na', 'nan', '']:
        folder = "Milestone Sources"
        found = False
        for ext in ['.jpg', '.JPG', '.png', '.PNG', '.pdf']:
            filename = os.path.join(folder, title + ext)
            if os.path.exists(filename):
                if ext.lower() == '.pdf':
                    st.write(f"📄 PDF Document: {title + ext}")
                    st.markdown(f"[📥 下载 PDF]({filename})")
                else:
                    st.image(filename, use_column_width=True)
                found = True
                break
        if not found:
            st.warning(f"⚠️ 未找到图片: {title}")

    st.markdown(description)
    st.divider()

# 可选：显示完整元数据表
with st.expander("📊 查看完整 Dublin Core 元数据表"):
    st.dataframe(df, use_container_width=True)

