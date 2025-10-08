import pandas as pd
import configparser
import sys

def load_config(filename='csv_column_extractor/config.ini'):
    """設定ファイル(config.ini)を読み込む"""
    config = configparser.ConfigParser()
    
    # encoding='utf-8' を指定して日本語の文字化けを防ぐ
    if not config.read(filename, encoding='utf-8'):
        print(f"エラー: 設定ファイル '{filename}' が見つからないか、空です。")
        sys.exit(1) # プログラムを終了
        
    settings = config['SETTINGS']
    
    # カンマ区切りの文字列をリストに変換
    # 各要素の前後の空白を削除
    headers_str = settings.get('target_headers', '')
    headers_list = [header.strip() for header in headers_str.split(',') if header.strip()]
    
    return {
        'input': settings.get('input_csv_file', ''),
        'output': settings.get('output_csv_file', ''),
        'headers': headers_list
    }

def extract_columns_with_pandas(input_filename, output_filename, headers_to_keep):
    """
    pandasを使用して、CSVファイルから指定された列を抽出します。
    """
    if not input_filename or not output_filename or not headers_to_keep:
        print("エラー: 設定ファイルの値が不足しています（input_csv_file, output_csv_file, target_headers）。")
        return

    try:
        df = pd.read_csv(input_filename, encoding='utf-8')

        existing_headers = [h for h in headers_to_keep if h in df.columns]
        missing = set(headers_to_keep) - set(existing_headers)
        if missing:
            print(f"⚠️ 警告: 次のヘッダーはCSVファイルに存在しませんでした: {', '.join(missing)}")
        
        if not existing_headers:
            print("エラー: 抽出対象のヘッダーがCSVファイルに一つも存在しません。処理を中断します。")
            return
            
        df_extracted = df[existing_headers]

        # ▼▼▼ ここを変更しました ▼▼▼
        # Excelで日本語が文字化けしないように、BOM付きUTF-8(utf-8-sig)で出力
        df_extracted.to_csv(output_filename, index=False, encoding='utf-8-sig')
        # ▲▲▲ 変更ここまで ▲▲▲

        print(f"✅ 処理が完了しました。'{output_filename}' に結果を保存しました。")

    except FileNotFoundError:
        print(f"エラー: 入力ファイル '{input_filename}' が見つかりません。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")


# --- ここから実行部分 ---
if __name__ == '__main__':
    # 設定ファイルから設定を読み込む
    config = load_config()
    
    # 読み込んだ設定を使って関数を実行
    extract_columns_with_pandas(
        input_filename=config['input'],
        output_filename=config['output'],
        headers_to_keep=config['headers']
    )