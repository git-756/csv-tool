import csv

def extract_specific_columns(input_filename, output_filename, headers_to_keep):
    """
    CSVファイルから指定されたヘッダーの列のみを抽出し、新しいCSVファイルに保存します。

    Args:
        input_filename (str): 入力CSVファイルのパス。
        output_filename (str): 出力CSVファイルのパス。
        headers_to_keep (list): 抽出したいヘッダー名のリスト。
    """
    try:
        with open(input_filename, 'r', encoding='utf-8', newline='') as infile, \
             open(output_filename, 'w', encoding='utf-8', newline='') as outfile:

            # 入力ファイルを辞書形式で読み込むリーダーを作成
            reader = csv.DictReader(infile)

            # headers_to_keepに存在しないヘッダーが指定された場合のエラーチェック
            missing_headers = set(headers_to_keep) - set(reader.fieldnames)
            if missing_headers:
                print(f"エラー: 指定されたヘッダーが見つかりません: {', '.join(missing_headers)}")
                return

            # 出力ファイルに書き込むライターを作成
            # fieldnamesには抽出したいヘッダーのリストを指定
            writer = csv.DictWriter(outfile, fieldnames=headers_to_keep)

            # 最初にヘッダーを書き込む
            writer.writeheader()

            # 一行ずつループ処理
            for row in reader:
                # 抽出したいデータだけを含む新しい辞書を作成
                extracted_row = {header: row[header] for header in headers_to_keep}
                # 新しい辞書を一行書き込む
                writer.writerow(extracted_row)

        print(f"✅ 処理が完了しました。'{output_filename}' に結果を保存しました。")

    except FileNotFoundError:
        print(f"エラー: 入力ファイル '{input_filename}' が見つかりません。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")


# --- ここから実行部分 ---
if __name__ == '__main__':
    # ▼▼▼ 設定を自分の環境に合わせて変更してください ▼▼▼

    # 1. 元となるCSVファイル名
    input_csv_file = 'csv_column_extractor/source_data.csv'

    # 2. 保存する新しいCSVファイル名
    output_csv_file = 'csv_column_extractor/extracted_data.csv'

    # 3. 抽出したいヘッダー（列名）のリスト
    target_headers = ['氏名', '年齢', '部署']

    # ▲▲▲ 設定はここまで ▲▲▲


    # --- サンプルの入力CSVファイルを作成 ---
    # この部分は動作確認用なので、実際には不要です。
    # 'source_data.csv'というファイルがすでにある場合は、この部分は実行されません。
    try:
        with open(input_csv_file, 'x', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', '氏名', '年齢', '部署', '入社日'])
            writer.writerow(['001', '山田 太郎', '32', '営業部', '2015-04-01'])
            writer.writerow(['002', '鈴木 花子', '28', '開発部', '2018-04-01'])
            writer.writerow(['003', '佐藤 次郎', '45', '人事部', '2005-10-01'])
        print(f"📝 サンプルファイル '{input_csv_file}' を作成しました。")
    except FileExistsError:
        pass # ファイルが既に存在する場合は何もしない
    # --- サンプル作成ここまで ---


    # 関数を実行
    extract_specific_columns(input_csv_file, output_csv_file, target_headers)