import time
timesleep={1:1.5,2:1.2,3:1,4:0.6,5:0.0001}
def bubblesort(data,draw_lines,time_interval,color):
    print(time_interval)
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if(data[j]>data[j+1]):
                data[j],data[j+1]=data[j+1],data[j]
                
                color=["sea green" if x==j+1 else "indian red" for x in range(len(data))]
                draw_lines(data,color)
                time.sleep(timesleep[time_interval])
        
    draw_lines(data,["sea green"]*len(data))