def show_args(title, *args, **kwargs):
    print(f"{title} args '{args}' and kwargs '{kwargs}'")
def show_more(name,*args,**kwargs):
    print(kwargs)


if __name__=="__main__":
    show_args(1)
    show_args("one unnamed argument", 1)
    show_args("one named argument", second="2",third=2)
    show_args("one of each", 3, fourth="4")