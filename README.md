# remove-meta-alpha
[日本語](#日本語) | [English](#english)

# 日本語

# 説明

本ツールは、複数画像のメタデータとアルファチャンネルの削除を一括して処理することができます。
<br><br>

# 特徴

- **対応画像形式**: JPEG, PNG, WEBP ※拡張子は小文字、大文字どちらにも対応しています。
- **メタデータの削除**: 画像ファイルからメタデータを削除します。
- **アルファチャンネルの削除**: 画像ファイルからアルファチャンネルを削除します。※NovelAI生成画像のアルファチャンネルに埋め込まれたメタデータの削除を目的としています。
- **日時情報の保持**: Windowsの場合はファイルの作成日時と更新日時を保持します。Mac, Linuxの場合は更新日時を保持します。
- **ファイル名**: ファイル名の末尾に_rmが追加されます。拡張子は元の画像と同じものになります。
<br><br>

# 前提
- Python 3.x
<br><br>

# 準備
以下のライブラリを使用するため、入っていない場合はインストールします。
- PIL  
~~~
pip install pillow
~~~

Windowsのみ  
- pywin32  
~~~
pip install pywin32
~~~
<br>

# 使い方
1. inputsフォルダに変換したい画像を入れます。  
2. Windowsの場合はremove-meta-alpha.batをダブルクリックします。Mac, Linuxの場合はremove-meta-alpha.pyを実行します。コマンドラインが起動します。  
3. outputsフォルダに画像が保存されます。コマンドラインが閉じます。
<br><br>

# 設定変更等  
- 処理完了後にコマンドラインを閉じないようにしたい場合はbatファイル内の@REM pauseのコメントアウトを外してください。
<br><br>

# 変更履歴

## [1.0.0] - 2023-12-20
### 追加
- GitHubで公開
<br><br>

# ライセンス
Copyright © 2023 Takenoko  
Released under the [MIT](https://opensource.org/licenses/mit-license.php) license.
<br><br><br>

# English

# Description

This tool allows you to process multiple images simultaneously, including removing metadata and alpha channels from the images.
<br><br>

# Features

- **Supported Image Formats**: JPEG, PNG, WEBP ※Supports both lowercase and uppercase extensions.
- **Metadata Removal**: Removes metadata from image files.
- **Alpha Channel Removal**: Removes alpha channels from image files. ※Intended for removing metadata embedded in alpha channels of NovelAI-generated images.
- **Date Information Preservation**: On Windows, the file's creation and modification dates are preserved. On Mac and Linux, the modification date is preserved.
- **File Name**: The suffix _rm is added to the file name. The extension remains the same as the original image.
<br><br>

# Prerequisites
- Python 3.x
<br><br>

# Preparation
Install the following libraries if not already installed:
- PIL  
~~~
pip install pillow
~~~

Windows only  
- pywin32  
~~~
pip install pywin32
~~~
<br>

# How to Use
1. Place the images you want to convert in the inputs folder.  
2. On Windows, double-click remove-meta-alpha.bat. On Mac and Linux, execute remove-meta-alpha.py. A command line will launch.  
3. Images will be saved in the outputs folder. The command line will close.
<br><br>

# Configuration and Modifications  
- If you want to keep the command line open after processing, uncomment @REM pause in the bat file.
<br><br>

# Change Log

## [1.0.0] - 2023-12-20
### Added
- Published on GitHub
<br><br>

# License
Copyright © 2023 Takenoko  
Released under the [MIT](https://opensource.org/licenses/mit-license.php) license.
