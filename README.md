# SVG to AutoCAD SCR Converter (SVG 转 CAD 自动画图脚本工具)

这是一个轻量级的 Python 脚本，用于将 SVG 格式的矢量线条图转换成 AutoCAD 的脚本文件（`.scr`）。

导入 AutoCAD 运行后，可以实现像手绘一样逐笔自动画图的效果，常用于抖音、快手等平台上的“CAD 自动画图”创意视频制作。

---

## 📌 项目特点

- **零外部依赖**：仅使用 Python 标准库（`xml.etree` 和 `re`），无需安装任何第三方库。
- **自动坐标修正**：SVG 的 Y 轴方向朝下，而 CAD 的 Y 轴朝上，脚本已自动处理了 Y 坐标的反转，确保图像在 CAD 中方向正确。
- **支持相对与绝对坐标**：支持基础的 SVG 路径命令，包括 `M`/`m`（移动）、`L`/`l`（画线）、`H`/`h`（水平线）、`V`/`v`（垂直线）以及 `Z`/`z`（闭合）。
- **支持自定义缩放**：可通过 `scale` 参数自由调整输出图形在 CAD 中的尺寸。

---

## 🛠 运行环境

- **Python 3.x**
- **AutoCAD** (任何支持 `.scr` 脚本的版本)

---

## 🚀 快速上手

### 1. 准备 SVG 文件
首先，您需要准备一张**黑白线稿格式**的 SVG 矢量图。
> 💡 **提示**：如果只有 JPG/PNG 图片，推荐先使用在线免费工具（如 [Vectorizer.ai](https://vectorizer.ai/) 或 [Convertio](https://convertio.co/zh/)）将图片转换为 **SVG** 格式。

### 2. 下载并配置文件
将您的 SVG 文件命名为 `boy.svg`，并与本项目的 Python 脚本放在同一个文件夹下。

### 3. 生成 CAD 脚本
打开终端或命令行，运行以下命令：

```bash
python convert.py
💻 在 AutoCAD 中运行
打开 AutoCAD，新建一个空白图纸（或打开已有图纸）。
在 CAD 下方的命令行输入：
code
Text
SCRIPT
或者直接输入简写命令：
code
Text
SCR
按回车键，在弹出的文件选择框中，选择刚刚生成的 boy_rose.scr 文件。
AutoCAD 会自动开始运行脚本并绘制图形。
⚙️ 自定义参数调整
如果想要调整生成的图纸大小，可以修改 convert.py 文件底部的调用参数：
code
Python
# 调整 scale 参数：若生成的图纸偏小，可将 1.0 改为 2.0 或更大；若偏大则改小
svg_to_cad_scr("boy.svg", "boy_rose.scr", scale=1.0)
⚠️ 局限性说明
本脚本专为结构相对简单的黑白线稿设计：
当前版本主要解析最基础的直线和折线路径（M, L, H, V, Z）。对于部分包含复杂贝塞尔曲线（C, S, Q, T）或圆弧（A）的 SVG，转换后可能会以端点直线连接进行近似替代。若对曲线精度要求极高，建议先在第三方矢量软件中将曲线“离散化”/“扁平化”为折线再进行转换。
📄 开源协议
本项目基于 MIT License 协议开源。
code
Code
