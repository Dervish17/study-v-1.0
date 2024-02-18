from horse2 import horse2
from template import template
from func_table import func_table


def main():
    horse2(cell=input())
    template(4, 5, 4)
    func_table('x ** 2 + y', 3, 5)


if __name__ == '__main__':
    main()
