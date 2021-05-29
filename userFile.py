class UserData:
    """
    Class that contains data about the user such as username and login details
    """
    users=[] #empty users data

    def __init__(self,firstName,lastName,password):
        """
        __init__ initialises the attributes of password locker
        """
        self.firstName = firstName
        self.lastName = lastName
        self.password = password

    def save_account(self):
        """
        saves account objects into users
        """
        UserData.users.append(self)

    def delete_account(self):
        """
        deletes saved accounts from the users
        """
        UserData.users.remove(self)

    @classmethod
    def find_account(cls,username):
        """
        method that takes in the first name and returns an account that matches the name
        """
        for account in cls.users:
            if account.firstName == username:
                return account

    @classmethod
    def account_exists(cls,username):
        """
        method to check if an account exists
        """
        for account in cls.users:
            if account.firstName == username:
                return True

                return False