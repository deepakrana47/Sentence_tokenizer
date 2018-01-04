import re,random

def find(s, chs):
    temp=[]
    for ch in chs:
        temp+=[i for i, ltr in enumerate(s) if ltr == ch]
    return temp

def match(text):
    if re.search(r"([^ \.]+[^A-Z \.]{1})[ ]*\.[ ]+([A-Z0-9])",text):
        return '1'
    elif re.search(r"([^ \.]+[^A-Z \.]{1})[ ]*;[ ]+([A-Za-z0-9])",text):
        return '1'
    else:
        return '0'

def fix5(tempv):
    # 0 ==> 1
    tempv = re.sub(r'([a-z]{2}\. \[[A-Z]..)\t0', r'\1\t1', tempv)
    tempv = re.sub(r'([0-9]\. [A-Z]...)\t0', r'\1\t1', tempv)
    tempv = re.sub(r'(^.....\.[ ]*[\)\(][ ]*[A-Z].*)\t0', r'\1\t1', tempv)
    tempv = re.sub(r'(^.{0,4}[\)\(][ ]{0,4}\.[ ]{0,4}[A-Z].{0,4})\t0', r'\1\t1', tempv)
    tempv = re.sub(r'([0-9]\. [0-9]...)\t0', r'\1\t1', tempv)
    tempv = re.sub(r' ([A-Z])(\. ....)\t1', r' \1\2\t0', tempv)

    # 1 ==> 0
    tempv = re.sub(r' (Mr|Dr|Ms|ST|St|Md|Mt|Lt|Jr)(\. ....)\t1', r' \1\2\t0', tempv)
    tempv = re.sub(r' (Mrs|Gen|Sgt|Jan|Feb|Aug|Oct|Nov|Dec)(\. ....)\t1', r' \1\2\t0', tempv)
    tempv = re.sub(r' (Miss|Sept|Capt|Brig)(\. ....)\t1', r' \1\2\t0', tempv)
    tempv = re.sub(r'(\. [a-z]...)\t1', r'\1\t0', tempv)
    tempv = re.sub(r'([A-Z][a-z]\. [0-9]...)\t1', r'\1\t0', tempv)
    tempv = re.sub(r'([a-z]\. [a-z]...)\t1', r'\1\t0', tempv)
    return tempv

# def fix4(tempv):
#     # 0 ==> 1
#     tempv = re.sub(r'([a-z]{2}\. \[[A-Z].)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r'([0-9]\. [A-Z]..)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r'(^....\.[ ]*[\)\(][ ]*[A-Z].*)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r'(^.{0,3}[\)\(][ ]{0,3}\.[ ]{0,3}[A-Z].{0,3})\t0', r'\1\t1', tempv)
#     tempv = re.sub(r'([0-9]\. [0-9]..)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r' ([A-Z])(\. ...)\t1', r' \1\2\t0', tempv)
#
#     # 1 ==> 0
#     tempv = re.sub(r' (Mr|Dr|Ms|ST|St|Md|Mt|Lt|Jr)(\. ...)\t1', r' \1\2\t0', tempv)
#     tempv = re.sub(r' (Mrs|Gen|Sgt|Jan|Feb|Aug|Oct|Nov|Dec)(\. ...)\t1', r' \1\2\t0', tempv)
#     tempv = re.sub(r'(Miss|Sept|Capt|Brig)(\. ...)\t1', r'\1\2\t0', tempv)
#     tempv = re.sub(r'(\. [a-z]..)\t1', r'\1\t0', tempv)
#     tempv = re.sub(r'([A-Z][a-z]\. [0-9]..)\t1', r'\1\t0', tempv)
#     tempv = re.sub(r'([a-z]\. [a-z]..)\t1', r'\1\t0', tempv)
#     return tempv

# def fix10(tempv):
#     # 0 ==> 1
#     tempv = re.sub(r'([a-z]{2}\. \[[A-Z].......)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r'([0-9]\. [A-Z]........)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r'(^..........\.[ ]*[\)\(][ ]*[A-Z].*)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r'(^.........[\)\(][ ]*\.[ ]*[A-Z].*)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r'([0-9]\. [0-9]........)\t0', r'\1\t1', tempv)
#     tempv = re.sub(r' ([A-Z])(\. .........)\t1', r' \1\2\t0', tempv)
#
#     # 1 ==> 0
#     tempv = re.sub(r' (Mr|Dr|Ms|ST|St|Md|Mt|Lt|Jr)(\. .........)\t1', r' \1\2\t0', tempv)
#     tempv = re.sub(r' (Mrs|Gen|Sgt|Jan|Feb|Aug|Oct|Nov|Dec)(\. .........)\t1', r' \1\2\t0', tempv)
#     tempv = re.sub(r' (Miss|Sept|Capt|Brig)(\. .........)\t1', r' \1\2\t0', tempv)
#     tempv = re.sub(r'(\. [a-z]........)\t1', r'\1\t0', tempv)
#     tempv = re.sub(r'([A-Z][a-z]\. [0-9]........)\t1', r'\1\t0', tempv)
#     tempv = re.sub(r'([a-z]\. [a-z]........)\t1', r'\1\t0', tempv)
#     return tempv

def int_to_8bit_binary(inp):
    # if inp > 255:
    #     print "Not an ascii character !!"
    #     return -1
    inp = ord(inp)
    temp = []
    while inp > 1:
        temp.append(inp % 2)
        inp = int(inp/2)
    temp.append(1)
    if len(temp) < 8:
        temp += [0 for i in range(8-len(temp))]
    return list(reversed(temp))

def generate_dataset(fname):
    tfd= open(fname,'r')
    text=tfd.read(50000)
    count = 1
    fcount = 1
    data = []
    # coll = ''

    context = 5
    if context == 5:
        fix = fix5
    # elif context == 10:
    #     fix = fix10
    # elif context == 4:
    #     fix = fix4

    while text and fcount < 5:
        text = re.sub(r'[^\x00-\x7F]', r'', text)
        text = re.sub(r'\n|\t', r' ', text)
        temp = find(text, '.;')
        count+=len(temp)
        for i in temp:
            val = text[i-context:i+context+1]
            # check for data size
            if len(val) != 2*context+1:
                continue
            tempv = val + '\t' + match(val)
            tempv = fix(tempv)

            # converted to binary input and label
            input, label = tempv.split('\t')
            binary = []
            for j in input[0:context] + input[context+1:]:
                binary += int_to_8bit_binary(j)

            # text input and label
            # coll += tempv+'\n'
            lab = [1, 0] if label == '1' else [0, 1]
            data.append([binary, lab])
        text = tfd.read(50000)
    return data

def partition(data, prob=.7):
    train=[]
    test=[]
    for i in data:
        if random.random() < prob:
            train.append(i)
        else:
            test.append(i)
    return train, test

def make_dataset(fname='text.txt'):
    data = generate_dataset(fname)
    train, test = partition(data, prob=.8)
    return train, test