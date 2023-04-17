import random
import sys

'''
Usage:
python split.py src_fpath tgt_fpath new_data_dir
'''

def split(src_fpath, tgt_fpath, nsrc='tl', ntgt='zh', ratio=(0.9, 0.05, 0.05), new_data_dir=''):
  src_fp = open(src_fpath, encoding='utf-8')
  tgt_fp = open(tgt_fpath, encoding='utf-8')

  src_train, src_test, src_val = open(new_data_dir + 'train.' + nsrc, 'w', encoding='utf-8'), \
    open(new_data_dir + 'test.' + nsrc, 'w', encoding='utf-8'), open(new_data_dir + 'valid.' + nsrc, 'w', encoding='utf-8')
  tgt_train, tgt_test, tgt_val = open(new_data_dir + 'train.' + ntgt, 'w', encoding='utf-8'), \
    open(new_data_dir + 'test.' + ntgt, 'w', encoding='utf-8'), open(new_data_dir + 'valid.' + ntgt, 'w', encoding='utf-8')
  colline=1
  src, tgt = src_fp.readlines(), tgt_fp.readlines()
  
  print(src)
  print(len(src))
  p=input("")
  print(tgt)
  print(len(tgt))
  p=input("")
  
  for s, t in zip(src, tgt):
      rand = random.random()
      if 0 < rand <= ratio[0]:
        print(colline)
        colline=colline+1
        print(len(t),t)
        if len(t) == 1:
            p=input("")
        src_train.write(s)
        print(colline)
        colline=colline+1
        print(len(s),s)
        if len(s) == 1:
            p=input("")
        tgt_train.write(t)
        print("---- train"+"-"*100)
      elif ratio[0] < rand <= ratio[0] + ratio[1]:
        src_test.write(s)
        tgt_test.write(t)
      else:
        src_val.write(s)
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
    split(src_fpath=sys.argv[1], tgt_fpath=sys.argv[2], nsrc='zh', ntgt='tl', ratio=(1.0, 0.0, 0.0), new_data_dir=sys.argv[3])
