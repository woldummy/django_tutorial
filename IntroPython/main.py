# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    i = 10
    # while i > 0:
    #     print(i)
    #     i = i-1
    # for i in range(1, 11):
    #     print(f'Zahl: {i}')
    mystyring = "Hallo Welt"
    print(mystyring)
    for letter in mystyring:
        print(letter, end=',')
    print()
    print(mystyring[2:5])  # slicing
    print(len(mystyring))
    txt = "The best things in life are freE!"
    if "free" in txt:
        print("Yes, 'free' is present.")
    # Liste
    mylist = [[10, 20, 30, 40, 50], [10, 20, 30, 40, 50]]
    for the_list in mylist:
        for number in the_list:
            print(number, end=',')
    print(type(mylist))

    dict1 = {'er': 'he', 'sie': 'she', 'es': 'it'}
    for key in dict1:
        print(key, ':', dict1[key])
    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())
    print(len(dict1))
    for key, val in dict1.items():
        print(key, ':', val)
    print(dict1.get('er1', 'No key'))
