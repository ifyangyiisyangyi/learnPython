import zipfile
import itertools


class crack_zip():
    '''
    暴力破解压缩文件
    '''

    def generate_nums(self):
        nums = [str(i) for i in range(10)]
        # chrs = [chr(i) for i in range(65, 91)]
        return itertools.permutations(nums, 3)

    def extract_file(self, zip_file, password):
        try:
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f'提取密码为：{password}')
            return True
        except:
            print(f'current {password} password is not correct')
            return False

    def main(self):
        pwd_lst = self.generate_nums()
        file = zipfile.ZipFile('test.zip', 'r')
        for i in pwd_lst:
            pwd = ''.join(i)
            if self.extract_file(file, pwd):
                break
            else:
                continue


if __name__ == '__main__':
    test = crack_zip()
    test.main()
