import fileinput

class parser():

    def __init__ (self,filename):
        self._filename = filename
        self._parsedict = {}
        
    def parse(self):
        #with open (self._filename) as f:
        #    lines = f.xreadlines()
        #    for line in lines:
        
        for line in fileinput.input(self._filename):
                #print(line)
                #raw_input("?")
            line = line.rstrip()
            name, amount = line.split(",")
            #print(name)
                #print(name)
                #print(amount)
                #raw_input("?")
            if name in self._parsedict.keys():
                self._parsedict[name].append(amount)
                    #print(self._parsedict)
                    #raw_input("?")
                   
            else:
                self._parsedict[name] = []
                self._parsedict[name].append(amount)
                    #print(self._parsedict)
                    #raw_input("?")
                    
        return self._parsedict
                
                
        