class User_Validator(object):
    '''
    Validator pentru clasa user
    Trebuie sa verific:
    - lungime nr tel sa fie 10
    - tipul sa fie admin sau client
    '''


    @staticmethod
    def validate(user):
        error_msg = ""
        if(len(user.get_nr_telefon())!=10):
            error_msg += "Nr. tel. invalid.\n"
        if (user.get_tip()!="client" and user.get_tip()!="admin"):
            error_msg += "Tip user invalid.\n"
        if len(error_msg) > 0: #daca am gasit ceva eroare, adica lungimea mesajului de eroare e >0
            raise ValueError(error_msg) #arunc exceptie - ii zic BĂI, E BAI MARE!! AI INTRODUS PROSTII!