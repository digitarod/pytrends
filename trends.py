from pytrends.request import TrendReq
import datetime
import json

# Googleトレンドに接続
pytrends = TrendReq(hl='ja-JP', tz=540)
trending_searches_df = pytrends.trending_searches(pn='japan')

# 現在の日付を取得
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# トレンドデータをリスト化
trends_list = [row[0] for _, row in trending_searches_df.iterrows()]

# JSONデータを作成
data = {
    "updated_at": today,
    "trending_words": trends_list
}

# JSONをテキストファイルに保存
with open("trends.txt", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Googleトレンドの急上昇ワードを trends.txt に保存しました。")
