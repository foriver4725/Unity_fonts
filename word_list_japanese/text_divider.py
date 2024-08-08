######################################################################################################################################################
# 入力ファイルの相対パス
input_file_path = "full.txt"

# 出力ファイルの相対パスのリスト
output_file_paths = [f"{i}.txt" for i in range(1, 5)]
######################################################################################################################################################

# 読み込み
with open(input_file_path, "r", encoding="utf-8") as f:
    input_char_list = list(f.read())

# 分割
divide_num = len(output_file_paths)
divided_num = len(input_char_list) // divide_num
output_string_list = ["".join(input_char_list[i * divided_num : (i + 1) * divided_num]) for i in range(divide_num)]
output_string_list[-1] += "".join(input_char_list[divide_num * divided_num :])

# 書き出し
for output_index, output_string in enumerate(output_string_list):
    with open(output_file_paths[output_index], "w", encoding = "utf-8") as f:
        f.write(output_string)

# 処理の成否判定
input_string_len = len(input_char_list)
output_string_len = sum(map(len, output_string_list))
print("Succeed") if input_string_len == output_string_len else print("Fail")