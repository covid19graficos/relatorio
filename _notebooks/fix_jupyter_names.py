import os, glob
import datetime

jupyter_fnames = glob.glob('*.ipynb')
today = datetime.datetime.today().strftime("%Y-%m-%d")

jupyter_new_fnames = [fname.replace('_','-') for fname in jupyter_fnames]
jupyter_new_fnames = [fname.replace("ANO-MES-DIA",today) for fname in jupyter_new_fnames]

for old_fname, new_fname in zip(jupyter_fnames, jupyter_new_fnames):
    os.system(f'mv {old_fname} {new_fname}')
