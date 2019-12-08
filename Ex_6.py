'''
שאלה 3 :תיכנות – מכרז מיירסון לבעיית התרמיל
נתון מערך גלובלי בשם weights ,שבו האיבר ה-i מייצג את המשקל של השחקן ה-i.
א. בחרו אחד מאלגוריתמי-הקירוב שלמדנו )א, ב, או א+ב(, וכיתבו את פונקציית-הבחירה המתאימה לו:
def choices (values: List[double]) → List[bool]: ...
ב. בחרו אחד מאלגוריתמי-הקירוב שלמדנו )א, ב, או א+ב(, וכיתבו את פונקציית-התשלום המתאימה לו:
def payments (values: List[float]) → List[float]: ...
כאן )בניגוד לשאלה הקודמת( חישוב התשלומים צריך להיות מדוייק, ע"י נוסחה מפורשת.
'''
import random
create_weight_list = lambda x: [random.randint(1,100) for i in range(x)]
weights = create_weight_list(50)

def fill_backpack(values, a_sort):
    picked = [False for i in range(len(values))]

    # Backpack [Weight,Value]
    backpack = [0, 0]
    while (backpack[0] + weights[a_sort[0][0]]) > 100:
        a_ind = a_sort.pop(0)[0]
        backpack[0] += weights[a_ind]
        backpack[1] += values[a_ind]
        picked[a_ind] = True
    return backpack, picked

# def choices (values: List[double]) → List[bool]: ...
def choices(values):
    '''
    Greedy A:
        sort by descending values
        fill backpack till full
    Greedy B:
        sort by descending value to weight ratio
        fill backpack till full
    :param values: list, value of agent i is value[i]
    :return: vector of selected items (True) and not selected (False)
    '''
    # Algorithm A sorted vector
    a_sort = list(enumerate(values))
    a_sort.sort(key=lambda x:x[1], reverse=True)

    # Algorithm B sorted vector
    b_rat = [val/weight for (val, weight) in zip(values, weights)]
    b_sort = list(enumerate(b_rat))
    b_sort.sort(key=lambda x: x[1], reverse=True)

    # Fill back pack
    a_backpack, a_picked = fill_backpack(values, a_sort)
    b_backpack, b_picked = fill_backpack(values, b_sort)

    if a_backpack[1] > b_backpack[1]:
        return a_picked
    else:
        return  b_picked



# def payments (values: List[float]) → List[float]: ...
def payments(values):
    picked = choices(values)
    calc_bag = lambda v, p: [v[i] for i in range(len(p)) if p[i] is True]
    bag_val = sum(calc_bag(values, picked))
    res = [0.0]*(len(values))
    for i in range(len(values)):
        if picked[i]:
            temp_values = values.copy()
            temp_values[i] = 0
            pick_temp = choices(temp_values)
            this_bag = sum(calc_bag(temp_values, pick_temp))
            val = bag_val - this_bag
            res[i] = val
            del temp_values
    return res
