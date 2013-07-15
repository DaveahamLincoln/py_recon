import fileinput

class parser():

    def __init__ (self,filename):
        self._filename = filename
        self._parsedict = {}
    
    def parse(self):
        for line in fileinput.input(self._filename):
            line = line.rstrip()
            quote = False
            rebuilder = []
            for i in range(0,len(line)):
                if line[i]== '\"':
                    quote = not quote
                    print quote
                    pass
                if line[i]==",":
                    if quote == True:
                        rebuilder.append("")
                    else:
                        rebuilder.append(line[i])
                else:
                    rebuilder.append(line[i])
            line = ''.join(rebuilder)
            line = line.replace('\"', "")
            #print(line)
            name, amount = line.split(",")
            
            if name in self._parsedict.keys():
                self._parsedict[name].append(amount)                   
            else:
                self._parsedict[name] = []
                self._parsedict[name].append(amount)
                
        return self._parsedict