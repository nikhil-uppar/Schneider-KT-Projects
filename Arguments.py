def Arguments(*args,**kwargs):
    print("positional arguments:",args)
    print("keyword arguments:",kwargs)
Arguments(1,2,3,{"key": "value"}, language = "Python")
