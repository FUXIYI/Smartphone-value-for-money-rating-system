# 📱 Smartphone Value-for-Money Rating System (手机性价比打分系统)

一个基于 Flask 的 Web 应用程序，通过多维度量化模型对手机硬件配置进行客观打分，并结合实时价格计算出「性价比分」，为购机决策提供直观的数据参考。评分仅可以帮助快速找出预算内性价比最高的手机并不可以精确知道手机使用情况具体选购还得上网查询使用情况进行斟酌购机，而且硬件并不可以代替具体使用软硬结合才是硬道理。

> **数据来源**：截止2026年8月，用ai和网上公开数据自行整理的手机硬件清单表，覆盖核心计算、显示、影像、能源等 8 大系统、100+ 硬件项。

## ✨ 功能特性

- **多维度硬件打分**：内置涵盖 8 大系统、100+ 硬件项的打分规则，每项独立计分，避免单一参数主导结果。
- **可视化结果展示**：总分与各系统分项得分一目了然，并详细列出每个硬件项的具体得分与规格。
- **自定义机型打分**：无需录入数据库，手动输入任意配置即可即时获得打分结果。
- **机型数据管理**：支持添加自定义机型。
- **打分规则透明**：独立的规则说明页，所有权重与计分逻辑完全公开，拒绝算法黑箱。
- **极简响应式设计**：纯 HTML/CSS/JS 实现，无前端框架依赖，轻量高效，兼容移动端与桌面端。

## 🛠️ 技术栈

| 分层 | 技术 |
|---|---|
| **后端** | Python 3, Flask |
| **前端** | HTML5, CSS3, 原生 JavaScript (无框架) |
| **数据存储** | JSON 文件 (`phones.json`) |
| **版本控制** | Git, GitHub |

## 🚀 快速开始

### 1. 环境要求

- Python 3.8 或更高版本
- pip (Python 包管理器)

### 2. 克隆项目

```bash
git clone https://github.com/FUXIYI/Smartphone-value-for-money-rating-system.git
cd Smartphone-value-for-money-rating-system
```

### 3. 安装依赖

💡 温馨提示：为了避免与电脑里其他 Python 项目冲突，推荐使用虚拟环境（venv）单独安装。
```bash
Windows 用户：

python -m venv venv           # 创建一个独立的虚拟环境文件夹
venv\Scripts\activate         # 激活虚拟环境（成功后命令行最前面会出现 (venv)）
pip install -r requirements.txt  # 安装本项目唯一需要的工具 Flask


macOS / Linux 用户：

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 4. 启动应用
```bash
在虚拟环境激活的状态下，运行主程序：

python app.py

启动成功后，打开浏览器访问 http://127.0.0.1:5000 即可体验。