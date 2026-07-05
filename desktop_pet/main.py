"""
Main - 程序入口，整合所有组件。
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from .mouse_listener import MouseListener
from .selection_overlay import SelectionOverlay
from .pet_window import PetWindow
from .tray_app import TrayApp


class DesktopPetApp:
    """桌面宠物应用主类"""
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)
        
        # 创建组件
        self.overlay = SelectionOverlay()
        self.pet = PetWindow()
        self.tray = TrayApp()
        self.mouse = MouseListener()
        
        # 连接信号
        self._setup_signals()
        
        # 状态
        self._selecting = False
    
    def _setup_signals(self):
        """设置信号连接"""
        # 鼠标事件 -> 选择覆盖层
        self.mouse.both_pressed.connect(self._on_both_pressed)
        self.mouse.mouse_moved.connect(self._on_mouse_moved)
        self.mouse.any_released.connect(self._on_any_released)
        
        # 选择完成 -> 召唤小猫
        self.overlay.selection_finished.connect(self._on_selection_finished)
        self.overlay.selection_cancelled.connect(self._on_selection_cancelled)
        
        # 托盘退出
        self.tray.exit_requested.connect(self._on_exit)
    
    def _on_both_pressed(self, pos):
        """左右键同时按下 - 开始选择"""
        self._selecting = True
        self.overlay.start_selection(pos)
    
    def _on_mouse_moved(self, pos):
        """鼠标移动 - 更新选择"""
        if self._selecting:
            self.overlay.update_position(pos)
    
    def _on_any_released(self, pos):
        """任意键释放 - 结束选择"""
        if self._selecting:
            self._selecting = False
            self.overlay.finish_selection(pos)
    
    def _on_selection_finished(self, rect):
        """选择完成 - 召唤小猫"""
        self.pet.appear_from_rect(rect)
    
    def _on_selection_cancelled(self):
        """选择取消"""
        pass
    
    def _on_exit(self):
        """退出程序"""
        self.mouse.stop()
        self.app.quit()
    
    def run(self):
        """运行应用"""
        # 启动鼠标监听
        self.mouse.start()
        
        # 显示托盘
        self.tray.show()
        
        # 运行
        return self.app.exec()


def main():
    """程序入口"""
    app = DesktopPetApp()
    sys.exit(app.run())


if __name__ == "__main__":
    main()
