def longest_subarray(array):
    
    zeros_counter = 0
    ones_counter = 0

    for i in range(len(array)):
        if(array[i] != '1' or array[i] != '0'):
            print(f"you entered an unacceptable input {array[i]} so it will get removed in order to continue the program :)")
            array.remove(i)
        else:
            for i in range(len(array)):
                if(array[i] == '1'):
                    ones_counter+1
                else:
                    zeros_counter+1

    return 0

numbers_sequence = input("Please enter the series of 1s and 0s you want \nbe sure to leave a space between each number")
numbers_sequence = numbers_sequence.split()
longest_subarray(numbers_sequence)

#didnt know how to continue the program after this step so i'll get back to it later