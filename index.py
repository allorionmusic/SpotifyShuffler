import random

lines = open('spotify.txt').readlines()
random.shuffle(lines)
open('spotify.txt', 'w').writelines(lines)
print('Done!')