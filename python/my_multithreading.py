import multiprocessing

def __return_wrapper(func,arr):
    def wrapper(*args, **kwargs):
        arr += [func(*args, **kwargs)]
    return wrapper

def thread(*func, **kwargs):
    arr = []
    return_arr = []
    for i in range(len(func)):
        x = multiprocessing.Process(target=__return_wrapper( func[i], return_arr ), args=arg[i])
        x.start()
        arr += [x]

    for i in range(len(arr)):
        arr[i].join()
    
    return return_arr