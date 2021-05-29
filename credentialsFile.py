import pyperclip
import string
import random

class Credentials:
    """
    class that generates new instances of credentials
    """

    credentials_list=[]

    def __init__(self,site,site_username,site_password):
        """
        initialises the attributes of credentials
        """
        self.site = site
        self.site_username = site_username
        self.site_password = site_password

    def save_credential(self):
        """
        save credentials of a user in the account
        """
        Credentials.credentials_list.append(self)

    @classmethod
    def generate_password(cls):
        """
        passwords can be generated randomly for the user
        """
        Random_password = string.ascii_letters
        res=''.join(random.choice(Random_password) for i in range(6))
        return res


    


