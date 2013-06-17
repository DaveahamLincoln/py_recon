class compdict():
    def __init__ (self, a, b, outfile):
        self._adict = a
        self._bdict = b
        self._cdict = {}
        self._outfile = outfile
        
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
        items = []
        for key in self._cdict.keys():
            items.append(key)
        items.sort()
        
        #This would ordinarily be handled by a separate save method, but there's
        #no real reason to do it here since we're not doing anything with the data
        #other than comparing it for immediate output to a log.  If pyrecon is
        #expanded to include further functionality, compdict.compare should
        #be changed to return an ordered list of the format
        #[(items[i]),(self._cdict[i])...(items[i+n]),(self._cdict[i+n])]
        #and a write method/reportwriter class should be created to handle writing 
        #different kinds of reports.  compdict should also be amended to not require
        #an outfile parameter.
        
        out = open(self._outfile,'w+')
        for i in items:
           out.write("%s, %s\n" % (i, self._cdict[i]))