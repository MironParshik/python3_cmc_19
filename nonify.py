def nonify(func):
    def new_return(*args_nn,**args_n):
        if not func(*args_nn,**args_n):
            return None
        else:
            return func(*args_nn,**args_n)
    return new_return
