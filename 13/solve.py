pairs = open("13/input.txt").read().split("\n\n")


def is_in_order(item1, item2):
    if isinstance(item1, list) and isinstance(item2, list):
        for elem1, elem2 in zip(item1, item2):
            compare = is_in_order(elem1, elem2)
            if compare is not None:
                return compare
        if len(item1) == len(item2):
            return None
        else:
            return len(item1) < len(item2)
    if isinstance(item1, int) and isinstance(item2, int):
        if item1 == item2:
            return None
        if item1 < item2:
            return True
        else:
            return False
    if isinstance(item1, int):
        return is_in_order([item1], item2)
    elif isinstance(item2, int):
        return is_in_order(item1, [item2])


in_order_inds = []
for ind, pair in enumerate(pairs):
    item1, item2 = pair.split("\n")
    item1, item2 = eval(item1), eval(item2)
    if is_in_order(item1, item2):
        in_order_inds.append(ind + 1)

print(sum(in_order_inds))
