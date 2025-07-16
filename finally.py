
def try_finally():
  try: 
    print('hi')
    return 'hello'
  except:
    return 'not reached'
  finally: 
    print('finally also reached') # even though the try is true, this finally will run before it

print(try_finally())
