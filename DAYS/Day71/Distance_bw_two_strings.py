def Edit_distance(Str1, Str2):
    if len(Str1) > len(Str2):
        distance = len(Str1)-len(Str2)
    elif len(Str2) > len(Str1):
        distance = len(Str2)-len(Str1)
    else:
        distance = 0
    for i in range(len(Str1)):
        if Str1[i] != Str2[i]:
            print(f"Replace: {Str1[i]} <--> {Str2[i]}")
            distance += 1
    return f"Replacement Required: {distance}\n"


if __name__ == "__main__":
    print(Edit_distance("Kitten", "Sitting"))
    print(Edit_distance("Medium", "Median"))
