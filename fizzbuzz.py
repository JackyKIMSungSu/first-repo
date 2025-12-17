# 1. delete both
# 2. one delete
# 3. remain both
# 4. make new one

# >>>>>>>>>> To make the status of running finally
# seperated line(<<<=============>>>) must be deleted!!!(if not, looks beginner)
for i in range(1, 18+1):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
