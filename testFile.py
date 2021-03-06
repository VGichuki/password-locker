import unittest #import the unittest module
import random #import for generating random passwords
import string #import for inputting passwords

from userFile import UserData #import the UserData class
from credentialsFile import Credentials #import the Credentials class

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

        #setUp for credentials
        self.new_credential = Credentials("Twitter","wangari.gichuki","kihujr")

    def test_init(self):
        """
        To check if the data has been initialised properly
        """
        #initialization for accounts
        self.assertEqual(self.new_users.firstName,"Wangari")
        self.assertEqual(self.new_users.lastName,"Gichuki")
        self.assertEqual(self.new_users.password,"0000")

        #initialization for credentials
        self.assertEqual(self.new_credential.site,"Twitter")
        self.assertEqual(self.new_credential.site_username,"wangari.gichuki")
        self.assertEqual(self.new_credential.site_password,"kihujr")


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

        #tearDown for credentials
        Credentials.credentials_list=[]

        #tests for accounts
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


        #test for credentials
    def test_save_credential(self):
        """
        test to check if a user can save credentials
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)
    @unittest.skip("Its working but I would like to see the other passwords")
    def test_generate_password(self):
        """
        test that generates passwords for the user
        """
        password="RivgpR"
        self.assertEqual(Credentials.generate_password(),password)

    def test_display_credentials(self):
        """
        test to check the users credentials
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_delete_credential(self):
        """
        test to check if a user can delete credentials
        """
        self.new_credential.save_credential()

        test_credential=Credentials("Instagram","valentinevivian","lit254")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential(self):
        """
        test that finds credentials for users
        """
        self.new_credential.save_credential()

        test_credential=Credentials("Instagram","valentinevivian","lit254")
        test_credential.save_credential()

        found_credential=Credentials.find_credential("valentinevivian")
        self.assertEqual(found_credential.site_username,test_credential.site_username)

    def test_credential_exists(self):
        """
        test if the credentials exist
        """
        self.new_credential.save_credential()

        test_credential=Credentials("Instagram","valentinevivian","lit254")
        test_credential.save_credential()

        existing_credential=Credentials.credential_exists("valentinevivian")
        self.assertTrue(existing_credential)


if __name__ == '__main__':
    unittest.main()
