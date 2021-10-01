import matplotlib.pyplot as plt


def overlapped():
    # single subplot
    plt.subplot(1, 1, 1)
    x = 1, 1, 3, 3, 1
    y = 1, 3, 3, 1, 1
    plt.plot(x, y, 'm:p')

    x = 2, 2, 4, 4, 2
    y = 2, 4, 4, 2, 2
    plt.plot(x, y, 'c--h')

    x = 3, 3, 5, 5, 3
    y = 3, 5, 5, 3, 3
    plt.plot(x, y, 'y-.D')

    plt.show()


overlapped()


def individual():
    plt.subplot(3, 3, 1)
    x = 1, 1, 3, 3, 1
    y = 1, 3, 3, 1, 1
    plt.plot(x, y, 'mp:')

    plt.subplot(3, 3, 2)
    x = 2, 2, 4, 4, 2
    y = 2, 4, 4, 2, 2
    plt.plot(x, y, 'c--h')

    plt.subplot(3, 3, 3)
    x = 3, 3, 5, 5, 3
    y = 3, 5, 5, 3, 3
    plt.plot(x, y, 'y-.D')
    plt.show()


individual()


def info():
    dict1 = {}
    dict1.setdefault("left", [])
    # dict1["left"].append([])
    dict1["left"].append([[1, 1, 3, 3, 1], [1, 3, 3, 1, 1], 'mp:'])
    dict1.setdefault("middle", [])
    dict1["middle"].append([[2, 2, 4, 4, 2], [2, 4, 4, 2, 2], 'c--h'])
    dict1.setdefault("right", [])
    dict1["right"].append([[3, 3, 5, 5, 3], [3, 5, 5, 3, 3], 'y-.D'])

    return dict1


def individual_using_info():
    squares = info()
    for key, value in squares.items():
        list1 = list(value)
        x = list1[0][0]
        y = list1[0][1]
        z = list1[0][2]

        plt.plot(x, y, z)
        plt.show()


individual_using_info()



# import matplotlib.pyplot as plt
# # def overlapped():
# #     # single subplot
# #     plt.subplot(1,1,1)
# #     x = 1,1,3,3,1
# #     y = 1,3,3,1,1
# #     plt.plot(x,y,'m:p')
# #
# #
# #     x = 2, 2, 4, 4,2
# #     y = 2, 4, 4, 2,2
# #     plt.plot(x, y, 'c--h')
# #
# #
# #     x = 3, 3, 5, 5,3
# #     y = 3, 5, 5, 3,3
# #     plt.plot(x, y, 'y-.D')
# #
# #     plt.show()
# # overlapped()
#
# def individual():
#     plt.subplot(2,2,1)
#     x = 1, 1, 3, 3, 1
#     y = 1, 3, 3, 1, 1
#     plt.plot(x,y,'mp:')
#
#     # plt.subplot(2,2,2)
#     # x = 2, 2, 4, 4,2
#     # y = 2, 4, 4, 2,2
#     # plt.plot(x,y,'c--h')
#     #
#     # plt.subplot(2,2,3)
#     # x = 3, 3, 5, 5,3
#     # y = 3, 5, 5, 3,3
#     # plt.plot(x,y,'y-.D')
#     plt.show()
#
# individual()
#

