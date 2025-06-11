import random
import sys
import time
import datetime


def dek(path, path2):
    vreme = datetime.datetime(2023, 12, 11, 2, 10, 1).timestamp()

    gif1 = [71, 73, 70, 56, 57, 97]
    gif2 = [71, 73, 70, 56, 55, 97]

    random_seed = str(round(vreme / 10)) + '.' + ''.join((str(b) for b in gif1[:6]))
    random.seed(random_seed)

    with open(path, 'rb') as f:
        file_content_bytes = [b for b in f.read()]

    file_content_bytes = [int('{:08b}'.format(b)[::-1], 2) for b in file_content_bytes]
    print("Posle prevrtanja bajtova: " + str(file_content_bytes[:6]))

    file_content_bytes_swapped = []

    for i in range(len(file_content_bytes)):
        modified_index = i + 1 if i % 2 == 0 else i - 1
        file_content_bytes_swapped.append(file_content_bytes[modified_index])

    file_content_bytes = file_content_bytes_swapped
    print("Posle zamene parnih i neparnih indeksa: " + str(file_content_bytes[:6]))

    order = list(range(len(file_content_bytes)))
    random.shuffle(order)
    random.shuffle(order)

    original = [0] * len(file_content_bytes)
    for index, originalIndex in enumerate(order):
        original[originalIndex] = file_content_bytes[index]

    print("Posle shuffle: " + str(original[:6]))
    with open(path2, 'wb') as f:
        f.write(bytes(original))


def enk(path, path2):
    flags = {'ማወዛወዝ': {'አትቀላቅ': True, 'ቁጥር_ጊዜ': 1}}
    try:
        fp = path
        op = path2
    except:
        print('ሥራህ ለቅዱስ አይገባውም። አጠቃቀም: encryptor.exe [inpath] [outpath]')
        sys.exit(1)
    with open(fp, 'rb') as f:
        file_content_bytes = [b for b in f.read()]
    random_seed = 17
    print('የዘፈቀደ ዘር; {}'.format(random_seed))
    print('ስለዚህ በመንግሥተ ሰማያት ጸጋ "random.seed" እጠቀማለሁ እና ይህን የርኩሰት አጸዳለሁ')
    random.seed(random_seed)
    print('ባንዲራዎችን በውዝ; {}'.format(flags['ማወዛወዝ']))
    for t in range(flags['ማወዛወዝ']['ቁጥር_ጊዜ'] if flags['ማወዛወዝ'] else 1):
        if flags['ማወዛወዝ'] and flags['ማወዛወዝ'].get('አትቀላቅል'):
            pass
            print("?")
        else:
            random.shuffle(file_content_bytes)
            print("!")
    print('2 ማወዛወዝ')
    random.shuffle(file_content_bytes)
    file_content_bytes_swapped = []
    for i in range(len(file_content_bytes)):
        modified_index = i + 1 if i % 2 == 0 else i - 1
        file_content_bytes_swapped.append(file_content_bytes[modified_index])
    file_content_bytes = file_content_bytes_swapped
    print('እርሳቱ! :D')
    file_content_bytes = [int('{:08b}'.format(b)[::-1], 2) for b in file_content_bytes]
    with open(op, 'wb') as f:
        f.write(bytes(file_content_bytes))


fp = "kafica_wow.gif.enc"
op = "kafica_wow.gif"
dek(fp, op)
