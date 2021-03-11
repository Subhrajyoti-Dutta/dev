import os
def files(src):
    fl = open(r"C:\dev\python\Cython\setup.py","w")
    fl.write(f"from distutils.core import setup\nfrom Cython.Build import cythonize\n\nsetup(ext_modules=cythonize('{src}'))")
    fl.close()
    
    os.system(r"cd C:\dev\python\Cython & python setup.py build_ext --inplace")
    #os.system('cls')
    print(f"Finished building {src}")