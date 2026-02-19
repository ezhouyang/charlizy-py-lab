import streamlit as st

def main():
    print("Hello from charlizy-py-lab!")
    
    st.set_page_config(page_title="Charlizy-PyLab", page_icon="🧬", layout="wide")
    st.title("🧬 欢迎来到 Charlizy-PyLab")
    st.markdown("""
    这是一个融合了**硬核工程架构**与**跨学科认知模型**的 Python 互动实验室。

    ### 💡 核心理念
    我们不教死记硬背的语法。我们将通过：
    1. **第一性原理**：看透代码背后的内存与计算本质。
    2. **生物学演化**：理解复杂系统（如 O2O 业务流、大模型应用）是如何从简单脚本生长出来的。
    3. **极速工程**：依托 `uv` 体验毫秒级的环境管理。

    👈 **请从左侧菜单选择一个认知模块开始你的实验！**
    """)
    st.info("💡 提示：本实验室所有代码均可在网页中直接修改并运行。")


if __name__ == "__main__":
    main()
