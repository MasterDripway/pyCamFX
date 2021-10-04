class genecalc:
    def __init__(self, gene1 : str, gene2 : str):
        self.gene1, self.gene2 = gene1, gene2
        self.charset = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        self.ng1 = list(self.gene1)
        self.ng2 = list(self.gene2)
        self.ng1.sort(key=lambda x : self.charset.index(x))
        self.ng2.sort(key=lambda x : self.charset.index(x))
        self.genes = [self.ng1, self.ng2]



    def createChart(self):
        self.rows = []
        self.new = []
        print(self.genes[0])
        for i in range(0, len(self.genes[0]), 2):
            self.gene = self.genes[0][i:i+2]
            self.new.append("".join(self.gene))
        print(self.new)





a = genecalc("ABab", "AABb")
a.createChart()
[print('\n', i) for i in a.rows]