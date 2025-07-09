#By A_8M_A                                                                                                                                                       logo.py *                                                                                                                                                                    

import os
import re
from pyfiglet import Figlet
# مسح الشاشة
os.system('wget https://raw.githubusercontent.com/xero/figlet-fonts/master/starwars.flf')
os.system('clear')
# إنشاء اللوجو
text = input("Enter text for logo: ")
logo = Figlet(font="starwars").renderText(text)
print("\n" + logo)  # عرض اللوجو

# المسار إلى ملف .zshrc
zshrc_path = os.path.expanduser("~/.zshrc")

# قراءة المحتوى الحالي

existing_content = ""
if os.path.exists(zshrc_path):
    with open(zshrc_path, 'r', encoding='utf-8') as file:
        existing_content = file.read()

# حذف أي تعريفات سابقة للدالة
cleaned_content = re.sub(r'(?:unset -f nn_logo\n)?# دالة عرض اللوجو[\s\S]*?nn_logo\(\) \{.*?\n[\s\S]*?\n\}\n', 
                        '', existing_content, flags=re.DOTALL)

# إضافة الدالة الجديدة
new_function = f"""
# دالة عرض اللوجو
nn_logo() {{


    echo -e "{logo.replace('"', '\\"')}"
    echo -e "\\e[31m       (  .      )        )        .      )  \\e[0m"
    echo -e "\\e[31m        )     (   )    . (    (   (   (    \\e[0m"
    echo -e "\\e[31m      (   (    )  (     ) )\ ) )\ ))\ ))\  \\e[0m"
    echo -e "\\e[31m       )\  )\(((  )\  ( /((()/(()/(()/(()/( \\e[0m"
    echo -e "\\e[31m     ((_)((_))_)((_) )(_))/(_))/(_))/(_))_) \\e[0m"
    echo -e "\\e[31m            (---------------------)\\e[0m"
    echo -e "\\e[31m             |   HALLO  HACKER   |\\e[0m"
    echo -e "\\e[31m            (---------------------)\\e[0m"
    echo -e "\\e[31m     ((_)((_))_)((_) )(_))/(_))/(_))/(_))_) \\e[0m"
}}
nn_logo
"""
# كتابة المحتوى المحدث
with open(zshrc_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_content + new_function)
