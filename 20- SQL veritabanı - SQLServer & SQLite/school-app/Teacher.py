class Teacher:
    def __init__(self, id,branch,name,surname,birthdate,gender,classid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        if len(branch) > 45:
            raise Exception("branch için maximum 45 karakter girmelisiniz.")
        self.branch = branch
        if len(name) > 30:
            raise Exception("name için maximum 25 karakter girmelisiniz.")
        self.name = name
        if len(surname) > 30:
            raise Exception("name için maximum 25 karakter girmelisiniz.")
        self.surname = surname
        self.birthdate = birthdate


        self.gender = gender.lower()
        if (gender=="e" or gender=="k"):
            self.gender = gender
        else:
            raise Exception("Gender değeri E-K olmalıdır.")