from tkinter import ttk

def bk():
    tree = ttk.Treeview(columns=("frequency",
                                 "mode",
                                 "description",
                                 "lockout"),
                        displaycolumns=("frequency",
                                        "mode",
                                        "description"),
                        show="headings")
    value =  [u'5,955,000', u'AM', u'found on 18.34 jan 08 2015', u'O']
    bk_list = []
    bk_list.append(value)
    bk = Bookmarks(tree, io=IO())
    bk._insert_bookmarks(bk_list)

    return bk 
bk()
            # fixme 
