from nearby import nearby
from stars import stars


def main():
    tuple_list = [('HTML', 15, 'M0111'), ('JavaScript', 10, 'M031'), ('Bootstrap', 5, 'M02111')]
    sorted_list = sorted(tuple_list, key=lambda x: (x[2], x[1], len(x[0]), -x[1]))
    print(sorted_list)
    nearby(['100100011', '0001100001', '100001001', '1110010111'], 4)
    stars(arr=input().split(' '))


if __name__ == '__main__':
    main()
