# 使い方
## 最初に
accessTokenを取得して、headersの部分の修正を行ってください。

以下参照です。

<https://developer.aibo.com/jp/docs#%E3%83%88%E3%83%BC%E3%82%AF%E3%83%B3%E3%81%AE%E5%8F%96%E5%BE%97>


accessTokenを取得したら、deviceIdを取得して変数deviceIdに代入してください。

以下参照です。

<https://developer.aibo.com/jp/docs#getdevices>

## Action API

```
$ python aibo_api コマンド パラメーター
```
例えば……

```
$ python aibo_api.py turn_around '{\"TurnSpeed\":2,\"TurnAngle\":180}'
```
これで180度aiboが回ります。

行動してから値が返ってくるので、SUCCESSが返ってくるまでかなり時間がかかります。

以下コマンド集です。

<https://developer.aibo.com/jp/docs#action-api>

## Cognition API

```
$ python aibo_api コマンド 
```
例えば……

```
$ python aibo_api.py hungry_status
```
これでバッテリー残量statusが返ってきます

SUCCESSが返ってくるまで数秒がかかります。

以下コマンド集です。

<https://developer.aibo.com/jp/docs#cognition-api>