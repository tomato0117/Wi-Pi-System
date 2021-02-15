#Wi-Pi
**必ずDesktop直下に設置してください プログラムがエラーを吐き、動作しない可能性があります**

    ├── main
    │   │
    │   ├── Wi-Pi.py　メインプログラム
    │   ├── grove_gesture_sensor.py　ジェスチャーセンサを使うためのもの
    │   └── Wi-Pi.json　データ保存に使用するもの（使ってはいないが、処理自体はメインプログラムにコメントアウトして残してある）
    │
    └── test テストや、開発で使ったものを全ている
        │
        ├── Blynk(このディレクトリのものは、mainでも使われています)
        │   │
        │   ├── main.cpp　Blynkのメインファイル
        │   └── main.o　　main.cppのコンパイル後に出てくるファイル
        │
        ├── Data      データを置いておくディレクトリ
        │   │
        │   ├── Wi-Pi.json　　ges-endress.pyで使用していたjson ges-reverse.pyにも組み込んではいるが、使わないんじゃないかとか思ったりしてる
        │   └── test.json   Other/testjson.pyで使用されているテストファイル（変数の保存用）
        │
        ├── Gesture　ジェスチャー関連のディレクトリ（下に行くほど新しい）
        │   │
        │   ├── grove_gesture_sensor.py　ジェスチャーセンサを使うためのファイル（Groveライブラリの一種かと）
        │   ├── grove_gesture_sensor.pyc　ジェスチャーセンサのキャッシュのようなものと考えている
        │   ├── test_value.py     LEDの点滅をジェスチャー認識ごとに切り替えられるようにしたもの
        │   │── test_value2.py　　test_value.pyからLED部分を関数化したもの
        │   ├── ges-router.py　　ルーターのonoff機能を追加したもの
        │   ├── ges-thread.py     ges-router.pyのコピー
        │   ├── ges-ledd.py     スレッドで書いてエラーが解決できなかったもの
        │   ├── ges-multi.py　　マルチプロセスコマンドを使用し、解決を求めたが、不可能だったもの
        │   ├── ges-singleWhile.py　スレッドを一時諦め、点滅の処理もWhile Trueの中に入れたもの
        │   ├── ges-wthread-ledd.py　実行時にインスタンスを立て、Thread問題を解決しようとしたもの
        │   ├── ges-subprocess.py　subprocessコマンドにてThreadと同じことをしようとしたもの
        │   ├── ges-endress.py  スレッドセーフで書かれていないため、プログラムが落ちて再起動を行う処理があるもの
        │   └── ges-reverse.py　もっともmain/Wi-Piに近い状態のもの
        │
        └── Other　LEDやjsonファイルなどテストプログラムなどが入っている
            │
            ├── led-change.py　LEDを変数によって切り替えられることを目的としたテストファイル
            ├── led.py          Blynkからアプリを操作する際にLED点滅をさせているプログラム（main.cppから呼び出し）
            ├── led_thread.py　ges-subprocess.pyなどで、LEDを無限ループさせた状態で呼び出せば行けるのかと想定したがダメだったもの（ただLEDは点滅し続ける）
            ├── test_thread.py  スレッドをしようとしてテストに使用したファイル（grs-router.py)がベース
            ├── thread_cpp.py　インターネット上から自由にスレッドを停止したりできるというものを見つけたもののコピーファイル
            ├── th-ledd.py    thread_cpp.pyにLEDの処理とカウントアップを組み込んだもの
            ├── thread.py　　　スレッドをデーモン化させるというものを見つけ、そこに、LEDの処理だけを入れたもの
            └── testjson.py　　Jsonをテストするために使用しているプログラム
