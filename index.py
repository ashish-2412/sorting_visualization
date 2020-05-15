from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubblesort
from quicksort import quickSort
selected_algo=""
data=[]
def generate():
    global data
    try:
        min_val=int(minval.get())
    except:
        min_val=1
    try:
        max_val=int(maxval.get())
    except:
        max_val=10
    try: 
        s=int(asize.get())
    except:
        s=10
    if min_val<0:min_val=0
    if max_val>100:max_val=100
    
    if min_val>max_val:min_val,max_val=max_val,min_val
    data=[]
    for _ in range(s):
        data.append(random.randrange(min_val,max_val+1))
    draw_lines(data,["indian red"]*len(data))
def draw_lines(data,color):
    
    canvas.delete("all")
    normalized_data=[i/max(data) for i in data]
    c_height=380
    c_width=600
    x_width=c_width/(len(data)+1)
    offset=0
    spacing=5
    
    for i,height in enumerate(normalized_data):
        #topleft
        x0=i*x_width+offset+spacing
        y0=c_height-height*350
        #bottomright
        x1=(i+1)*x_width+offset
        y1=c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=color[i])
        
    root.update_idletasks()
def startsort():
    global data
    if not data:return
    if(selectbox.get()=="Quick Sort"):
        quickSort(data,0,len(data)-1,draw_lines,speed_scale.get())
        draw_lines(data,["sea green"]*len(data))
    elif selectbox.get()=="Bubble Sort":
        bubblesort(data,draw_lines,speed_scale.get(),["indian red"]*len(data))
    

root=Tk()
root.title("Sorting Visualization")
root.minsize(650,550)
root.config(bg='white')
menu=Frame(root,width="900",height="800",bg='slate grey')
menu.grid(row=0,column=0,padx=0,pady=0)
canvas=Canvas(root,width=600,height=380)
canvas.grid(row=1,column=0,padx=20,pady=5)

b1=Button(menu,text="Generate random values",command=generate,bg="indian red")
b1.grid(row=2,column=3,padx=0,pady=5)

l1=Label(menu,text="Sorting Algorithm",bg='azure')
l1.grid(row=0,column=0,padx=5,pady=5,sticky=W)
selectbox=ttk.Combobox(menu,textvariable=selected_algo,values=["Bubble Sort","Quick Sort"])
selectbox.grid(row=0,column=1,padx=5,pady=5)
selectbox.current(0)

speed_scale=Scale(menu,from_=1,to=5,length=150,digits=2,resolution=1,orient=HORIZONTAL,label="Select speed")
speed_scale.grid(row=2,column=0,padx=5,pady=5)

start=Button(menu,text="Start!",command=startsort,bg="sea green")
start.grid(row=2,column=2,padx=(0,50),pady=5)


asize=Scale(menu,from_=10,to=140,length=150,digits=3,resolution=10,orient=HORIZONTAL,label="Select size")
asize.grid(row=1,column=0,padx=5,pady=5,sticky=W)

l3=Label(menu,text="Minimum value",bg='azure')
l3.grid(row=1,column=1,padx=5,pady=5,sticky=W)
minval=Entry(menu,width=10)
minval.grid(row=1,column=2,padx=5,pady=5,sticky=W)

l4=Label(menu,text="Maximum value",bg='azure')
l4.grid(row=1,column=3,padx=5,pady=5,sticky=W)
maxval=Entry(menu,width=10)
maxval.grid(row=1,column=4,padx=5,pady=5,sticky=W)


root.mainloop()