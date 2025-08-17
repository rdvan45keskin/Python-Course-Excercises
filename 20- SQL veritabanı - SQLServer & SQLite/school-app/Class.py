class Class:
    def __init__(self, id,name,teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        if len(name) > 30:
            raise Exception("name için maximum 25 karakter girmelisiniz.")
        self.name = name
        self.teacherid = teacherid

    @staticmethod
    def CreateClass(obj):
        liste = []
        for i in obj:
            liste.append(Class(i[0],i[1],i[2]))
        return liste