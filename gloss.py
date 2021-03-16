#create glossary list


class dxkbGlossary:

    def __init__(self, path): 
        self.path = path
        self.terms = []
    def saveGloss(self):
        with open("output.txt", "w+") as txt_file:
            for line in self.terms:
                txt_file.write(" ".join(line) + "\n") 

    def createGloss(self):
        from os import listdir
        from os.path import isfile, join, splitext

        for f in listdir(self.path):
            if not(isfile(join(self.path, f))):
                continue
            if not(splitext(f)[1] == '.md'):
                continue
            filename = join(path,f)
            with open(filename,"r") as f:
                slug = f.readlines()[1][6:-1].replace("'","")
                self.terms.append((filename,slug))
             

#        filelist = [f for f in listdir(self.path) if splitext(f)[1] == '.md' if isfile(join(self.path, f))]
#        for filename in filelist:
#            f = join(path, filename)
#            with open(f,"r") as f:
#                slug = f.readlines()[1][6:-1].replace("'","")
#                self.terms.append((filename,slug))
                
        print("Done!")
        print(self.terms)
       
        



path = "test mds"
gloss = dxkbGlossary(path)
gloss.createGloss()
gloss.saveGloss()

