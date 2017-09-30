import os
class wenjianbianli(object):
    def __init__(self):
        self.cur_dir=os.curdir
        self.ext={}

    def dir_check(self,file):
        if os.path.isdir(file):
            return 1
        if os.path.isfile(file):
            return 0

    def get_file_type(self,file):
        return os.path.splitext(file)[1][1:]

    def file_bianli(self,file):
        print file,os.path.isdir(file)
        if self.dir_check(file) == 1:
            cur_dir=os.listdir(file)
            for i in cur_dir:
                self.file_bianli(os.path.join(file,i))
        if self.dir_check(file) == 0:
            extent=self.get_file_type(file)
            if self.ext.has_key(extent):
                count=int(self.ext.get(extent))+1
                self.ext.update({extent:count})
            else:
                self.ext.update({extent:1})
            return

    def run(self):
        self.file_bianli(self.cur_dir)
        print '[*]Result: '
        for i in self.ext:
            print i,self.ext[i]

if __name__=='__main__':
    cls=wenjianbianli()
    cls.run()
