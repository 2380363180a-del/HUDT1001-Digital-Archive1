import streamlit as st
import base64
from PIL import Image
import os 
import json
import streamlit.components.v1 as components
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

import streamlit as st
import os
import base64
import json
import streamlit.components.v1 as components

st.subheader("Time Slider")
st.title("🏙️ Shenzhen: 45 Years of Transformation")
st.markdown("""
Welcome to the Shenzhen Digital Archive. 
Use the slider below to journey through time and witness the incredible evolution of Shenzhen from 1979 to the present day.
""")
st.divider()

# 2. 准备数据
available_years = [1979] + list(range(1984, 2021))

# 3. 核心黑科技：图片 Base64 预加
@st.cache_data
def get_images_base64():
    """将所有存在的图片一次性读取并转为 Base64，避免滑动时读取硬盘"""
    img_dict = {}
    for year in available_years:
        path = f"images/{year}.jpg"
        if os.path.exists(path):
            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
                # 拼接成浏览器可以直接识别的图片数据格式
                img_dict[year] = f"data:image/jpeg;base64,{encoded}"
        else:
            img_dict[year] = None
    return img_dict

# 4. 生成给前端的数据
with st.spinner("⏳ 正在打包历史影像，初次加载请稍候..."):
    images_b64 = get_images_base64()
    
    # 将 Python 字典转换为 JavaScript 可以识别的 JSON 字符串
    js_images = json.dumps(images_b64)
    # 【修改点1】：统一把所有年份的说明写成 Shenzhen in the year xxxx
    js_captions = json.dumps({y: f"Shenzhen in the year {y}" for y in available_years})
    js_years = json.dumps(available_years)

# 5. 构建原生 HTML/JS 组件 (实现毫秒级切换)
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ font-family: sans-serif; text-align: center; color: #FAFAFA; background-color: transparent; margin: 0; padding: 0; }}
    
    /* 【修改点2】：将年份数字颜色改为白色，并增加了一点阴影提升质感 */
    #year-display {{ font-size: 2.5em; font-weight: 800; color: white; margin-bottom: 10px; text-shadow: 2px 2px 5px rgba(0,0,0,0.5); }}
    
    /* 自定义滑动条样式 */
    #slider {{ width: 100%; margin: 20px 0; cursor: pointer; accent-color: #ff4b4b; height: 6px; }}
    /* 图片容器 */
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
        // 接收来自 Python 的数据
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
            caption.innerText = captions[year]; // 直接调用统一格式的文本
            
            // 如果图片存在则显示，否则显示警告信息
            if (images[year]) {{
                img.src = images[year];
                img.style.display = 'block';
                noImgText.style.display = 'none';
            }} else {{
                img.style.display = 'none';
                noImgText.style.display = 'block';
            }}
        }}

        // 页面加载时初始化第一张图
        updateView(slider.value);

        // 监听滑块的实时拖动事件（核心：这是毫秒级响应的关键）
        slider.addEventListener('input', function() {{
            updateView(this.value);
        }});
    </script>
</body>
</html>
"""

# 6. 在 Streamlit 中渲染这个定制组件
components.html(html_code, height=750)

st.divider()

st.subheader("1980: The Establishment of Shenzhen Special Zone")
st.image("pages/Shenzhen1979.png")
st.write("On March 5, 1979, the State Council of the People's Republic of China issued Document No. [1979] 63, officially approving the establishment of Shenzhen (formerly Bao'an County), marking the legal starting point for Shenzhen's transformation from a border town to a modern city, and paving the way for it to be designated as China's first special economic zone in 1980.")

st.markdown("---")
