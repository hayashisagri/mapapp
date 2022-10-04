## 訪問した都道府県の記録アプリ

###ローカル環境構築手順
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

###説明資料
<iframe class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/4a60fc70481342509b01c893d01cf2ed" title="mapapp" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 560px; height: 315px;" data-ratio="1.7777777777777777"></iframe>
