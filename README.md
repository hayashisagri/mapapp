### 訪問した都道府県の記録アプリ

ローカル環境構築手順
- 前提条件
python3系がインストールされている
<br>

1. 空のディレクトリを作成
```
mkdir example
```

2. `cd example`

3. `git clone git@github.com:hayashisagri/mapapp.git`

4. python仮想環境を作成する
```
$ python -m venv example
$ source example/bin/activate

# (venv)$と表示されていれば成功
```

5. 各種ライブラリのインストール
```
pip install django==3.2
pip install Pillow
```
6. `cd mapapp`

7. データベース初期化
```
python manage.py migrate
```

8. server起動
```
python manage.py runserver
```

9. localhostにアクセス
```
http://127.0.0.1:8000/home/
```
