import random

m_in_km = 1000
ft_in_mile = 5280
friends = ['Justin', 'Jake', 'Pi']

def get_file_ext(filename):
    return filename[filename.index('.') + 1:]

def roll_dice(x):
    return random.randint(1,x)