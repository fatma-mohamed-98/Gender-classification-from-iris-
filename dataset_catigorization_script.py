import xlrd
import os
import shutil

male_dirc='D:\Dataset\Male'
female_direc='D:\Dataset\Female'

Lmale_dirc='D:\Dataset\Male_L'
Lfemale_direc='D:\Dataset\Female_L'

Rmale_dirc='D:\Dataset\Male_R'
Rfemale_direc='D:\Dataset\Female_R'
data_direc='D:\Dataset\IrisImage'

direc_arr=[male_dirc, female_direc, Lmale_dirc, Lfemale_direc, Rmale_dirc, Rfemale_direc]

for direc in direc_arr:
    os.makedirs(direc, exist_ok=True)
#****************************************************************************************
workbook = xlrd.open_workbook('D:\Dataset\METADATA.xlsx')
workbook = xlrd.open_workbook('D:\Dataset\METADATA.xlsx', on_demand = True)
worksheet = workbook.sheet_by_index(0)
label = []
for row in range(worksheet.nrows):
    label.append( worksheet.cell_value(row,0) )
#****************************** Separate to male and female*****************************
data=os.listdir(data_direc)
i=1
for file in label:
    if file =='M':
        src_dir = data_direc+'/'+str(i)
        dst_dir = male_dirc
        shutil.move(src_dir,dst_dir)
    else:
        src_dir = data_direc + '/' + str(i)
        dst_dir = female_direc
        shutil.move(src_dir, dst_dir)
    i=i+1
# #**************************************Separate female to left and right******************************

female = os.listdir(female_direc)
for file in female:
    direction = os.listdir(female_direc+'/'+str(file))
    for index, d in enumerate(direction):
        if d =='L1.JPG' or d =='L2.JPG' or d =='L3.JPG' or d =='L1L.JPG' or d =='L2L.JPG' or d =='L3L.JPG' or d =='LL1.JPG' or d =='LL2.JPG' or d =='LL3.JPG':
            os.rename(os.path.join(female_direc + '/' + str(file), d),os.path.join(female_direc + '/' + str(file),''.join([str(index + 1) + str(file), '.JPG'])))
            src_dir = female_direc+'/'+str(file)+'/'+str(index + 1) + str(file)+'.JPG'
            dst_dir = Lfemale_direc
            shutil.move(src_dir,dst_dir)
        elif d =='R1.JPG' or d =='R2.JPG' or d =='R3.JPG' or d =='RR1.JPG' or d =='RR2.JPG' or d =='RR3.JPG' or d =='R1R.JPG' or d =='R2R.JPG' or d =='R3R.JPG':
            os.rename(os.path.join(female_direc + '/' + str(file), d),os.path.join(female_direc + '/' + str(file),''.join([str(index + 1) + str(file), '.JPG'])))
            src_dir = female_direc + '/' + str(file) + '/' +str(index + 1) + str(file)+'.JPG'
            dst_dir = Rfemale_direc
            shutil.move(src_dir, dst_dir)
        else:
            pass
#**********************************Separate male to left and right*****************************************
male = os.listdir(male_dirc)
for file in male :
    direction = os.listdir(male_dirc+'/'+str(file))
    for index, d in enumerate(direction):
        if d =='L1.JPG' or d =='L2.JPG' or d =='L3.JPG' or d =='L1L.JPG' or d =='L2L.JPG' or d =='L3L.JPG' or d =='LL1.JPG' or d =='LL2.JPG' or d =='LL3.JPG':
            os.rename(os.path.join(male_dirc + '/' + str(file), d),os.path.join(male_dirc + '/' + str(file),''.join([str(index + 1) + str(file), '.JPG'])))
            src_dir = male_dirc+'/'+str(file)+'/'+str(index + 1) + str(file)+'.JPG'
            dst_dir = Lmale_dirc
            shutil.move(src_dir,dst_dir)


        elif d == 'R1.JPG' or d == 'R2.JPG' or d == 'R3.JPG' or d == 'RR1.JPG' or d == 'RR2.JPG' or d == 'RR3.JPG' or d == 'R1R.JPG' or d == 'R2R.JPG' or d == 'R3R.JPG':
            os.rename(os.path.join(male_dirc + '/' + str(file), d),os.path.join(male_dirc + '/' + str(file),''.join([str(index + 1) + str(file), '.JPG'])))
            src_dir = male_dirc + '/' + str(file) + '/' +str(index + 1) + str(file)+'.JPG'
            dst_dir = Rmale_dirc
            shutil.move(src_dir, dst_dir)
        else:
            pass

