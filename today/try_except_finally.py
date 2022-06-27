# f = open('new_file.')
try:
    f = open('new_file.pp', 'r')
except Exception as err:
    print(err)
finally:
    f.close()