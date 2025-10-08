# CSV Column Extractor

`CSV Column Extractor`は、大規模なCSVファイルから必要な列だけを簡単かつ高速に抽出するためのPythonスクリプトです。設定ファイルを使って抽出したい列名を指定するだけで、新しいCSVファイルを生成します。

---

## ✨ 主な機能

- **設定ファイルベース**: `config.ini`ファイルに設定を記述するだけで、スクリプトの変更は不要です。
- **複数列の指定**: 抽出したい列をカンマ区切りで複数指定できます。
- **高速な処理**: データ操作に最適化された`pandas`ライブラリを使用しており、大きなファイルも効率的に処理します。
- **エラーハンドリング**: ファイルが存在しない場合や、指定した列が見つからない場合に警告やエラーメッセージを表示します。

---

## ⚙️ 動作要件

- Python 3.8 以上
- **pandas** およびその依存ライブラリ (`numpy`, `python-dateutil`, `pytz`, `six`)

---

## 🚀 使い方

1.  **リポジトリのクローンまたはダウンロード**
    ```bash
    git clone https://github.com/git-756/csv-tool.git
    cd csv-tool
    ```

2.  **設定ファイルの準備**
    - `csv_column_extractor/config.ini.sample` をコピーして、同階層に `config.ini` という名前で保存します。

3.  **`config.ini`の編集**
    - `config.ini`ファイルを開き、自分の環境に合わせて以下の項目を設定します。

    ```ini
    [SETTINGS]
    # 入力する元のCSVファイル名を指定します
    input_csv_file = path/to/your/source_data.csv

    # 出力する新しいCSVファイル名を指定します
    output_csv_file = path/to/your/extracted_data.csv

    # 抽出したいヘッダー（列名）をカンマ(,)区切りで指定します
    target_headers = 氏名,メールアドレス,購入製品
    ```

4.  **スクリプトの実行**
    - ターミナルで以下のコマンドを実行します。

    ```bash
    python csv_column_extractor/extract_csv.py
    ```

5.  **結果の確認**
    - 処理が完了すると、`output_csv_file`で指定したパスに、指定した列だけが含まれた新しいCSVファイルが作成されます。

---

## 📜 ライセンス

このプロジェクトは **MIT License** のもとで公開されています。ライセンスの全文については、[LICENSE](LICENSE) ファイルをご覧ください。

また、このプロジェクトはサードパーティ製のライブラリを利用しています。これらのライブラリのライセンス情報については、[NOTICE.md](NOTICE.md) ファイルに記載しています。

## 作成者
Samurai-Human-Go
- [ブログ記事: 【Python開発物語】CSV列抽出スクリプトが「賢いツール」に進化するまで（Pandasと設定ファイル）](https://samurai-human-go.com/python-pandas-csv-tool-story/)