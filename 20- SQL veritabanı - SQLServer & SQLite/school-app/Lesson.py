class Lesson:
    def __init__(self, id,name):
        if id is None:
            self.id = 0
        else:
            self.id = id
        if len(name) > 30:
            raise Exception("name için maximum 25 karakter girmelisiniz.")
        self.name = name
