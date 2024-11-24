Week08～10課題「FlaskでWebサービスを作成する」用Dockerファイルのサンプルです

以下の手順で環境を構築します。
--- Linux ---
1. TeraTermでログインする
プロンプトが「[user2@week08 ~]$」であるならばOK

2. リポジトリをクローンする
git clone https://github.com/（自分のGitHubアカウント）/flask.git

3. カレントディレクトリを「flask」へ変更する
cd flask

4. Dockerでcompose upする
docker compose down; docker compose up -d --build

5. WindowsのWebブラウザーで「http://192.168.56.102:5000/」にアクセスする
アプリ画面が表示したらOK

--- Windows ---
1. コマンドプロンプトを開く
カレントディレクトリが「c:\Users\(自分の学生番号)」であるならばOK
そうでない場合は「c:\Users\(自分の学生番号)」へ移動する

2. gitの環境変数を設定する
git config --global user.name "（フルネームをローマ字で）"
git config --global user.email （メールアドレス）
git config --global init.defaultBranch main

3. リポジトリをクローンする
git clone https://github.com/（自分のGitHubアカウント）/flask.git

4. カレントディレクトリを「flask」へ変更する
cd flask

5. Flask開発用環境を作成する
python -m venv --upgrade-deps .venv

6. Flask開発用環境に入る
.venv\Scripts\activate

7. Flask開発用のPythonパッケージをインストールする
pip install -r requirements.txt

8. VSCodeを表示する
メニュー「ファイル(F)」-「フォルダーを開く...」で、「c:\ユーザー\(自分の学生番号)\flask」を開く

9. VSCodeをFlask開発用に設定する
メニュー「表示(V)」-「ターミナル」で、右下にターミナルを表示する
ターミナルでも、Flask開発用環境に入る
.\.venv\Scripts\activate
左側のツリービューから「src\app.py」を開く
右下の表示が「Python 3.12.6('.venv')」になっていることを確認する。「Python 3.12.6('.venv')」以外になっている場合は切り替える
「実行とデバッグ」を開く
「launch.jsonファイルを作成します」をクリックする
デバッガーの種類から「Python Debugger」を選択する
デバッグ構成から「Flask」を選択する
「app.py」を選択する
launch.jsonが開くので、「"module": "flask",」の1行下に、以下を追加する
"cwd": "${workspaceFolder}\\src",
launch.jsonを保存して閉じる
ここまで出来たら、いったんVSCodeを閉じる

10. VSCodeを表示する
メニュー「ファイル(F)」-「フォルダーを開く...」で、「c:\ユーザー\(自分の学生番号)\flask」を開く
ターミナルでも、Flask開発用環境に入る
.\.venv\Scripts\activate
左側のツリービューから「src\app.py」を開く
右下の表示が「Python 3.12.6('.venv')」になっていることを確認する。「Python 3.12.6('.venv')」以外になっている場合は切り替える
F5キーを押す
ターミナルに「* Running on http://127.0.0.1:5000」と表示するので、Ctrlキーを押しながらURLをクリックする
Webブラウザーが開き、アプリ画面が表示したらOK
確認が終わったら、停止ボタンをクリックする