import json
import datetime
from twikit.trends import get_trends

# 日本のWOEID (Yahoo!のWhere On Earth ID) = 23424856
woeid_japan = 23424856

# Twitterの急上昇トレンドを取得
trends = get_trends(woeid=woeid_japan)

# 現在の日時を取得
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# JSON形式で保存
data = {
    "updated_at": now,
    "trending_words": [trend["name"] for trend in trends]
}

# ファイルに保存
with open("trends.txt", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Twitterのトレンドを trends.txt に保存しました。")
