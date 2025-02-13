import streamlit as st

st.title("Streamlit Cloud 图片展示")

# 显示本地图片
st.subheader("📷 本地图片")
st.image("image1.jpg", caption="本地图片示例", use_column_width=True)

# 显示在线图片
st.subheader("🌍 在线图片")
st.image("https://picsum.photos/800/400", caption="在线图片示例", use_column_width=True)

# 允许用户上传图片
st.subheader("📤 上传图片")
uploaded_file = st.file_uploader("请选择一张图片", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="用户上传的图片", use_column_width=True)
    st.success("✅ 图片已成功上传！")
