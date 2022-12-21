import sys


def main():
    card = input("Number: ")
    card_len = len(str(card))

    sum1 = 0
    sum2 = 0
    sum_all = 0
    temp1 = 0
    temp2 = 0

    if card_len != 13 and card_len != 15 and card_len != 16:
        print("INVALID")
        sys.exit()

    for i in range(-2, (-card_len-1), -2):
        temp1 = int(card[i]) * 2
        if temp1 >= 10:
            sum1 = sum1 + temp1 - 9
        else:
            sum1 = sum1 + temp1

    for i in range(-1, (-card_len-1), -2):
        temp2 = int(card[i])
        sum2 = sum2 + temp2

    sum_all = sum1 + sum2

    if sum_all % 2 == 0:
        if int(card[0]) == 3 and int(card[1]) == 4 or int(card[1]) == 7:
            print("AMEX")
        elif int(card[0]) == 5 and int(card[1]) >= 1 and int(card[1]) <= 5:
            print("MASTERCARD")
        elif int(card[0]) == 4:
            print("VISA")
        else:
            print("INVALID")


if __name__ == "__main__":
    main()