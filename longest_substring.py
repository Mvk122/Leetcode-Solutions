def longest(s):
        start_pointer = 0 
        end_pointer = start_pointer
        maximum = 0
        char_dict = {}
        while start_pointer < len(s):
            if end_pointer == len(s):
                if end_pointer - start_pointer > maximum:
                    maximum = end_pointer - start_pointer
                return maximum
            print(f"{start_pointer} : {end_pointer}")
            if s[end_pointer] in char_dict.keys():
                print()
                if end_pointer - start_pointer > maximum:
                    maximum = end_pointer - start_pointer
                start_pointer += 1
                char_dict = {}
                end_pointer = start_pointer
                continue
            else:
                char_dict[s[end_pointer]] = 1
                end_pointer += 1
        return maximum

print(longest("au"))