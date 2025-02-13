import streamlit as st
import pandas as pd

st.title("📊 Excel 数据展示工具")

# 允许用户上传 Excel 文件
st.subheader("📤 上传 Excel 文件")
uploaded_file = st.file_uploader("请选择一个 Excel 或 CSV 文件", type=["xlsx", "csv"])

if uploaded_file:
    # 判断文件类型并读取
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file, engine="openpyxl")  # 读取 Excel 文件
    else:
        df = pd.read_csv(uploaded_file)  # 读取 CSV 文件

    st.success("✅ 文件已成功上传！")

    # 显示原始数据
    st.subheader("📄 文件内容预览")
    st.dataframe(df)  # 显示表格数据

    # 显示文件信息
    st.subheader("📌 文件基本信息")
    st.write(f"**文件名：** `{uploaded_file.name}`")
    st.write(f"**行数：** {df.shape[0]}")
    st.write(f"**列数：** {df.shape[1]}")

    # 选择要展示的列
    selected_columns = st.multiselect("请选择要显示的列", df.columns.tolist(), default=df.columns.tolist())

    if selected_columns:
        st.subheader("📊 选定列的数据")
        st.dataframe(df[selected_columns])
