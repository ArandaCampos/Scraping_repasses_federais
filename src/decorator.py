from time import sleep

# Decorator retry
def retry(repeat, secounds):
    count = 0
    def decorator(funcs):
        def closure(*args, **kwargs):
            nonlocal count
            try:
                funcs(*args, **kwargs)
            except:
                count+=1
                print(f'Função: {funcs.__name__} falhou. Tentativas: {count}')
                if count < repeat:
                    sleep(secounds)
                    return closure(*args, **kwargs)
        return closure
    return decorator
