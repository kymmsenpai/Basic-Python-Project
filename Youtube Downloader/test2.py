import time
from tqdm import tqdm

for i in tqdm(range(20), desc = 'tqdm() Progress Bar'):
    time.sleep(0.5)


# ui = '|/\|/\|/\|'
# size = 100
# for i in range(size):
#     time.sleep(0.2)
#     print(f'\r{ui[i%len(ui)]}', end='')
# print('\r| DONE')


# loop 10 times
# for i in range(10):
#     # print the current iteration number
#     print(f"Iteration {i+1}", end="\r")
#     # wait for 1 second
#     time.sleep(1)

x = 'okokoook'

print(x, end='\r')
time.sleep(0.5)
print(' '*len(x), end='\r')

print('yaaaaaa')





