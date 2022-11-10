import tkinter
from PIL import Image, ImageTk
import os

path_0 = 'images'
files_0 = os.listdir(path_0)
num_png_0 = len(files_0)

path_1 = 'to_images'
files_1 = os.listdir(path_1)
num_png_1 = len(files_1)
# 创建一个窗口对象
screen = tkinter.Tk()
screen.title("森林火灾监测报警仪")
screen.geometry('1920x1080')
# 创建label对象
label1 = tkinter.Label(screen, text="温度(℃):", font=('宋体', 30, 'bold'))
label2 = tkinter.Label(screen, text="湿度(%rh):", font=('宋体', 30, 'bold'))
label3 = tkinter.Label(screen, text="状态指示灯(无火灾):", font=('宋体', 30, 'bold'))
label4 = tkinter.Label(screen, text="状态指示灯(有火灾):", font=('宋体', 30, 'bold'))

text = tkinter.Text(screen, width=15, height=1, font=("宋体", 30))
text_1 = tkinter.Text(screen, width=15, height=1, font=("宋体", 30))
text.place(x=1440, y=102)
text_1.place(x=1440, y=252)
txtfile = "p_main.txt"
f = open(txtfile, 'r', encoding='utf-8')
# lengths = len(f.readlines())


# 显示label,pack函数是自适应
label1.place(x=1190, y=100, height=50, width=250)
label2.place(x=1200, y=250, height=50, width=250)
label3.place(x=1190, y=650, height=50, width=400)
label4.place(x=1200, y=850, height=50, width=400)

mycanvas_0 = tkinter.Canvas(screen, width=3, height=1080, bg="white")
mycanvas_0.place(x=1100, y=0)
mycanvas0 = mycanvas_0.create_line(1.5, 0, 0, 1080, width=10)

mycanvas_1 = tkinter.Canvas(screen, width=1920, height=3, bg="white")
mycanvas_1.place(x=0, y=500)
mycanvas1 = mycanvas_1.create_line(0, 1.5, 1920, 0, width=10)

mycanvas_2 = tkinter.Canvas(screen, width=100, height=200)
mycanvas_2.place(x=0, y=180)
mycanvas2 = mycanvas_2.create_text(50, 50, text='拍摄', font=("宋体", 30))
mycanvas2_ = mycanvas_2.create_text(50, 100, text='图片', font=("宋体", 30))

mycanvas_3 = tkinter.Canvas(screen, width=100, height=200)
mycanvas_3.place(x=0, y=680)
mycanvas3 = mycanvas_3.create_text(50, 50, text='检测', font=("宋体", 30))
mycanvas3_ = mycanvas_3.create_text(50, 100, text='图片', font=("宋体", 30))
isok = 1
if isok == 1:
    color1 = 'white'
    color2 = 'red'

else:
    color1 = 'green'
    color2 = 'white'

mycanvas_4 = tkinter.Canvas(screen, width=100, height=100)
mycanvas_4.place(x=1650, y=620)
mycanvas4 = mycanvas_4.create_oval(5, 5, 95, 95, fill=color1)
mycanvas_5 = tkinter.Canvas(screen, width=100, height=100)
mycanvas_5.place(x=1650, y=820)
mycanvas5 = mycanvas_5.create_oval(5, 5, 95, 95, fill=color2)

# for i in range(num_png_0):
photo_0 = Image.open('images\image_' + str(0) + '.jpg')
photo_0 = photo_0.resize((995, 495))
img_png_0 = ImageTk.PhotoImage(photo_0)

label_img_0 = tkinter.Label(image=img_png_0)
label_img_0.place(x=105, y=5, height=495, width=995)

photo_1 = Image.open('to_images\image_' + str(0) + '.jpg')
photo_1 = photo_1.resize((995, 495))
img_png_1 = ImageTk.PhotoImage(photo_1)

label_img_1 = tkinter.Label(image=img_png_1)
label_img_1.place(x=105, y=507, height=495, width=995)
line = f.readline()
text.delete(0.0, tkinter.END)
text.insert('insert', line[:6])
text_1.delete(0.0, tkinter.END)
text_1.insert('insert', line[7:])
text.update()
text.after(1000)
text_1.update()
text_1.after(1000)
screen.update()
screen.after(1000)




f.close()




# 使用mainloop方法使得窗口显示
screen.mainloop()
