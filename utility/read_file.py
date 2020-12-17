class ReadFile:

    @staticmethod
    def read_lines(filename):
        with open(filename, 'r') as f:
            try:
                for line in f:
                    yield line
            except FileNotFoundError:
                print('no file!')
            finally:
                f.close()
