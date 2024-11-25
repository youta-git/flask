### Week08～10課題「FlaskでWebサービスを作成する」用Dockerファイルのサンプルです
以下の手順で環境を構築ください。

## ■■■ Linux（本番環境）の構築方法 ■■■
#### TeraTermでログインする
- プロンプトが`[user2@week08 ~]$`であるならばOK

#### リポジトリをクローンする
```sh
git clone https://github.com/（自分のGitHubアカウント名）/flask.git
```

#### カレントディレクトリを`flask`へ変更する
```sh
cd flask
```

#### Dockerでcompose upする
```sh
docker compose down; docker compose up -d --build
```

#### WindowsのWebブラウザーで[http://192.168.56.102:5000/](http://192.168.56.102:5000/)にアクセスする
- アプリ画面が表示したらOK

## ■■■ Windows（開発環境）の構築方法 ■■■
#### コマンドプロンプトを開く
- カレントディレクトリが`c:\Users\(学生番号)`であるならばOK
  - そうでない場合は`c:\Users\(学生番号)`へ移動する

#### gitの環境変数を設定する
```sh
git config --global user.name "（フルネームをローマ字で）"
git config --global user.email （メールアドレス）
git config --global init.defaultBranch main
```

#### リポジトリをクローンする
```sh
git clone https://github.com/（自分のGitHubアカウント名）/flask.git
```

#### カレントディレクトリを`flask`へ変更する
```sh
cd flask
```

#### Flask開発用環境を作成する
```sh
python -m venv --upgrade-deps .venv
```

#### Flask開発用環境に入る
```sh
.venv\Scripts\activate
```

#### Flask開発用のPythonパッケージをインストールする
```sh
pip install -r requirements.txt
```

#### VSCodeで開発環境を開く
- メニュー`ファイル(F)`-`フォルダーを開く...`で、`c:\ユーザー\(自分の学生番号)\flask`を開く

#### VSCodeをFlask開発用に設定する
1. メニュー`表示(V)`-`ターミナル`で、右下にターミナルを表示する
  1-1. ターミナルでも、Flask開発用環境に入る
```sh
.\.venv\Scripts\activate
```
2. 左側のツリービューから`src\app.py`を開く
1. 右下の表示が`Python 3.12.6('.venv')`になっていることを確認する。
  3-1. `Python 3.12.6('.venv')`以外になっている場合は切り替える
1. `実行とデバッグ`を開く
1. リンク`launch.jsonファイルを作成します`をクリックする
1. デバッガーの種類から`Python Debugger`を選択する
1. デバッグ構成から`Flask`を選択する
1. `app.py`を選択する
1. launch.jsonが開くので、`"module": "flask",`の1行下に以下を追加する
```
"cwd": "${workspaceFolder}\\src",
```
10. launch.jsonを保存して閉じる
1. ここまで出来たら、いったんVSCodeを閉じる

#### VSCodeでFlaskの動作確認を行う
- メニュー`ファイル(F)`-`フォルダーを開く...`で、`c:\ユーザー\(学生番号)\flask`を開く
- ターミナルでも、Flask開発用環境に入る
```sh
.\.venv\Scripts\activate
```
- 左側のツリービューから`src\app.py`を開く
  - 右下の表示が`Python 3.12.6('.venv')`になっていることを確認する。
  - `Python 3.12.6('.venv')`以外になっている場合は切り替える
- F5キーを押す
  - ターミナルに「* Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)」と表示するので、Ctrlキーを押しながらURLをクリックする
  - Webブラウザーが開き、アプリ画面が表示したらOK
  - 確認が終わったら、停止ボタンをクリックする
