# Copyright © 2023 Takenoko
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

import glob
import os
from PIL import Image, PngImagePlugin
from datetime import datetime
from pywintypes import Time

# Windowsの場合
on_windows = os.name == 'nt'
if on_windows:
    import win32file
    import win32con

input_folder = 'inputs'
output_folder = 'outputs'

# 画像の拡張子と対応する形式を定義
# ※大文字も可
image_formats = {
    'JPEG': ('jpg', 'jpeg'),
    'PNG': ('png'),
    'WEBP': ('webp')
}

# メタデータとアルファチャンネルを削除する関数
def process_image(input_path, output_path, image_formats):
    try:
        with Image.open(input_path) as img:
            print(f"Processing {input_path}")
            # アルファチャンネルを削除
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                img = img.convert('RGB')

            # ファイルの拡張子を取得
            file_extension = os.path.splitext(input_path)[-1]

            # 対応する形式のメタデータを削除
            for format_name, format_extensions in image_formats.items():
                # ドットを除いた拡張子を比較
                if file_extension[1:].lower() in format_extensions:
                    # 新しいファイル名を生成
                    input_filename = os.path.basename(input_path)
                    output_filename = os.path.splitext(input_filename)[0] + "_rm" + file_extension
                    output_path = os.path.join(output_folder, output_filename)

                    # ファイルを保存
                    if format_name == 'JPEG' or 'WEBP':
                        quality = img.info.get('quality', 80) + 5
                        img.save(output_path, format=format_name, quality=quality)
                    else:
                        img.save(output_path, format=format_name)

                    # 日時情報を取得
                    access_time = os.path.getatime(input_path)  # アクセス日時
                    modify_time = os.path.getmtime(input_path)  # 更新日時

                    if on_windows:
                        creation_time = os.path.getctime(input_path)  # 作成日時

                    # 日付情報の設定
                    # ファイルのハンドルを取得（Windowsのみ）
                    if on_windows:
                        handle = win32file.CreateFile(
                            output_path,
                            win32con.GENERIC_WRITE,
                            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
                            None,
                            win32con.OPEN_EXISTING,
                            0,
                            None
                        )

                        # 元画像の作成日時、アクセス日時、更新日時を設定
                        win32file.SetFileTime(handle, Time(creation_time), Time(access_time), Time(modify_time))

                        # ハンドルを閉じる
                        handle.Close()

                    # 他のプラットフォームではアクセス日時と更新日時を設定
                    os.utime(output_path, (access_time, modify_time))

                    break
            else:
                print(f"Unsupported format for {input_path}")
    except Exception as e:
        # ファイル名が特定のパターンに一致する場合エラーメッセージを表示しない
        if os.path.basename(input_path) == "Put File(PNG JPEG WEBP) here.txt":
            return
        print(f"{str(e)}")

# 入力フォルダ内の画像を処理
print("Converting...")
for root, _, files in os.walk(input_folder):
    for filename in files:
        input_path = os.path.join(root, filename)
        output_path = os.path.join(output_folder, filename)
        process_image(input_path, output_path, image_formats)
print("Conversion completed.")
