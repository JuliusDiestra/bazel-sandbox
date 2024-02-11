
import sys

sys.path.append('..')

import my_package.class_foo
import my_package.class_data

def main():
    foo = my_package.class_foo.Foo()
    data = my_package.class_data.Data(10)
    print("Value in data object : " + str(data.get_value()))
    data.set_value(20)
    print("Value in data object after update : " + str(data.get_value()))

if __name__ == "__main__":
    main()
