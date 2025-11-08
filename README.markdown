# Advanced Color Converter Pro

## English

### Overview
**Advanced Color Converter Pro** is a sophisticated, cross-platform desktop application built with Python and PyQt6. It provides real-time color conversion across multiple color spaces: RGB, HEX, HSV, HSL, CMYK, and YUV. Featuring an interactive color picker, color harmony tools, multi-language support, and modern theming, it is the ultimate tool for designers, developers, and digital artists.

### Key Features
- **Real-Time Conversion**: Instantly convert between RGB, HEX, HSV, HSL, CMYK, and YUV with live updates.
- **Interactive Color Picker**: Advanced HSV-based picker with hue slider and saturation/value gradient canvas.
- **Color Harmony Generator**: Visualize Complementary, Analogous, Triadic, and Tetradic color schemes.
- **Multi-Language Support**: English, فارسی (Persian with RTL), 中文 (Chinese), Русский (Russian) – fully localized UI.
- **Dynamic Themes**: Light, Dark, System Default, Red, and Blue themes with smooth palette transitions.
- **Input Methods**: RGB spin boxes, HEX text input, and color picker – all synchronized.
- **Copy to Clipboard**: One-click copy of RGB values.
- **Modern UI**: Rounded corners, gradients, shadows, and responsive layout inspired by Windows 11.
- **RTL Layout Support**: Automatic right-to-left alignment for Persian.

### Requirements
- Python 3.8+
- PyQt6

### Installation
1. Ensure Python is installed.
2. Install dependencies:
   ```bash
   pip install PyQt6
   ```
3. Run the application:
   ```bash
   python color_converter.py
   ```

### Usage
- **Select Language & Theme**: Use dropdowns in the top-left for instant switching.
- **Input Color**: 
  - Enter RGB values in spin boxes.
  - Type HEX code (e.g., `#FF0000`).
  - Drag on the color picker canvas.
- **View Outputs**: All color spaces update in real time.
- **Color Harmony**: Click buttons to see complementary or analogous colors.
- **Copy**: Click "Copy" to copy `RGB(r, g, b)` to clipboard.

### Screenshots
- Dual-panel layout with input and output tabs  
- Interactive color picker with hue slider and gradient  
- Color harmony dialog with live swatches  
- Persian RTL interface with full translation  
- Dark and custom Red/Blue themes  

### Technical Highlights
- **Color Space Algorithms**: Accurate conversions using `colorsys` and custom YUV/CMYK logic.
- **Thread-Safe Updates**: Prevents UI recursion with `updating` flags.
- **Dynamic Theming**: Palette-based themes with full control over colors.
- **Event-Driven Architecture**: Signals and slots for seamless synchronization.

### Contributing
Fork, improve, or add new color spaces (LAB, XYZ). Pull requests and suggestions are welcome!

### License
MIT License – Free to use, modify, and distribute.

---

## فارسی

### بررسی اجمالی
**مبدل پیشرفته رنگ پرو** یک برنامه دسکتاپ حرفه‌ای و چندپلتفرمی است که با پایتون و PyQt6 ساخته شده. این ابزار تبدیل لحظه‌ای رنگ بین فضاهای رنگی مختلف را فراهم می‌کند: RGB، HEX، HSV، HSL، CMYK و YUV. با انتخابگر رنگ تعاملی، ابزار هارمونی رنگ، پشتیبانی چندزبانه و تم‌های مدرن، بهترین ابزار برای طراحان، توسعه‌دهندگان و هنرمندان دیجیتال است.

### ویژگی‌های کلیدی
- **تبدیل لحظه‌ای**: تبدیل فوری بین RGB، HEX، HSV، HSL، CMYK و YUV با به‌روزرسانی زنده.
- **انتخابگر رنگ تعاملی**: انتخابگر مبتنی بر HSV با اسلایدر رنگ و گرادیان اشباع/روشنایی.
- **تولیدکننده هارمونی رنگ**: نمایش مکمل، مشابه، سه‌گانه و چهارگانه.
- **پشتیبانی چندزبانه**: انگلیسی، فارسی (با راست‌چین)، چینی، روسی – ترجمه کامل رابط کاربری.
- **تم‌های پویا**: روشن، تاریک، پیش‌فرض سیستم، قرمز و آبی با انتقال نرم پالت.
- **روش‌های ورودی**: جعبه‌های اسپین RGB، ورودی متنی HEX و انتخابگر رنگ – همه همگام.
- **کپی در کلیپ‌بورد**: کپی یک‌کلیکی مقدار `RGB(r, g, b)`.
- **رابط کاربری مدرن**: گوشه‌های گرد، گرادیانت، سایه و چیدمان پاسخگو الهام‌گرفته از ویندوز ۱۱.
- **پشتیبانی راست‌چین**: جهت‌گیری خودکار برای فارسی.

### پیش‌نیازها
- پایتون ۳.۸ یا بالاتر
- PyQt6

### نصب
۱. پایتون را نصب کنید.
۲. وابستگی‌ها را نصب نمایید:
   ```bash
   pip install PyQt6
   ```
۳. برنامه را اجرا کنید:
   ```bash
   python color_converter.py
   ```

### نحوه استفاده
- **انتخاب زبان و تم**: از منوهای کشویی بالا-چپ برای تغییر فوری استفاده کنید.
- **ورود رنگ**:
  - مقادیر RGB را در جعبه‌ها وارد کنید.
  - کد HEX را تایپ کنید (مثل `#FF0000`).
  - روی صفحه انتخابگر بکشید.
- **مشاهده خروجی**: تمام فضاهای رنگی به‌صورت زنده به‌روزرسانی می‌شوند.
- **هارمونی رنگ**: روی دکمه‌ها کلیک کنید تا رنگ‌های مکمل یا مشابه ببینید.
- **کپی**: روی "کپی" کلیک کنید تا `RGB(r, g, b)` در کلیپ‌بورد کپی شود.

### تصاویر
- چیدمان دوپنل با تب‌های ورودی و خروجی  
- انتخابگر رنگ تعاملی با اسلایدر رنگ و گرادیان  
- پنجره هارمونی با نمونه‌های زنده  
- رابط فارسی راست‌چین با ترجمه کامل  
- تم‌های تاریک و قرمز/آبی سفارشی  

### نکات فنی
- **الگوریتم‌های فضای رنگی**: تبدیل دقیق با `colorsys` و منطق سفارشی YUV/CMYK.
- **به‌روزرسانی ایمن**: جلوگیری از تکرار با پرچم `updating`.
- **تم‌بندی پویا**: تم‌های مبتنی بر پالت با کنترل کامل رنگ‌ها.
- **معماری رویدادمحور**: سیگنال‌ها و اسلات‌ها برای همگام‌سازی بی‌نقص.

### مشارکت
فورک کنید، بهبود دهید یا فضای رنگی جدید (LAB، XYZ) اضافه کنید. Pull requestها و پیشنهادها خوش‌آمد!

### مجوز
مجوز MIT – آزاد برای استفاده، تغییر و توزیع.

---

## 中文

### 概述
**高级颜色转换器专业版** 是一款精致的跨平台桌面应用程序，使用 Python 和 PyQt6 构建。它提供多种颜色空间之间的实时转换：RGB、HEX、HSV、HSL、CMYK 和 YUV。配备交互式颜色选择器、颜色和谐工具、多语言支持和现代主题，是设计师、开发者和数字艺术家的终极工具。

### 主要功能
- **实时转换**：在 RGB、HEX、HSV、HSL、CMYK 和 YUV 之间即时转换，实时更新。
- **交互式颜色选择器**：基于 HSV 的高级选择器，带色相滑块和饱和度/明度渐变画布。
- **颜色和谐生成器**：可视化互补色、类似色、三色调和四色调。
- **多语言支持**：英语、波斯语（RTL）、中文、俄语 – 完全本地化的 UI。
- **动态主题**：明亮、暗黑、系统默认、红色和蓝色主题，平滑调色板过渡。
- **输入方式**：RGB 数值框、HEX 文本输入和颜色选择器 – 全部同步。
- **一键复制**：点击“复制”将 `RGB(r, g, b)` 复制到剪贴板。
- **现代 UI**：圆角、渐变、阴影和响应式布局，灵感来自 Windows 11。
- **RTL 布局支持**：为波斯语自动右到左对齐。

### 要求
- Python 3.8+
- PyQt6

### 安装
1. 确保已安装 Python。
2. 安装依赖项：
   ```bash
   pip install PyQt6
   ```
3. 运行应用程序：
   ```bash
   python color_converter.py
   ```

### 使用方法
- **选择语言与主题**：使用左上角下拉菜单即时切换。
- **输入颜色**：
  - 在数值框中输入 RGB 值。
  - 输入 HEX 代码（如 `#FF0000`）。
  - 在颜色选择器画布上拖动。
- **查看输出**：所有颜色空间实时更新。
- **颜色和谐**：点击按钮查看互补色或类似色。
- **复制**：点击“复制”将 `RGB(r, g, b)` 复制到剪贴板。

### 截图
- 双面板布局，带输入和输出选项卡  
- 交互式颜色选择器，带色相滑块和渐变  
- 颜色和谐对话框，带实时色块  
- 波斯语 RTL 界面，完整翻译  
- 暗黑和自定义红/蓝主题  

### 技术亮点
- **颜色空间算法**：使用 `colorsys` 和自定义 YUV/CMYK 逻辑的精确转换。
- **线程安全更新**：使用 `updating` 标志防止 UI 递归。
- **动态主题**：基于调色板的主题，完全控制颜色。
- **事件驱动架构**：信号和槽实现无缝同步。

### 贡献
Fork 仓库，改进或添加新颜色空间（LAB、XYZ）。欢迎 Pull Request 和建议！

### 许可证
MIT 许可证 – 免费用于个人和商业用途、修改和分发。