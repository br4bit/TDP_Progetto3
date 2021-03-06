import TdP_collections.hash_table.sorted_table_map
import hashlib
from TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from pandas.tests.io.parser import index_col
from TdP_collections.hash_table.chain_hash_map import ChainHashMap
from TdP_collections.hash_table.sorted_table_map import SortedTableMap
from builtins import print
import pandas as pd
import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets

qtCreatorFile = "gui_camp.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

def fail_func(w):
    #initializing the array auxiliar with 0 in each cell
    auxiliar = [0] * len(w)
    # for index 0, it will always be 0, starting from 1
    i = 1
    #m can also be viewed as index of first mismatch
    m = 0
    while i < len(w):
    # prefix = suffix till m-1
        if w[i] == w[m]:
            m += 1
            auxiliar[i] = m
            i += 1
            # when there is a mismatch,we will check the index of previous possible prefix.
        elif w[i] != w[m] and m != 0:
        # Note that we do not increment i here.
            m = auxiliar[m-1]
        else:
                # m = 0, we move to the next letter, 
                # there was no any prefix found which is equal to the suffix for index i
            auxiliar[i] = 0
            i += 1
    return auxiliar

def count_kmp(T,P):
    count = 0
    array_aux = fail_func(P)
    #counter for word P
    i = 0
    #counter for word T
    j = 0
    while j < len(T):
        #we need handle 2 conditions when there is a mismatch
        if P[i] != T[j]:
            #1s condition
            if i == 0:
                #start again from next character in the text T
                j += 1
            else:
                # array_aux[i-1] will tell from where to compare next
                # and no need to match for P[0..array_aux[i-1] - 1],
                # they will match anyway.
                i = array_aux[i-1]
        else:
            i += 1
            j += 1
            # we found the pattern
            if i == len(P):
                #count + 1
                count+=1
                i = array_aux[i-1]
    return count

def load_excel():
    camp=ProbeHashMap()
    key="E0"
    key1="E1"
    #df=pd.DataFrame()
    #df = pd.read_excel('all-euro-data-2016-2017.xlsx', sheet_name='E0', usecols=range(10))
    #camp.setdefault(df.at[1,'Div'])
    #df=df.set_index("Div")
    #print(df.head())
    #camp[key]=[df['HomeTeam'],df['Date']]
    camp[key]=['ciao',2,3,4,5]
    camp[key].append(6)
    camp[key1]=[2]
    camp[key1].append(3)
    print(camp.get(key)[0])
    print(len(camp))
    for k in camp.keys():
        print("Chiave: ",k," valore: ",camp[k])
    #print("Numero colonne: ",df.shape[0])
    #print(df.at[1,'Div'])
    #id = int(hashlib.md5('ciao'.encode('utf-8')).hexdigest(), 16)
    #id2 = int(hashlib.md5('ciao'.encode('utf-8')).hexdigest(), 16)
    #print(id)
    #print(id2)
    

def main():
    pattern = "acabacacd"
    text = "acfacabacabacacdkacabacacdacabacacd"
    print("Text: ",text)
    print("Pattern: ",pattern)
    print("Numero di occorrenze KMP algorithm: ",count_kmp(text,pattern))
    print()
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    #main()
    #load_excel()
    