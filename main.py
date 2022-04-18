import cv2
import csv
import os
import shutil


# pos: x,y,w,h
def pic_merge(base, diff, pos):
    x1 = pos[0]
    x2 = pos[0]+pos[2]
    y1 = pos[1]
    y2 = pos[1]+pos[3]
    pic1_path = os.path.join(path, pic_dict[base])
    pic2_path = os.path.join(path, pic_dict[diff])
    pic1 = cv2.imread(pic1_path)
    pic2 = cv2.imread(pic2_path)

    pic1[y1:y2, x1:x2] = pic2
    # cv2.imshow('1', pic1)
    # cv2.waitKey()
    save_path = './pic_out'
    # save_url = os.path.join(save_path, base.lower() + '_' + diff.lower()+'.png')
    save_url = os.path.join(save_path, diff.lower()+'.png')
    print(save_url)
    cv2.imwrite(save_url, pic1)


path = './'
os.makedirs('pic_out', exist_ok=True)
file_list = os.listdir(path)
pic_dict = {}
csv_list = []

for i in file_list:
    if i[-8:] == '.tlg.png':
        pic_dict[i[:-8].upper()] = i
    if i[-4:] == '.csv':
        csv_list.append(i)

for csv_file in csv_list:
    with open(csv_file) as f:
        f_csv = csv.reader(f)
        header = next(f_csv)
        # row: tag,base,diff,x,y,w,h,guidex,guidey,fillSamePixel
        for row in f_csv:
            base = row[1]
            diff = row[2]
            # copy base pic
            if diff == '':
                tmp_str = pic_dict[base]
                tmp_str = tmp_str[:-8] + tmp_str[-4:]
                sour = os.path.join(path, pic_dict[base])
                dest = os.path.join('./pic_out', tmp_str)
                shutil.copyfile(sour, dest)
                continue
            pos = [int(row[3]), int(row[4]), int(row[5]), int(row[6])]
            pic_merge(base, diff, pos)

