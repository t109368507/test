import os
import sys
import re

DIR_PATH="C:\\Users\\yange\\Desktop\\語音辨識\\機器翻譯\\語料庫\\全民台語聖經網站"

index=0
line = ''
line_zh = ''
line_tl = ''
line_en = ''
line_all = ''

dirs = os.listdir( DIR_PATH )
tl_zh = 0
zh_en = 1

# 刪除上次預處理後的檔案
outfile_zh = "bible.b.raw.zh"
outfile_tl = "bible.raw.tl"
outfile_en = "bible.b.raw.en"
outfile_all = "bible.b.raw.all"

is_all_exist = False
is_zh_exist = False

line_number=0

characters = "”－\"'[]()“「」（）：。,，.？！『』﹙﹚‘、:；;…"  # 過濾半形全形符>號
split_characters = "。,，."

# if os.path.isfile(outfile_zh):
#     os.remove(outfile_zh)
# if os.path.isfile( outfile_tl):
#     os.remove(outfile_tl)
# if os.path.isfile(outfile_en):
#     os.remove(outfile_en)
if os.path.isfile(outfile_all):
    print(outfile_all,"exist!")
    is_all_exist = True
else:
    # os.remove(outfile_all)
    print(outfile_all,"is not exist!")
    is_all_exist = False

# ?出所有文件和文件?.
# if is_all_exist == False:
for _dirs in dirs:
    print ("="*50,_dirs,"="*50)
    _files = os.listdir(DIR_PATH+"\\"+_dirs)
    # print(_files)

    if tl_zh:
        for i in range(len(_files)):
            if "tl-zh" in _files[i]:
                findex = i
                # print(_files[findex])
    if zh_en:
        for i in range(len(_files)):
            if "zh-en" in _files[i]:
                findex = i
                # print(_files[findex])

    with open(DIR_PATH +"\\"+ _dirs + "\\" + _files[findex], "r", encoding='utf-8') as f:
        for _line in f.readlines():
            for x in range(len(characters)):
                _line = _line.replace(characters[x], " ")

            _line = _line.strip()
            _line = re.findall(".{1}", _line)

            if len(_line) < 2:
                p=input("")

            for c in _line:
                if index<5:
                    if c >= '0' and c <= '9' or c == ':':
                        _line[index] = ''
                    index=index+1
            index=0
            # print(_line)
            line_all = line_all + "".join(_line) + '\n'

            # print(line)
            # if line_number==0:
            if line_number == 1:
                s1 = []
                count = 0
                for i in _line:
                    s1.append(i)

                    # if i == ',':
                    #           count += 1
                    #                     if count == len(_line):
                    #                         continue s1.append('\n')

                _line = s1
                # line_tl = line_tl + "".join(_line) + '\t' + '[' + _files[0] + ']' +'\n'
                if tl_zh:
                    # line_tl = line_tl + "".join(_line) + '\t' + '[' + _files[findex] + ']' + '\n'
                    line_tl = line_tl + "".join(_line) +'\n'
                    # print(line_tl)
                if zh_en:
                    # line_en = line_en + "".join(_line) + '\t' + '[' + _files[findex] + ']' + '\n'
                    line_en = line_en + "".join(_line) + '\n'
                    # print(line_en)

                # line_number=1
                line_number = 0
            # elif line_number==1:
            elif line_number == 0:
                s1 = []
                count = 0
                for i in _line:
                    s1.append(i)
                    count += 1
                    if count == len(_line):
                        continue
                    s1.append('')

                _line = s1

                # line_zh = line_zh + "".join(_line) + '\t' + '[' + _files[0] + ']' +'\n'
                line_zh = line_zh + "".join(_line) +'\n'
                # line_number=0
                line_number = 1

        line_number=0


if tl_zh:
    with open(outfile_tl, 'w', encoding='utf-8') as file:
        file.write(line_tl)
if zh_en:
    with open(outfile_en, 'w', encoding='utf-8') as file:
        file.write(line_en)
with open(outfile_zh, 'w', encoding='utf-8') as file:
    file.write(line_zh)
with open(outfile_all, 'w', encoding='utf-8') as file:
    file.write(line_all)



print("Done!------------------------------------")