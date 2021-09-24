import os
import matplotlib.pyplot as plt
import numpy as np
import serpentTools as st

exceptions = ['runAll.py', 'readAll1D.py', 'keff.png']

cwdStart = os.getcwd()
folders1 = os.listdir(cwdStart)
folders1 = [x for x in folders1 if x not in exceptions]
v1Order = np.array([])

os.chdir('{}/{}'.format(cwdStart, folders1[0]))
cwd = os.getcwd()
folders2 = os.listdir(cwd)
folders2 = [x for x in folders2 if x not in exceptions]

f1Len = len(folders1)
f2Len = len(folders2)

os.chdir(cwdStart)

keffArray = np.zeros((f1Len, f2Len))
kErrorArray = np.zeros((f1Len, f2Len))
conversionArray = np.zeros((f1Len, f2Len))

for i in range(0, len(folders1)):
    f1 = folders1[i]
    v1Order = np.append(v1Order, f1)
    pDone = '{} {} %'.format(f1, np.round(i / f1Len * 100, 1))
    print("\u0332".join(pDone))

    dest1 = '{}/{}'.format(cwdStart, f1)
    os.chdir(dest1)

    cwd = os.getcwd()
    folders2 = os.listdir(cwd)
    folders2 = [x for x in folders2 if x not in exceptions]
    v2Order = np.array([])

    for j in range(0, len(folders2)):
        f2 = folders2[j]
        v2Order = np.append(v2Order, f2)
        print(' ➞ {}'.format(f2))

        dest2 = '{}/{}'.format(dest1, f2)
        os.chdir(dest2)

        cwd = os.getcwd()
        files = os.listdir(cwd)

        for file in files:
            if file.endswith('.m'):
                res = st.read(file)
                keffArray[i, j] = res.resdata['anaKeff'][0]
                kErrorArray[i, j] = res.resdata['anaKeff'][1]
                conversionArray[i, j] = res.resdata['conversionRatio'][0]
os.chdir(cwdStart)
print(v1Order)
print(keffArray.flatten())
v1Order = np.linspace(140,160,21)
keffArray = keffArray.flatten()
kErrorArray = kErrorArray.flatten()
plt.plot(v1Order,keffArray)
plt.fill_between(v1Order,keffArray-kErrorArray,keffArray+kErrorArray,color='gray', alpha=0.2)
plt.savefig('keff.png')
plt.show()




