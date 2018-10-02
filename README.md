# demo20180922  
demo on 20180922  
父母懇親会  
  
## Overview  
測距センサで常時距離を計測  
↓  
測距センサで測っている距離が50cm以内になったらGoogle Homeで音声を再生する  
↓  
音声を再生した後に、今の時刻をGoogleスプレッドシートに書き込む  
  
  
## Code contents  
  
- `main.py`を起動  
    - ここでGoogle Homeでの音声再生をスムーズに行う為に事前にGoogle Homeと接続をしておく  
  
- [超音波距離センサー](http://akizukidenshi.com/catalog/g/gM-11009/)で常時センサ前方の距離を計測  
    - `HC_SR04.py` 距離を返す関数measureを内包  
        - 常に距離を出力（50cm以内であろうがなかろうが）  
  
- センサで計測している値が50cm以内になったらGoogle Homeで音声を再生  
    - 再生する音声は[Sound of text](https://soundoftext.com/)を利用して静的にmp3ファイルを生成  
  
- 今の時刻をGoogleスプレッドシートに書き込む  
    - 書き込むセル番号は静的に処理しなければならず外部ファイル`nowRowNumber.txt`に次書き込むべき行番号を記載  
        - 次書き込むべき行番号を読み込み、+1して書き込みする  
        - テキストファイルを読み込む時、終端文字が含まれているので処理が必要（`GSS_writing.py`内15, 16行）  
  
## Sensor  
[超音波距離センサー HC-SR04](http://akizukidenshi.com/catalog/g/gM-11009/)  
