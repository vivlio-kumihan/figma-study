import glob
import os
import sys
sys.path.append('../lib')
from tika import parser

file_path = glob.glob("./*.pdf")

for file in file_path:
    # 下準備　ファイル名取得　拡張子を取ったオリジナルのファイル名が欲しい。
    basename, ext = os.path.splitext( os.path.basename(file) )
    # docx2pythonのインスタンスを作成する。
    pdf = parser.from_file(file)
    # content = extract_text(file)

    # 本文、ルビ、脚注を抜き出すメソッドを呼んで、オブジェクトに格納する。
    # contents = t14i_regex.text_ins_reg(doc)
    with open(f'{basename}.txt', "w") as f:
        f.write(pdf["content"])
