def nonify(func):
    def new_return(args):
        if not func(*args):
            return None
        else:
            return func
    8
    return new_return
