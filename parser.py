import fileinput

class parser():

    def __init__ (self,filename):
        self._filename = filename
        self._parsedict = {}
        
    def parse(self):
        
        for line in fileinput.input(self._filename):
            line = line.rstrip()
            quoteflag = 0
            if line.startswith('"'):
                quoteflag = 1
                rebuilder = []
                for i in range(1,len(line)):
                    if quoteflag == 1:
                        if line[i] == '"':
                            quoteflag = 0
                        elif line[i] == ",":
                            pass
                        else:
                            rebuilder.append(line[i])
                    
                    else:
                        rebuilder.append(line[i])
                        
                line = ''.join(rebuilder)
            
            name, amount = line.split(",")
            if name in self._parsedict.keys():
                self._parsedict[name].append(amount)                   
            else:
                self._parsedict[name] = []
                self._parsedict[name].append(amount)
                
        return self._parsedict
                
                
        