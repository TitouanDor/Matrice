class Matrice:
    def __init__(self, mat) -> None:
        if len(mat) == 0: raise ValueError("MatriceObject mustn't be empty")
        teste = len(mat[0])
        for i in mat:
            if len(i) != teste: raise ValueError("Column of the matrice haven't the same number")
            for j in i: 
                if not((type(j) == float) or (type(j) == int)): raise TypeError(f"Values must be interger or float not {type(j)}")
        
        if len(mat[0]) == 0: raise ValueError("MatriceObject mustn't be empty")

        self.mat = mat
        self.line = len(mat)
        self.column = len(mat[0])
        pass

    def __str__(self) -> str:
        text = "\n"
        for i in self.mat: text = text + str(i) + "\n"
        return text
    
    def multiplyBy(self, x):
        """Méthode renvoyant une matrice multiplier par un nombre réels"""
        if not((type(x) == float) or (type(x) == int)): raise TypeError(f"X must be interger or float not {type(x)}")
        matriceFinal = []; sousListe = []
        for i in self.mat:
            for j in i: sousListe.append(j*x)

            matriceFinal.append(sousListe)
            sousListe = []
        return Matrice(matriceFinal)
    
    def divideBy(self, x):
        """Méthode renvoyant une matrice diviser par un nombre réels"""
        if not((type(x) == float) or (type(x) == int)): raise TypeError(f"X must be interger or float not {type(x)}")
        matriceFinal = []; sousListe = []
        for i in self.mat:
            for j in i: sousListe.append(j/x)

            matriceFinal.append(sousListe)
            sousListe = []
        return Matrice(matriceFinal)

    def addMatrice(self, B):
        """Méthode renvoyant l'addition de deux matrices"""
        if not(((self.line == B.line) and (self.column == B.column))): raise IndexError("Matrice must have the same lenght")
        matriceFinal = []; sousListe = []
        for i in range(self.line):
            for j in range(self.column): sousListe.append(self.mat[i][j] + B.mat[i][j])

            matriceFinal.append(sousListe)
            sousListe = []
        return Matrice(matriceFinal)
    
    def subMatrice(self, B):
        """Méthode renvoyant la différence de 2 matrices"""
        if not(((self.line == B.line) and (self.column == B.column))): raise IndexError("Matrice must have the same lenght")
        matriceFinal = []; sousListe = []
        for i in range(self.line):
            for j in range(self.column): sousListe.append(self.mat[i][j] - B.mat[i][j])

            matriceFinal.append(sousListe)
            sousListe = []
        return Matrice(matriceFinal)
    
    def multiplyMatrice(self, B):
        """Méthode retournant le produit matricielle"""
        if not(self.column == B.line): raise IndexError("Matrice must have same line than the number of column of the otehr matrice")

        matri = [[0 for _ in range(B.column)] for _ in range(self.line)]; somme = 0
        for i in range(self.column): 
            for j in range(B.column): 
                for k in range(B.line): somme += self.mat[i][k]*B.mat[k][j]
                matri[i][j] = somme; somme = 0

        return Matrice(matri)
    
    def power(self, x):
        """Méthode retournant la matrice exposant X"""
        if not(type(x) == int): raise TypeError(f"X must be interger not {type(x)}")
        base = self
        for _ in range(1, x): self = self.multiplyMatrice(base)
        return self
