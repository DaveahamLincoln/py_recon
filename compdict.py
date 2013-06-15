class compdict():
    def __init__ (self, a, b):
        self._adict = a
        self._bdict = b
        self._cdict = {}
        
    def compare(self):
        for key in self._adict.keys():
            if key in self._bdict.keys():
                alist = self._adict[key]
                blist = self._bdict[key]
                for item in alist:
                    if item in blist:
                        pass
                    else:
                        if key in self._cdict.keys():
                            self._cdict[key].append(item)
                            
                        else:
                            self._cdict[key] = []
                            self._cdict[key].append(item)
        #print self._cdict
        items = []
        for key in self._cdict.keys():
            #print(key)
            items.append(key)
        items.sort()
        out = open('output.txt','w+')
        for i in items:
           out.write("%s, %s\n" % (i, self._cdict[i]))
                
        
                        