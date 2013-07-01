import os

class fuzzy_finder:
    def __init__(self, root, suffix=''):
        ''' helpful for finding files without putting massive great paths in scripts '''
        self.root=root
        self.mega=[]
        for root,dirs,files in os.walk(root):
            self.mega+=map(lambda x: os.path.join(root, x), files)
        self.mega=filter(lambda x: x.endswith(suffix), self.mega)

    def find(self, substring):
        ''' fuzzy-find a file and return its path '''
        items=[]
        for item in self.mega:
            if substring in item: items.append(item)
        if len(items)==1: return items[0]
        if len(items)>1: return items
        print '%s not found!!!' % substring
        raw_input()

    def __str__(self):
        ''' convert to string '''
        return '\n'.join(self.mega)
