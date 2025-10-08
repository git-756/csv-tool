import pandas as pd

def extract_columns_with_pandas(input_filename, output_filename, headers_to_keep):
    """
    pandasを使用して、CSVファイルから指定された列を抽出します。

    Args:
        input_filename (str): 入力CSVファイルのパス。
        output_filename (str): 出力CSVファイルのパス。
        headers_to_keep (list): 抽出したいヘッダー名のリスト。
    """
    try:
        # CSVファイルをDataFrameとして読み込む
        df = pd.read_csv(input_filename, encoding='utf-8')

        # 指定された列のみを抽出
        # headers_to_keepに存在しない列が指定されるとエラーになるため、存在チェックを挟む
        existing_headers = [h for h in headers_to_keep if h in df.columns]
        if len(existing_headers) != len(headers_to_keep):
            missing = set(headers_to_keep) - set(existing_headers)
            print(f"警告: 次のヘッダーはファイルに存在しませんでした: {', '.join(missing)}")
        
        if not existing_headers:
            print("エラー: 抽出対象のヘッダーがファイルに一つも存在しません。")
            return
            
        df_extracted = df[existing_headers]

        # 新しいCSVファイルとして保存（index=Falseで余計な行番号を消す）
        df_extracted.to_csv(output_filename, index=False, encoding='utf-8')

        print(f"✅ 処理が完了しました。'{output_filename}' に結果を保存しました。")

    except FileNotFoundError:
        print(f"エラー: 入力ファイル '{input_filename}' が見つかりません。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")


# --- ここから実行部分 ---
if __name__ == '__main__':
    # ▼▼▼ 設定を自分の環境に合わせて変更してください ▼▼▼
    input_csv_file = 'csv_column_extractor/source_data.csv'
    output_csv_file = 'csv_column_extractor/extracted_data_pandas.csv'
    target_headers = ['氏名', '年齢', '部署']
    # ▲▲▲ 設定はここまで ▲▲▲
    
    # 上のコードでサンプルファイルが作成されているはずなので、ここでは実行のみ
    extract_columns_with_pandas(input_csv_file, output_csv_file, target_headers)