import sys
import colorsys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox,
    QTabWidget, QGroupBox, QSpinBox, QGridLayout, QFrame,
    QSlider, QDialog, QFormLayout
)
from PyQt6.QtGui import (
    QPalette, QColor, QLinearGradient, QBrush, QIcon, QFont, QPixmap,
    QPainter
)
from PyQt6.QtCore import Qt, pyqtSignal

class ColorConverter:
    @staticmethod
    def rgb_to_hex(r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}".upper()

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip('#')
        if len(hex_str) != 6:
            return 0, 0, 0
        try:
            return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
        except:
            return 0, 0, 0

    @staticmethod
    def rgb_to_hsv(r, g, b):
        r, g, b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
        h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        return round(h*360), round(s*100), round(v*100)

    @staticmethod
    def hsv_to_rgb(h, s, v):
        h = h % 360
        s = max(0, min(100, s)) / 100.0
        v = max(0, min(100, v)) / 100.0
        r, g, b = colorsys.hsv_to_rgb(h/360.0, s, v)
        return round(r*255), round(g*255), round(b*255)

    @staticmethod
    def rgb_to_hsl(r, g, b):
        r, g, b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
        h, l, s = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
        return round(h*360), round(s*100), round(l*100)

    @staticmethod
    def hsl_to_rgb(h, s, l):
        h = h % 360
        s = max(0, min(100, s)) / 100.0
        l = max(0, min(100, l)) / 100.0
        r, g, b = colorsys.hls_to_rgb(h/360.0, l, s)
        return round(r*255), round(g*255), round(b*255)

    @staticmethod
    def rgb_to_cmyk(r, g, b):
        r, g, b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
        r_norm, g_norm, b_norm = r/255.0, g/255.0, b/255.0
        k = 1 - max(r_norm, g_norm, b_norm)
        if k >= 1:
            return 0, 0, 0, 100
        c = (1 - r_norm - k) / (1 - k) * 100
        m = (1 - g_norm - k) / (1 - k) * 100
        y = (1 - b_norm - k) / (1 - k) * 100
        return round(c), round(m), round(y), round(k*100)

    @staticmethod
    def cmyk_to_rgb(c, m, y, k):
        c, m, y, k = max(0, min(100, c)), max(0, min(100, m)), max(0, min(100, y)), max(0, min(100, k))
        c_norm, m_norm, y_norm, k_norm = c/100.0, m/100.0, y/100.0, k/100.0
        r = 255 * (1 - c_norm) * (1 - k_norm)
        g = 255 * (1 - m_norm) * (1 - k_norm)
        b = 255 * (1 - y_norm) * (1 - k_norm)
        return round(r), round(g), round(b)

    @staticmethod
    def rgb_to_yuv(r, g, b):
        r, g, b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
        y = 0.299*r + 0.587*g + 0.114*b
        u = -0.147*r - 0.289*g + 0.436*b + 128
        v = 0.615*r - 0.515*g - 0.100*b + 128
        return round(y), round(u), round(v)

    @staticmethod
    def yuv_to_rgb(y, u, v):
        u -= 128
        v -= 128
        r = y + 1.140*v
        g = y - 0.395*u - 0.581*v
        b = y + 2.032*u
        return max(0, min(255, round(r))), max(0, min(255, round(g))), max(0, min(255, round(b)))

class ColorPickerWidget(QWidget):
    colorChanged = pyqtSignal(int, int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(340, 340)
        self.hue = 0
        self.sat = 100
        self.val = 100
        self.updating = False  # Flag to prevent recursion
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        self.canvas = QLabel()
        self.canvas.setFixedSize(316, 316)
        self.canvas.setStyleSheet("border: 4px solid #1a1a1a; border-radius: 20px; background: #f8f8f8;")
        layout.addWidget(self.canvas)
        self.update_canvas()

    def update_canvas(self):
        pixmap = QPixmap(316, 316)
        pixmap.fill(QColor(0, 0, 0, 0))
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        gradient = QLinearGradient(0, 0, 316, 0)
        gradient.setColorAt(0, QColor("white"))
        gradient.setColorAt(1, QColor.fromHsv(self.hue, 255, 255))
        painter.fillRect(0, 0, 316, 316, QBrush(gradient))

        gradient2 = QLinearGradient(0, 0, 0, 316)
        gradient2.setColorAt(0, QColor(0, 0, 0, 0))
        gradient2.setColorAt(1, QColor(0, 0, 0, 255))
        painter.fillRect(0, 0, 316, 316, QBrush(gradient2))

        x = int((self.sat / 100.0) * 316)
        y = int((1 - self.val / 100.0) * 316)
        pen = painter.pen()
        pen.setColor(QColor(255, 255, 255))
        pen.setWidth(4)
        painter.setPen(pen)
        painter.drawEllipse(x - 10, y - 10, 20, 20)
        pen.setColor(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawEllipse(x - 10, y - 10, 20, 20)

        painter.end()
        self.canvas.setPixmap(pixmap)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.pick_color(event.position().toPoint())

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.pick_color(event.position().toPoint())

    def pick_color(self, pos):
        if not (12 <= pos.x() <= 304 and 12 <= pos.y() <= 304):
            return
        x = (pos.x() - 12) / 292.0
        y = (pos.y() - 12) / 292.0
        s = max(0, min(100, x * 100))
        v = max(0, min(100, (1 - y) * 100))
        r, g, b = ColorConverter.hsv_to_rgb(self.hue, s, v)
        self.sat = s
        self.val = v
        self.update_canvas()
        if not self.updating:
            self.colorChanged.emit(r, g, b)

    def set_hsv(self, h, s, v):
        if self.updating:
            return
        self.updating = True
        self.hue = h % 360
        self.sat = max(0, min(100, s))
        self.val = max(0, min(100, v))
        self.update_canvas()
        r, g, b = ColorConverter.hsv_to_rgb(self.hue, self.sat, self.val)
        self.colorChanged.emit(r, g, b)
        self.updating = False

class LanguageManager:
    def __init__(self, app):
        self.app = app
        self.current_lang = "en"
        self.translations = {
            "en": {
                "title": "Advanced Color Converter Pro",
                "rgb": "RGB", "hex": "HEX", "hsv": "HSV", "hsl": "HSL", "cmyk": "CMYK", "yuv": "YUV",
                "language": "Language", "theme": "Theme",
                "light": "Light", "dark": "Dark", "system": "System", "red": "Red Theme", "blue": "Blue Theme",
                "red_val": "Red", "green": "Green", "blue": "Blue", "hue": "Hue", "sat": "Saturation",
                "val": "Value", "lightness": "Lightness", "cyan": "Cyan", "magenta": "Magenta",
                "yellow": "Yellow", "black": "Black", "luminance": "Luminance", "copy": "Copy",
                "input": "Input Values", "output": "Converted Outputs", "tools": "Color Tools",
                "picker": "Color Picker", "harmony": "Color Harmony", "complementary": "Complementary",
                "analogous": "Analogous", "triadic": "Triadic", "tetradic": "Tetradic"
            },
            "fa": {
                "title": "مبدل پیشرفته رنگ پرو",
                "rgb": "آرجی‌بی", "hex": "هگز", "hsv": "اچ‌اس‌وی", "hsl": "اچ‌اس‌ال", "cmyk": "سی‌ام‌وای‌کی", "yuv": "وای‌یو‌وی",
                "language": "زبان", "theme": "تم",
                "light": "روشن", "dark": "تیره", "system": "سیستم", "red": "تم قرمز", "blue": "تم آبی",
                "red_val": "قرمز", "green": "سبز", "blue": "آبی", "hue": "رنگ", "sat": "اشباع",
                "val": "روشنایی", "lightness": "روشنی", "cyan": "فیروزه‌ای", "magenta": "ارغوانی",
                "yellow": "زرد", "black": "سیاه", "luminance": "روشنایی", "copy": "کپی",
                "input": "مقادیر ورودی", "output": "خروجی‌های تبدیل شده", "tools": "ابزارهای رنگ",
                "picker": "انتخابگر رنگ", "harmony": "هارمونی رنگ", "complementary": "مکمل",
                "analogous": "مشابه", "triadic": "سه‌گانه", "tetradic": "چهارگانه"
            },
            "zh": {
                "title": "高级颜色转换器专业版",
                "rgb": "红绿蓝", "hex": "十六进制", "hsv": "色相饱和度明度", "hsl": "色相饱和度亮度", "cmyk": "青品黄黑", "yuv": "亮度色度",
                "language": "语言", "theme": "主题",
                "light": "明亮", "dark": "暗黑", "system": "系统", "red": "红色主题", "blue": "蓝色主题",
                "red_val": "红", "green": "绿", "blue": "蓝", "hue": "色相", "sat": "饱和度",
                "val": "明度", "lightness": "亮度", "cyan": "青", "magenta": "品红",
                "yellow": "黄", "black": "黑", "luminance": "亮度", "copy": "复制",
                "input": "输入值", "output": "转换输出", "tools": "颜色工具",
                "picker": "颜色选择器", "harmony": "颜色和谐", "complementary": "互补色",
                "analogous": "类似色", "triadic": "三色调", "tetradic": "四色调"
            },
            "ru": {
                "title": "Продвинутый конвертер цветов Про",
                "rgb": "Красный Зеленый Синий", "hex": "HEX", "hsv": "Оттенок Насыщенность Яркость", "hsl": "Оттенок Насыщенность Светлота", "cmyk": "Голубой Пурпурный Желтый Черный", "yuv": "Яркость Цветность",
                "language": "Язык", "theme": "Тема",
                "light": "Светлая", "dark": "Темная", "system": "Системная", "red": "Красная тема", "blue": "Синяя тема",
                "red_val": "Красный", "green": "Зеленый", "blue": "Синий", "hue": "Оттенок", "sat": "Насыщенность",
                "val": "Яркость", "lightness": "Светлота", "cyan": "Голубой", "magenta": "Пурпурный",
                "yellow": "Желтый", "black": "Черный", "luminance": "Яркость", "copy": "Копировать",
                "input": "Входные значения", "output": "Преобразованные выходы", "tools": "Инструменты цвета",
                "picker": "Пипетка цвета", "harmony": "Гармония цветов", "complementary": "Дополнительный",
                "analogous": "Аналогичный", "triadic": "Триадный", "tetradic": "Тетрадный"
            }
        }

    def tr(self, key):
        return self.translations.get(self.current_lang, self.translations["en"]).get(key, key)

    def set_language(self, lang):
        self.current_lang = lang
        self.app.retranslateUi()

class ThemeManager:
    @staticmethod
    def apply_theme(app, theme_name):
        palette = QPalette()
        if theme_name == "light":
            palette.setColor(QPalette.ColorRole.Window, QColor(248, 248, 252))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(20, 20, 35))
            palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
            palette.setColor(QPalette.ColorRole.Text, QColor(20, 20, 35))
            palette.setColor(QPalette.ColorRole.Button, QColor(235, 235, 245))
            palette.setColor(QPalette.ColorRole.ButtonText, QColor(20, 20, 35))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 122, 255))
            palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        elif theme_name == "dark":
            palette.setColor(QPalette.ColorRole.Window, QColor(25, 25, 35))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(240, 240, 245))
            palette.setColor(QPalette.ColorRole.Base, QColor(38, 38, 50))
            palette.setColor(QPalette.ColorRole.Text, QColor(240, 240, 245))
            palette.setColor(QPalette.ColorRole.Button, QColor(52, 52, 70))
            palette.setColor(QPalette.ColorRole.ButtonText, QColor(240, 240, 245))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(80, 140, 255))
            palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        elif theme_name == "red":
            palette.setColor(QPalette.ColorRole.Window, QColor(40, 15, 20))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 170, 170))
            palette.setColor(QPalette.ColorRole.Base, QColor(60, 25, 30))
            palette.setColor(QPalette.ColorRole.Text, QColor(255, 170, 170))
            palette.setColor(QPalette.ColorRole.Button, QColor(80, 35, 40))
            palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 190, 190))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(200, 50, 50))
        elif theme_name == "blue":
            palette.setColor(QPalette.ColorRole.Window, QColor(15, 25, 45))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(180, 210, 255))
            palette.setColor(QPalette.ColorRole.Base, QColor(25, 35, 65))
            palette.setColor(QPalette.ColorRole.Text, QColor(180, 210, 255))
            palette.setColor(QPalette.ColorRole.Button, QColor(35, 45, 85))
            palette.setColor(QPalette.ColorRole.ButtonText, QColor(200, 220, 255))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(70, 130, 220))
        else:
            palette = app.style().standardPalette()
        app.setPalette(palette)

class ColorInputWidget(QGroupBox):
    valueChanged = pyqtSignal(int, int, int)

    def __init__(self, title, lang_manager, parent=None):
        super().__init__(title, parent)
        self.lang_manager = lang_manager
        self.updating = False
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)
        layout.setSpacing(10)
        self.inputs = []
        labels = [self.lang_manager.tr("red_val"), self.lang_manager.tr("green"), self.lang_manager.tr("blue")]
        for i, label in enumerate(labels):
            lbl = QLabel(label + ":")
            lbl.setStyleSheet("color: #0055aa; font-weight: bold; font-size: 13px;")
            spin = QSpinBox()
            spin.setRange(0, 255)
            spin.setFixedHeight(42)
            spin.setStyleSheet("QSpinBox { padding: 10px; font-size: 15px; border-radius: 10px; }")
            spin.valueChanged.connect(self.on_value_changed)
            self.inputs.append(spin)
            layout.addWidget(lbl, 0, i * 2)
            layout.addWidget(spin, 0, i * 2 + 1)
        self.copy_btn = QPushButton(self.lang_manager.tr("copy"))
        self.copy_btn.setFixedHeight(42)
        self.copy_btn.setStyleSheet("QPushButton { font-weight: bold; }")
        self.copy_btn.clicked.connect(self.copy_values)
        layout.addWidget(self.copy_btn, 0, 6, 1, 2)

    def on_value_changed(self):
        if self.updating:
            return
        r = self.inputs[0].value()
        g = self.inputs[1].value()
        b = self.inputs[2].value()
        self.valueChanged.emit(r, g, b)

    def set_values(self, r, g, b):
        if self.updating:
            return
        self.updating = True
        r, g, b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
        self.inputs[0].blockSignals(True)
        self.inputs[1].blockSignals(True)
        self.inputs[2].blockSignals(True)
        self.inputs[0].setValue(r)
        self.inputs[1].setValue(g)
        self.inputs[2].setValue(b)
        self.inputs[0].blockSignals(False)
        self.inputs[1].blockSignals(False)
        self.inputs[2].blockSignals(False)
        self.updating = False

    def copy_values(self):
        text = f"RGB({self.inputs[0].value()}, {self.inputs[1].value()}, {self.inputs[2].value()})"
        QApplication.clipboard().setText(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lang_manager = LanguageManager(self)
        self.current_r, self.current_g, self.current_b = 255, 0, 0
        self.updating = False  # Global update flag
        self.setup_ui()
        self.apply_initial_theme()
        self.set_rtl_if_needed()
        self.update_all_outputs()
        self.update_preview()

    def setup_ui(self):
        self.setWindowTitle(self.lang_manager.tr("title"))
        self.setMinimumSize(1500, 950)
        self.setWindowIcon(QIcon.fromTheme("color-management"))
        self.setStyleSheet("QMainWindow { background: transparent; }")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(28)
        main_layout.setContentsMargins(28, 28, 28, 28)

        # Left Panel
        left_panel = QFrame()
        left_panel.setFrameShape(QFrame.Shape.StyledPanel)
        left_panel.setMinimumWidth(460)
        left_panel.setStyleSheet("QFrame { border-radius: 20px; background: rgba(255,255,255,0.8); }")
        left_layout = QVBoxLayout(left_panel)
        left_layout.setSpacing(18)

        # Controls
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(14)

        lang_combo = QComboBox()
        lang_combo.addItems(["English", "فارسی", "中文", "Русский"])
        lang_combo.setCurrentIndex(0)
        lang_combo.currentIndexChanged.connect(self.change_language)
        lang_combo.setStyleSheet("QComboBox { padding: 10px; border-radius: 12px; font-size: 14px; }")
        controls_layout.addWidget(QLabel(self.lang_manager.tr("language")))
        controls_layout.addWidget(lang_combo)

        theme_combo = QComboBox()
        theme_combo.addItems([
            self.lang_manager.tr("light"), self.lang_manager.tr("dark"),
            self.lang_manager.tr("system"), self.lang_manager.tr("red"), self.lang_manager.tr("blue")
        ])
        theme_combo.currentIndexChanged.connect(self.change_theme)
        theme_combo.setStyleSheet("QComboBox { padding: 10px; border-radius: 12px; font-size: 14px; }")
        controls_layout.addWidget(QLabel(self.lang_manager.tr("theme")))
        controls_layout.addWidget(theme_combo)

        left_layout.addLayout(controls_layout)

        # Color Preview
        self.color_preview = QLabel()
        self.color_preview.setFixedHeight(160)
        self.color_preview.setStyleSheet("background-color: #FF0000; border-radius: 24px; border: 5px solid #1a1a1a;")
        self.color_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        preview_text = QLabel("RGB(255, 0, 0)")
        preview_text.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        preview_layout = QVBoxLayout(self.color_preview)
        preview_layout.addWidget(preview_text)
        self.preview_text = preview_text
        left_layout.addWidget(self.color_preview)

        # Input
        input_tabs = QTabWidget()
        input_tabs.setDocumentMode(True)
        input_tabs.setStyleSheet("QTabWidget::pane { border: 0; } QTabBar::tab { padding: 14px; border-radius: 12px; }")

        rgb_tab = QWidget()
        rgb_layout = QVBoxLayout(rgb_tab)
        rgb_layout.setSpacing(14)
        self.rgb_input = ColorInputWidget(self.lang_manager.tr("rgb"), self.lang_manager)
        self.rgb_input.valueChanged.connect(self.on_rgb_changed)
        rgb_layout.addWidget(self.rgb_input)

        hex_layout = QHBoxLayout()
        hex_layout.setSpacing(10)
        self.hex_input = QLineEdit("#FF0000")
        self.hex_input.setFixedHeight(42)
        self.hex_input.setStyleSheet("QLineEdit { padding: 10px; font-size: 15px; border-radius: 12px; }")
        self.hex_input.textChanged.connect(self.on_hex_changed)
        hex_layout.addWidget(QLabel(self.lang_manager.tr("hex") + ":"))
        hex_layout.addWidget(self.hex_input)
        rgb_layout.addLayout(hex_layout)

        input_tabs.addTab(rgb_tab, self.lang_manager.tr("input"))
        left_layout.addWidget(input_tabs)

        # Right Panel
        right_panel = QFrame()
        right_panel.setFrameShape(QFrame.Shape.StyledPanel)
        right_panel.setStyleSheet("QFrame { border-radius: 20px; background: rgba(255,255,255,0.8); }")
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(18)

        # Output
        output_group = QGroupBox(self.lang_manager.tr("output"))
        output_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 15px; }")
        output_layout = QVBoxLayout(output_group)

        output_tabs = QTabWidget()
        output_tabs.setDocumentMode(True)

        # HSV
        hsv_tab = QWidget()
        hsv_layout = QFormLayout(hsv_tab)
        self.hsv_labels = []
        for label in [self.lang_manager.tr("hue"), self.lang_manager.tr("sat"), self.lang_manager.tr("val")]:
            val_label = QLabel("0")
            val_label.setStyleSheet("font-weight: bold; color: #0055aa; font-size: 15px;")
            hsv_layout.addRow(label + ":", val_label)
            self.hsv_labels.append(val_label)
        output_tabs.addTab(hsv_tab, self.lang_manager.tr("hsv"))

        # HSL
        hsl_tab = QWidget()
        hsl_layout = QFormLayout(hsl_tab)
        self.hsl_labels = []
        for label in [self.lang_manager.tr("hue"), self.lang_manager.tr("sat"), self.lang_manager.tr("lightness")]:
            val_label = QLabel("0")
            val_label.setStyleSheet("font-weight: bold; color: #0055aa; font-size: 15px;")
            hsl_layout.addRow(label + ":", val_label)
            self.hsl_labels.append(val_label)
        output_tabs.addTab(hsl_tab, self.lang_manager.tr("hsl"))

        # CMYK
        cmyk_tab = QWidget()
        cmyk_layout = QFormLayout(cmyk_tab)
        self.cmyk_labels = []
        for label in [self.lang_manager.tr("cyan"), self.lang_manager.tr("magenta"), self.lang_manager.tr("yellow"), self.lang_manager.tr("black")]:
            val_label = QLabel("0")
            val_label.setStyleSheet("font-weight: bold; color: #0055aa; font-size: 15px;")
            cmyk_layout.addRow(label + ":", val_label)
            self.cmyk_labels.append(val_label)
        output_tabs.addTab(cmyk_tab, self.lang_manager.tr("cmyk"))

        # YUV
        yuv_tab = QWidget()
        yuv_layout = QFormLayout(yuv_tab)
        self.yuv_labels = []
        for label in [self.lang_manager.tr("luminance"), "U", "V"]:
            val_label = QLabel("0")
            val_label.setStyleSheet("font-weight: bold; color: #0055aa; font-size: 15px;")
            yuv_layout.addRow(label + ":", val_label)
            self.yuv_labels.append(val_label)
        output_tabs.addTab(yuv_tab, self.lang_manager.tr("yuv"))

        output_layout.addWidget(output_tabs)
        right_layout.addWidget(output_group)

        # Color Picker
        picker_group = QGroupBox(self.lang_manager.tr("picker"))
        picker_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 15px; }")
        picker_layout = QVBoxLayout(picker_group)
        self.picker = ColorPickerWidget()
        self.picker.colorChanged.connect(self.on_color_picked)
        picker_layout.addWidget(self.picker)

        hue_slider = QSlider(Qt.Orientation.Horizontal)
        hue_slider.setRange(0, 360)
        hue_slider.setValue(0)
        hue_slider.valueChanged.connect(self.on_hue_changed)
        hue_slider.setStyleSheet("QSlider::handle { background: #0055aa; width: 24px; height: 24px; border-radius: 12px; }")
        picker_layout.addWidget(QLabel(self.lang_manager.tr("hue")))
        picker_layout.addWidget(hue_slider)
        self.hue_slider = hue_slider

        right_layout.addWidget(picker_group)

        # Harmony
        harmony_group = QGroupBox(self.lang_manager.tr("harmony"))
        harmony_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 15px; }")
        harmony_layout = QGridLayout(harmony_group)
        harmony_layout.setSpacing(10)

        harmonies = [
            self.lang_manager.tr("complementary"),
            self.lang_manager.tr("analogous"),
            self.lang_manager.tr("triadic"),
            self.lang_manager.tr("tetradic")
        ]
        for i, name in enumerate(harmonies):
            btn = QPushButton(name)
            btn.setFixedHeight(48)
            btn.setStyleSheet("QPushButton { font-weight: bold; font-size: 14px; }")
            btn.clicked.connect(lambda checked, idx=i: self.show_harmony(idx))
            harmony_layout.addWidget(btn, i // 2, i % 2)

        right_layout.addWidget(harmony_group)

        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(right_panel, 1)

    def apply_initial_theme(self):
        ThemeManager.apply_theme(QApplication.instance(), "light")

    def change_language(self, index):
        langs = ["en", "fa", "zh", "ru"]
        self.lang_manager.set_language(langs[index])
        self.retranslateUi()
        self.set_rtl_if_needed()

    def set_rtl_if_needed(self):
        if self.lang_manager.current_lang == "fa":
            self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
            QApplication.instance().setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        else:
            self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            QApplication.instance().setLayoutDirection(Qt.LayoutDirection.LeftToRight)

    def change_theme(self, index):
        themes = ["light", "dark", "system", "red", "blue"]
        ThemeManager.apply_theme(QApplication.instance(), themes[index])

    def on_rgb_changed(self, r, g, b):
        if self.updating:
            return
        self.current_r, self.current_g, self.current_b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
        self.update_preview()
        self.update_all_outputs()

    def on_hex_changed(self, text):
        if self.updating:
            return
        if len(text) == 7 and text.startswith("#"):
            try:
                r, g, b = ColorConverter.hex_to_rgb(text)
                self.current_r, self.current_g, self.current_b = r, g, b
                self.rgb_input.set_values(r, g, b)
                self.update_preview()
                self.update_all_outputs()
            except:
                pass

    def on_color_picked(self, r, g, b):
        if self.updating:
            return
        self.current_r, self.current_g, self.current_b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
        self.rgb_input.set_values(r, g, b)
        self.hex_input.setText(ColorConverter.rgb_to_hex(r, g, b))
        self.update_preview()
        self.update_all_outputs()

    def on_hue_changed(self, h):
        if self.updating:
            return
        hsv = ColorConverter.rgb_to_hsv(self.current_r, self.current_g, self.current_b)
        self.picker.set_hsv(h, hsv[1], hsv[2])

    def update_preview(self):
        color = f"rgb({self.current_r}, {self.current_g}, {self.current_b})"
        hex_val = ColorConverter.rgb_to_hex(self.current_r, self.current_g, self.current_b)
        self.color_preview.setStyleSheet(f"background-color: {color}; border-radius: 24px; border: 5px solid #1a1a1a;")
        self.preview_text.setText(f"RGB({self.current_r}, {self.current_g}, {self.current_b})\n{hex_val}")

    def update_all_outputs(self):
        if self.updating:
            return
        self.updating = True

        r, g, b = self.current_r, self.current_g, self.current_b
        hex_val = ColorConverter.rgb_to_hex(r, g, b)
        h, s, v = ColorConverter.rgb_to_hsv(r, g, b)
        h2, s2, l = ColorConverter.rgb_to_hsl(r, g, b)
        c, m, y, k = ColorConverter.rgb_to_cmyk(r, g, b)
        y_val, u, v_val = ColorConverter.rgb_to_yuv(r, g, b)

        self.hex_input.setText(hex_val)

        for i, val in enumerate([h, s, v]):
            self.hsv_labels[i].setText(str(val))
        for i, val in enumerate([h2, s2, l]):
            self.hsl_labels[i].setText(str(val))
        for i, val in enumerate([c, m, y, k]):
            self.cmyk_labels[i].setText(str(val))
        for i, val in enumerate([y_val, u, v_val]):
            self.yuv_labels[i].setText(str(val))

        self.hue_slider.blockSignals(True)
        self.hue_slider.setValue(h)
        self.hue_slider.blockSignals(False)
        self.picker.set_hsv(h, s, v)

        self.updating = False

    def show_harmony(self, type_idx):
        h, s, v = ColorConverter.rgb_to_hsv(self.current_r, self.current_g, self.current_b)
        colors = []
        if type_idx == 0:
            colors = [(h, s, v), ((h + 180) % 360, s, v)]
        elif type_idx == 1:
            colors = [(h, s, v), ((h + 30) % 360, s, v), ((h - 30) % 360, s, v)]
        elif type_idx == 2:
            colors = [(h, s, v), ((h + 120) % 360, s, v), ((h + 240) % 360, s, v)]
        elif type_idx == 3:
            colors = [(h, s, v), ((h + 90) % 360, s, v), ((h + 180) % 360, s, v), ((h + 270) % 360, s, v)]

        dialog = QDialog(self)
        dialog.setWindowTitle(self.lang_manager.tr("harmony"))
        dialog.setMinimumSize(560, 200)
        dialog.setStyleSheet("QDialog { background: #f5f5f5; border-radius: 16px; }")
        layout = QHBoxLayout(dialog)
        layout.setSpacing(18)
        layout.setContentsMargins(24, 24, 24, 24)
        for ch, cs, cv in colors:
            cr, cg, cb = ColorConverter.hsv_to_rgb(ch, cs, cv)
            frame = QFrame()
            frame.setFixedSize(110, 110)
            frame.setStyleSheet(f"background-color: rgb({cr},{cg},{cb}); border-radius: 18px; border: 4px solid #333;")
            label = QLabel(f"RGB({cr},{cg},{cb})")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("color: white; font-weight: bold; font-size: 12px;")
            vbox = QVBoxLayout(frame)
            vbox.addWidget(label)
            layout.addWidget(frame)
        dialog.exec()

    def retranslateUi(self):
        self.setWindowTitle(self.lang_manager.tr("title"))
        self.update_all_outputs()
        self.update_preview()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    font = QFont("Segoe UI", 11)
    app.setFont(font)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())