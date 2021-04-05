def TOH(disks, source, aux, to):
    if disks == 1:
        print(f"Move Disk from {source} to {to}")
        return
    else:
        TOH(disks-1, source, to, aux)
        print(f"Move Disk from {source} to {to}")
        TOH(disks-1, aux, source, to)


if __name__ == "__main__":
    num = int(input("How many Disks: "))
    TOH(num, 'A', 'B', 'C')
