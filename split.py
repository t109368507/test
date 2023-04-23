import random
import sys

from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
#data_utils.download_data_gdown("./")
#data_utils.download_data_url("./") # iis-ckip
#data_utils.download_data_gdown("./") # gdrive-ckip

'''
Usage:
python split.py src_fpath tgt_fpath new_data_dir
'''

def split(src_fpath, tgt_fpath, nsrc='zh', ntgt='tl', ratio=(0.9, 0.05, 0.05), new_data_dir=''):
  src_fp = open(src_fpath, encoding='utf-8')
  tgt_fp = open(tgt_fpath, encoding='utf-8')

  src_train, src_test, src_val = open(new_data_dir + 'train.' + nsrc, 'w', encoding='utf-8'), \
    open(new_data_dir + 'test.' + nsrc, 'w', encoding='utf-8'), open(new_data_dir + 'valid.' + nsrc, 'w', encoding='utf-8')
  tgt_train, tgt_test, tgt_val = open(new_data_dir + 'train.' + ntgt, 'w', encoding='utf-8'), \
    open(new_data_dir + 'test.' + ntgt, 'w', encoding='utf-8'), open(new_data_dir + 'valid.' + ntgt, 'w', encoding='utf-8')

  src, tgt = src_fp.readlines(), tgt_fp.readlines()
  #print(src)
  #print(len(src))
  #p = input('')
  #print(tgt)
  #print(len(tgt))
  #p = input('')
  colline=1
  ws = WS("./data")
  for s, t in zip(src, tgt):
      rand = random.random()
      if 0 < rand <= ratio[0]:
        #if len(t) < 6:
        #    p=input("")
        #    continue
        #if len(s) < 6:
        #    p=input("")
        #    continue
        _ws = ws([t])
        #print(_ws)
        t=" ".join(_ws[0])
        print(len(s),s.lower())
        print(len(t),t)
        if len(t) < 6:
            p=input("")
            continue
        if len(s) < 6:
            p=input("")
            continue
        #p=input("")
        src_train.write(s.lower())
        tgt_train.write(t)
        print("---- train"+"-"*100)
      elif ratio[0] < rand <= ratio[0] + ratio[1]:
        if len(t) == 1 or len(t) < 6:
            continue
        if len(s) == 1 or len(s) < 6:
            continue
        _ws = ws([t])
        #print(_ws)
        t=" ".join(_ws[0])
        print(len(s),s.lower())
        print(len(t),t)
        print("---- test"+"-"*100)
        src_test.write(s.lower())
        tgt_test.write(t)
      else:
        if len(t) == 1 or len(t) < 6:
            continue
        if len(s) == 1 or len(s) < 6:
            continue
        _ws = ws([t])
        #print(_ws)
        t=" ".join(_ws[0])
        print(len(s),s.lower())
        print(len(t),t)
        print("---- val"+"-"*100)
        src_val.write(s.lower())
        tgt_val.write(t)

  src_fp.close()
  tgt_fp.close()
  src_train.close()
  src_test.close()
  src_val.close()
  tgt_train.close()
  tgt_test.close()
  tgt_val.close()

if __name__ == '__main__':
    split(src_fpath=sys.argv[1], tgt_fpath=sys.argv[2], nsrc='tl', ntgt='zh', ratio=(0.8, 0.1, 0.1), new_data_dir=sys.argv[3])

