import os, glob

jupyter_fnames = glob.glob('*.ipynb')

jupyter_new_fnames = [fname.replace('_','-') for fname in jupyter_fnames]

for old_fname, new_fname in zip(jupyter_fnames, jupyter_new_fnames):
    os.system(f'mv {old_fname} {new_fname}')