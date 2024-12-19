def finding_uncommon_elements(list1, list2):
    unc_list = []

    for el in list1:
        if el not in list2:
            unc_list.append(el)

    for el in list2:
        if el not in list1:
            unc_list.append(el)

    return unc_list

list1 = [1,1,2]
list2 = [2,3,4]
print(finding_uncommon_elements(list1, list2))