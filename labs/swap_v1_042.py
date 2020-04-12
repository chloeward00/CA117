def swap_keys_values(b):
    swapped_dictionary = {}
    for i in b:
        swapped_dictionary[b[i]] = i
    return swapped_dictionary


def main():

    x = {1: "a", 2: "b", 3: "c"}
    print (swap_keys_values(x))

if __name__ == "__main__":
    main()
