'''
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.
'''

def main():
    name = input("Please input your name:")
    age = input("Please input your age:")
    username = input("Please input your username:")

    file = open("information.txt", "w")
    file.write(name)
    file.write(age)
    file.write(username)

    print ("Your name is {0}, you are {1} years old, and your username is {2}.".format(name, age, username))

main()
