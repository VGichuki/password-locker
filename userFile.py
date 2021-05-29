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