import itertools


def subset_sum(numbers, target, partial, ret_list):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        ret_list.append(partial)
        return ret_list
        # print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return ret_list  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n], ret_list)
    return ret_list


if __name__ == "__main__":
    e1, e2 = [], []
    eng1 = int(input("first engraving book points?"))
    cnt3_val = 0
    if eng1 == 12:
        e1 = [3]
        cnt3_val = 1
    elif eng1 == 9:
        e1 = [3, 3]
        cnt3_val = 2
    eng2 = int(input("second engraving book points?"))
    if eng2 == 12:
        e2 = [3]
        cnt3_val += 1
    elif eng2 == 9:
        e2 = [3, 3]
        cnt3_val += 2
    rock = input("rock points(split by space, enter like 7 8)?")
    eng3 = int(rock.split(" ")[0])
    eng4 = int(rock.split(" ")[1])
    eng5 = 0
    acc_cnt = 0
    while True:
        accs = input("any accessories(eng1 is your first engraving and eng2 is your second, eng3 is rock top row, eng4 is rock bottom row, and eng5 is the last one, enter like eng3 6 eng5 7)?")
        if accs == 'no' or accs == 'No' or accs == 'NO':
            break
        else:
            acc_cnt += 1
            temp = accs.split(" ")
            if temp[0] == "eng3":
                eng3 += int(temp[1])
            elif temp[0] == "eng4":
                eng4 += int(temp[1])
            elif temp[0] == "eng5":
                eng5 += int(temp[1])
            elif temp[0] == "eng1":
                cnt3_val -= 1
                if int(temp[1]) + eng1 >= 15:
                    e1 = []
                else:
                    e1 = [3]
            elif temp[0] == "eng2":
                cnt3_val -= 1
                if int(temp[1]) + eng2 >= 15:
                    e2 = []
                else:
                    e2 = [3]
            if len(temp) > 2:
                if temp[2] == "eng3":
                    eng3 += int(temp[3])
                elif temp[2] == "eng4":
                    eng4 += int(temp[3])
                elif temp[2] == "eng5":
                    eng5 += int(temp[3])
                elif temp[2] == "eng1":
                    cnt3_val -= 1
                    if int(temp[3]) + eng1 >= 15:
                        e1 = []
                    else:
                        e1 = [3]
                elif temp[2] == "eng2":
                    cnt3_val -= 1
                    if int(temp[3]) + eng2 >= 15:
                        e2 = []
                    else:
                        e2 = [3]
    comp3 = max(15 - eng3, 0)
    if comp3 < 3 and comp3 != 0:
        comp3 = 3
    comp4 = max(15 - eng4, 0)
    if comp4 < 3 and comp4 != 0:
        comp4 = 3
    comp5 = max(15 - eng5, 0)
    if comp5 < 3 and comp5 != 0:
        comp5 = 3
    final_output = []
    eng3_list = subset_sum([3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5], comp3, [], [])
    eng3_list.sort()
    eng3_list = list(k for k, _ in itertools.groupby(eng3_list))
    eng4_list = subset_sum([3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5], comp4, [], [])
    eng4_list.sort()
    eng4_list = list(k for k, _ in itertools.groupby(eng4_list))
    eng5_list = subset_sum([3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5], comp5, [], [])
    eng5_list.sort()
    eng5_list = list(k for k, _ in itertools.groupby(eng5_list))
    #print(eng3_list, eng4_list, eng5_list)
    for e3 in eng3_list:
        for e4 in eng4_list:
            for e5 in eng5_list:
                cnt3 = cnt3_val
                cnt45 = 0
                cnt3 += len([i for i in e3 if i == 3])
                cnt45 += len([i for i in e3 if i >= 4])
                cnt3 += len([i for i in e4 if i == 3])
                cnt45 += len([i for i in e4 if i >= 4])
                cnt3 += len([i for i in e5 if i == 3])
                cnt45 += len([i for i in e5 if i >= 4])
                #print(e3, e4, e5, cnt3, cnt45, acc_cnt)
                if cnt45 <= (5 - acc_cnt) and cnt45 + cnt3 <= (10 - acc_cnt * 2) and len(e3) <= (5 - acc_cnt) and len(e4) <= (5 - acc_cnt) and len(e5) <= (5 - acc_cnt):
                    temp_dict = {"eng1": e1, "eng2": e2, "eng3": e3, "eng4": e4, "eng5": e5}
                    final_output.append(temp_dict)

    if len(final_output) == 0:
        print("read legendary books or cut a better stone KEKW")
    else:
        print("printing all {} results:".format(len(final_output)))
        for i in final_output:
            print("eng1:{}, eng2:{}, eng3:{}, eng4:{}, eng5:{}\n".format(i["eng1"], i["eng2"], i["eng3"], i["eng4"], i["eng5"]))
