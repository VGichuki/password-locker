import pyperclip

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

    


