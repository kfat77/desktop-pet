# 桌面宠物 - Desktop Pet 🐱

一个可爱的桌面宠物程序。按住鼠标**左右键同时**并向任意方向拖动，即可画出一个矩形框，随后会有一只小猫从框中探出脑袋，然后跳出来在桌面上活动！

## 演示效果

1. 按住鼠标左键 + 右键不放
2. 向任意方向拖动，画出一个矩形区域
3. 松开鼠标，小猫从矩形框中探头，然后跳出来
4. 小猫会在桌面上自由走动，偶尔眨眼、摇尾巴

## 环境要求

- Python 3.8+
- Windows / macOS / Linux

## 安装与运行

```bash
# 克隆仓库
git clone https://github.com/kfat77/desktop-pet.git
cd desktop-pet

# 安装依赖
pip install -r requirements.txt

# 运行
python -m desktop_pet
```

## 交互说明

| 操作 | 效果 |
|------|------|
| 左键 + 右键 拖动 | 画出矩形框，召唤小猫 |
| 点击小猫 | 小猫会做出反应（跳跃/叫） |
| 右键点击托盘图标 | 退出程序 |

## 项目结构

```
desktop-pet/
├── desktop_pet/
│   ├── __init__.py
│   ├── __main__.py          # 入口
│   ├── main.py              # 程序主逻辑
│   ├── tray_app.py          # 系统托盘
│   ├── mouse_listener.py    # 全局鼠标监听
│   ├── selection_overlay.py # 矩形选择覆盖层
│   ├── pet_window.py        # 宠物主窗口
│   └── cat_widget.py        # 小猫绘制与动画
├── requirements.txt
└── README.md
```

## 技术栈

- **PySide6**: 跨平台GUI框架，用于窗口、动画和绘制
- **pynput**: 全局鼠标/键盘事件监听
- **QPainter**: 2D矢量绘制（猫咪图形、矩形框）

## License

MIT License
