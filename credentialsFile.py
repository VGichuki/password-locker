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

    @classmethod
    def display_credentials(cls):
        """
        displays the credentials of a user according to the init
        """
        return cls.credentials_list

    def delete_credential(self):
        """
        deletes the credentials a user does not need
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls,site_username):
        for credential in cls.credentials_list:
            if credential.site_username == site_username:
                return credential



    


