import os, glob
import datetime

jupyter_fnames = glob.glob('*.ipynb')
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
yesterday = yesterday.strftime("%Y-%m-%d")
befyest = today- datetime.timedelta(days=2)
befyest = befyest.strftime("%Y-%m-%d")
jupyter_new_fnames = [fname.replace('_','-') for fname in jupyter_fnames]
jupyter_new_fnames = [fname.replace("ANO-MES-DIA", yesterday) for fname in jupyter_new_fnames]

for old_fname, new_fname in zip(jupyter_fnames, jupyter_new_fnames):
    os.system(f'mv {old_fname} {new_fname}')
    os.system(f'git add {new_fname}')

# delete previous version
os.system(f'git rm -f {befyest}-projecao-*')

# Commit changes
os.system(f'git commit -m "update projection"')


