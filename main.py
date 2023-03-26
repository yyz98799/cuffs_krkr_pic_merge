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
    pic1 = cv2.imread(pic1_path, cv2.IMREAD_UNCHANGED)
    pic2 = cv2.imread(pic2_path, cv2.IMREAD_UNCHANGED)

    pic1[y1:y2, x1:x2] = pic2
    save_path = './pic_out'
    save_url = os.path.join(save_path, pic_dict[diff].split('.')[0] + '.png')
    print(save_url)
    # save as RGBA
    cv2.imwrite(save_url, pic1)


path = './'
os.makedirs('pic_out', exist_ok=True)
file_list = os.listdir(path)
pic_dict = {}
csv_list = []
image_format = ['png', 'jpg', 'bmp']

for i in file_list:
    tmp_sp = i.split('.')
    if tmp_sp[-1] in image_format:
        pic_dict[tmp_sp[0].upper()] = i
    if tmp_sp[-1] == 'csv':
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
                tmp_sp = tmp_str.split('.')
                # tmp_str = tmp_sp[0] + '.' + tmp_sp[-1]
                sour = os.path.join(path, pic_dict[base])
                dest = os.path.join('./pic_out', tmp_sp[0]+'.png')
                # cv2.imread(sour, cv2.IMREAD_UNCHANGED)
                cv2.imwrite(dest, cv2.imread(sour, cv2.IMREAD_UNCHANGED))
                # shutil.copyfile(sour, dest)
                print("copy: " + dest)
                continue
            pos = [int(row[3]), int(row[4]), int(row[5]), int(row[6])]
            pic_merge(base, diff, pos)

