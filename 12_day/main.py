from itertools import permutations


with open('puzzle.txt', 'r') as f:
    lines = f.read().split('\n')


def filter_paths(paths):
    valid_paths = []
    for path in paths:

        import pdb; pdb.set_trace()


class Cave:
    def __init__(self, path):
        self.entry = path.split('-')[0]
        self.exit = path.split('-')[1]
        self.once = 


valid_paths = filter_paths(paths)
import pdb; pdb.set_trace()