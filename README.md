# 🧬 Charlizy-PyLab: 告别纸上谈兵的 Python x AI 全链路实战实验室

Beyond syntax: An ultra-fast playground to reshape your engineering cognition and build AI-driven Python applications.

[![Powered by uv](https://img.shields.io/badge/Powered%20by-uv-purple.svg)](https://github.com/astral-sh/uv)
[![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> **“从‘跑通 Demo’到‘产业级运用’，中间隔着一道巨大的工程鸿沟。我开源这个项目，就是为了帮你填平它。”**

欢迎来到 **Charlizy-PyLab**。这不是一本静态的电子书，而是一个由前沿包管理器 `uv` 和交互式框架 `Streamlit` 驱动的**完全可运行、所见即所得的工程验证平台**。

在这里，我们将一步步把 Python 核心基础、底层认知模型（第一性原理/沉没成本），以及真正的 AI 产业级应用（大模型接入、Agent 构建、数据分析 Copilot）融合在一起，在你的本地机器上跑起来。



## ✨ 核心特性

* ⚡️ **极速工程底座**：抛弃缓慢的 `pip`。底层全量接入用 Rust 编写的新锐工具 `uv`。毫秒级创建环境与解析依赖，把时间花在思考上，而不是等待上。
* 🧠 **认知模型驱动**：将“第一性原理”、“沉没成本”等高级思维模型写进代码逻辑中，重塑你的工程认知。
* 🧱 **开箱即用的交互沙盒**：基于 Streamlit 打造 Web 界面，左侧导航章节，右侧直接在浏览器中修改代码并运行。
* 🤖 **产业级 AI 实战**：告别单纯的 API 调用，实战演示状态管理、System Prompt 编排与流式输出等真实业务 Copilot 架构。

---

## 🛠️ 极速启动指南 (Quick Start)

只需要三步，将这个强大的实战实验室在你的电脑上跑起来。

### 前置准备：安装 uv
如果你还没有安装 `uv`，请打开终端执行以下命令（极速安装）：
* **macOS / Linux**: `curl -LsSf https://astral.sh/uv/install.sh | sh`
* **Windows**: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

### 第 1 步：克隆实验室代码
将本仓库克隆到你的本地计算机：
```bash
git clone [https://github.com/ezhouyang/charlizy-py-lab](https://github.com/ezhouyang/charlizy-py-lab)
cd charlizy-py-lab

```

### 第 2 步：毫秒级同步环境依赖

得益于 `uv` 的强大，你不需要手动创建虚拟环境。直接运行：

```bash
uv sync

```

*这会自动读取 `uv.lock` 文件，并在瞬间为你准备好包含 Streamlit、OpenAI 等所有库的 `.venv` 隔离环境。*

### 第 3 步：启动交互式 Web 引擎

激动人心的时刻到了，启动实验室：

```bash
uv run streamlit run main.py

```

浏览器会自动打开 `http://localhost:8501`。尽情探索你的本地 AI 实验室吧！

---


## 🤝 参与贡献与交流

我是 **Charlizy**，一名热衷于复杂业务架构重构与 AI 产品创新的研发工程师。我相信，优秀的代码不仅需要扎实的技术栈，更需要跨学科的认知模型与对商业价值的敏锐嗅觉。

让我们在实践中，一起进化！

