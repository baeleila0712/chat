#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    BAeee_word_count = 0
    BAeee_sticker_count = 0
    BAeee_image_count = 0
    Hui_word_count = 0
    Hui_sticker_count = 0
    Hui_image_count = 0

    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'BAeee':
            if s[2] == '圖片':
                BAeee_image_count += 1
            elif s[2] == '貼圖':
                BAeee_sticker_count += 1
            else:
                for m in s[2:]:
                    BAeee_word_count += len(m)
                               
        elif name == 'Hui':
            if s[2] == '圖片':
                Hui_image_count += 1
            elif s[2] == '貼圖':
                Hui_sticker_count += 1
            else:       
                for m in s[2:]:
                    Hui_word_count += len(m)


    print('BAeee說了', BAeee_word_count, '個字')
    print('BAeee傳了', BAeee_image_count, '張圖片')
    print('BAeee傳了', BAeee_sticker_count, '張貼圖')
    print('Hui傳了', Hui_word_count, '個字')
    print('Hui傳了', Hui_image_count, '張圖片')
    print('Hui傳了', Hui_sticker_count, '張貼圖')
        #print(s)


def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')    


def main():
    lines = read_file('[LINE]Hui.txt')
    lines = convert(lines)

main()