import os
import time


def main():
    while True:
        userName = input("please enter your Username: ")
        PassWord = input("Please enter your password: ")

    if userName == "bob" and PassWord == "watuwangu":
        time.sleep(2)
        print("Login Successful")
        logged()
    else:
        print("Password is wrong")


def logged():
    time.sleep(2)
    print("Welcome")


main()
