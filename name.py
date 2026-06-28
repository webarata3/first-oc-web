import random
import string

# 英小文字(a-z)と数字(0-9)を組み合わせた文字列を作成
chars = string.ascii_lowercase + string.digits

# ランダムに8文字選んで結合する
random_str = ''.join(random.choices(chars, k=8))

print(random_str)
