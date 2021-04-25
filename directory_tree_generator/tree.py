import os
os.system('clear')

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

class Dir:

    def __init__(self, root_dir):
        global initial_dir_level
        self.root_dir = root_dir
        self.files = []
        self.dirs = []
        self.level = self.root_dir.count('/') - initial_dir_level

        for f in os.listdir(self.root_dir):
            temp_path = f"{self.root_dir}/{f}"
            if os.path.isfile(temp_path):
                self.files.append(f)
            else:
                self.dirs.append(Dir(temp_path))


    def __str__(self):

        basename = self.root_dir.split('/')[-1]
        r = ""
        if self.level == 0:
            r += f"{basename}/\n│\n"
        elif len(self.files) == 0:
            r += f" {basename}/"
        else:
            r += f" {basename}/\n"

        if len(self.dirs) > 0:
            for i in range(len(self.dirs)):
                r += self.level * PIPE_PREFIX + f"{TEE}{self.dirs[i]}\n"

        for i in range(len(self.files)):
            if i == len(self.files)-1:
                r += self.level * PIPE_PREFIX + f"{ELBOW} {self.files[i]}" + f"\n{self.level*PIPE_PREFIX}"
            else:
                r += self.level * PIPE_PREFIX + f"{TEE} {self.files[i]}\n"

        return r


root_folder = 'directory_tree_generator/hello'
initial_dir_level = root_folder.count('/')

root = Dir(root_folder)
print(root)
