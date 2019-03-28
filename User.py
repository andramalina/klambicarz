class User:
    def __init__(self, id_user, username, nume, nr_telefon, tip, password):
        self.id_user=id_user
        self.username=username
        self.nume=nume
        self.nr_telefon=nr_telefon
        self.tip=tip
        self.password=password

    def set_id_user(self, id_user):
        self.id_user=id_user

    def set_username(self, username):
        self.username=username

    def set_nume(self, nume):
        self.nume=nume

    def set_nr_telefon(self, nr_telefon):
        self.nr_telefon=nr_telefon

    def set_tip(self,tip):
        self.tip=tip

    def set_password(self, password):
        self.password=password

    def get_id_user(self):
        return self.id_user

    def get_username(self):
        return self.username

    def get_nume(self):
        return self.nume

    def get_nr_telefon(self):
        return self.nr_telefon

    def get_tip(self):
        return self.tip

    def get_password(self):
        return self.password