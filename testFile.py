import unittest #import the unittest module
from userFile import UserData #import the UserData class

class TestAccount(unittest.TestCase):
    """
    Test class that defines test cases for the userFile and credentials.
    """

    def setUp(self):
        """
        Method to run before each test case.
        """
        #setUp for an account
        self.new_users = UserData("Wangari","Gichuki","0000")

    def test_init(self):
        """
        To check if the data has been initialised properly
        """
        self.assertEqual(self.new_users.firstName,"Wangari")
        self.assertEqual(self.new_users.lastName,"Gichuki")
        self.assertEqual(self.new_users.password,"0000")

    def test_save_account(self):
        """
        test if we can save data in user list
        """
        self.new_users.save_account()
        self.assertEqual(len(UserData.users),1)

    def tearDown(self):
        """
        cleans up the user list which stores accounts
        """
        #tearDown for accounts
        UserData.users=[]

    def test_delete_account(self):
        """
        test that ensures we can remove an account from the user list
        """
        self.new_users.save_account()

        test_users = UserData("Nina", "Wangui","1111")
        test_users.save_account()

        self.new_users.delete_account()
        self.assertEqual(len(UserData.users),1)

    def test_find_account(self):
        """
        test to check if we can find an account
        """
        self.new_users.save_account()

        test_users = UserData("Nina","Wangui","1111")
        test_users.save_account()

        found_users = UserData.find_account("Nina")
        self.assertEqual(found_users.firstName,test_users.firstName)

    def test_account_exists(self):
        """
        test to check if we can return a boolean if we cannot find the account
        """
        self.new_users.save_account()

        test_users = UserData("Nina","Wangui","1111") #new account
        test_users.save_account()

        account_exists = UserData.account_exists("Nina")

        self.assertTrue(account_exists)







if __name__ == '__main__':
    unittest.main()
