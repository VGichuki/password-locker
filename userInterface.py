#!/usr/bin/env python3

from userFile import UserData #import UserData from the userFile
from credentialsFile import Credentials #import Credentials from credentialsFile

#user account 
def new_account(firstName,lastName,password):
    """
    function to create an account
    """
    new_users=UserData(firstName,lastName,password)
    return new_users

def save_account(userFile):
    """
    function to save an account
    """
    userFile.save_account()

def delete_account(userFile):
    """
    function to delete an account
    """
    userFile.delete_account()

def find_account(username):
    """
    function to find an account
    """
    return UserData.find_account(username)

def account_exists(username):
    """
    function to check if an account exists
    """
    return UserData.account_exists(username)

#credential 
def new_credential(site,site_username,site_password):
    """
    function to that create a new credential
    """
    new_credential=Credentials(site,site_username,site_password)
    return new_credential

def save_credential(credentialsFile):
    """
    function to save credentials
    """
    credentialsFile.save_credential()

def generate_password():
    """
    function that generates random password
    """
    return Credentials.generate_password()

def display_credential():
    """
    function to display credentials
    """
    return Credentials.display_credentials()

def delete_credential(credentialFile):
    """
    function to delete credentials
    """
    credentialFile.delete_credential()

def find_credential(site_username):
    """
    find credentials by username
    """
    return Credentials.credential_exists(site_username)

#userInterface
def Interface():
    print("Welcome to the password locker app")
    print('\n')

    print("Please Create an account........")

    print("Enter Firstname.....")
    firstName=input()
    print("Enter Lastname.......")
    lastName=input()
    print("Create Password......")
    password=input()



if __name__=='__main__':
    Interface()





    
