def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = len(s)
    if 2 <= l <= 6 and s[0] not in '0123456789' and s[1] not in '0123456789':
        return True
    else:
        return False



main()