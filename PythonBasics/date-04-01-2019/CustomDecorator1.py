def entry_exitForCompany(func):
    def learn():
        print(func.__name__,"Joining today")
        func()
        print("Exiting from",func.__name__,"today")
    return learn

@entry_exitForCompany
def office():
    print("inside office")

office()
print(office.__name__)