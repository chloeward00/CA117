def swap_unique_keys_values(b):
    swapped_dictionary = {}
    for i in b:
        if b[i] in swapped_dictionary:
            del (swapped_dictionary[b[i]])
        else:
            swapped_dictionary[b[i]] = i
    return swapped_dictionary


def main():

    x = {1: "a", 2: "b", 3: "c", 4: "c"}
    print (swap_unique_keys_values(x))

if __name__ == "__main__":
    main()
