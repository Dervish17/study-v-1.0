from groundhog_day import groundhog_day
from gears import gears
from brackets import brackets


def main():
    brackets('([{}])()<{}>')
    groundhog_day(["Groundhog Festival in Punxsutawney.",
                   "Groundhog Festival in Punksutawney.",
                   "Groundhog Festivel in Punxsutowney."])
    gears([[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]], 30, 7)


if __name__ == '__main__':
    main()
