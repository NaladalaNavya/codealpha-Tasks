pos = -1
def search(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1;
            else:
                u = mid-1;

    return False


user_input = input("Enter numbers separated by spaces: ")

# Split the input string by spaces and convert to a list of integers
numbers_list = [int(num) for num in user_input.split(",")]

print("Numbers entered by the user:",numbers_list)
n = int(input("Enter the number:"))

if search(numbers_list, n):
    print("Found at ",pos+1)
else:
    print("Not Found")

