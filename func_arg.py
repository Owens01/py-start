# def add(val1, val2):
#     return val1 + val2


# user = input("Add a value: ")
# result = add(4, int(user))

# print(result)


# keyword arguments
def person(name, **keylarge):
    print("name :", name)
    # print(keylarge)

    #to print each value from person func we use for loop
    for a,b in keylarge.items():
        print(a, ":", b)


person(name="Owen", age="20", location="coming soon", tech="python")
