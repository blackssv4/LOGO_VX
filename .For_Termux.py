import os
import re
from pyfiglet import Figlet
class Colors:
    LIGHT_GREEN = '\033[92m'
    RED = '\033[91m'
# مسار ملف bashrc
bashrc_path = os.path.expanduser("~/.bashrc")

# توليد اللوجو
text = input(f"{Colors.LIGHT_GREEN}Enter text for logo: {Colors.RED}")
logo = Figlet(font="3d").renderText(text)

# معالجة اللوجو
logo_clean = logo.replace('"', '\\"').replace("\n", "\\n")
logo_block = f'    echo -e "{logo_clean}"'

# قراءة bashrc الحالي
with open(bashrc_path, 'r', encoding='utf-8') as file:
    content = file.read()

# هل الدالة موجودة؟
if 'nn_logo()' in content:
    print(f"{Colors.LIGHT_GREEN}The Function Already Exists . Update Will Be Performed")

    # استبدال اللوجو القديم بالجديد داخل الدالة
    content = re.sub(
        r'nn_logo\(\) \{\n    clear\n    echo -e ".*?"',
        f'nn_logo() {{\n    clear\n{logo_block}',
        content,
        flags=re.DOTALL
    )

else:
    print("✅ إضافة دالة nn_logo() جديدة.")

    # تجهيز الدالة الكاملة
    function_code = f"""

# دالة عرض اللوجو
nn_logo() {{
    clear
    echo -e "{logo_clean}"
    echo -e "\\e[31m        (  .      )        )        .      )  \\e[0m"
    echo -e "\\e[31m         )     (   )    . (    (   (   (    \\e[0m"
    echo -e "\\e[31m       (   (    )  (     ) )\\ ) )\\ ))\\ ))\\  \\e[0m"
    echo -e "\\e[31m        )\\  )\\(((  )\\  ( /((()/(()/(()/(()/( \\e[0m"
    echo -e "\\e[31m      ((_)((_))_)((_) )(_))/(_))/(_))/(_))_) \\e[0m"
    echo -e "\\e[31m             (---------------------)\\e[0m"
    echo -e "\\e[31m              |   HALLO  HACKER   |\\e[0m"
    echo -e "\\e[31m             (---------------------)\\e[0m"
    echo -e "\\e[31m      ((_)((_))_)((_) )(_))/(_))/(_))/(_))_) \\e[0m"
}}
nn_logo
"""
    content += function_code

# كتابة التعديلات في bashrc
with open(bashrc_path, 'w', encoding='utf-8') as file:
    file.write(content)


