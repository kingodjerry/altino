from Altino import * 
import datetime 


#자율주행 함수 Auto  
#Auto(0)->오른쪽 자율주행
#Auto(1)->왼쪽 자율주행
def Auto(direction=0,th=35,sp=280,bsp=-280) :
    if sensor.IR[1]>th and sensor.IR[2]>th and sensor.IR[3]>th :
        if direction == 0 :
            Go(bsp,bsp);Steering(127);
        else :
            Go(bsp,bsp);Steering(-127);
    elif sensor.IR[1]>100 and sensor.IR[2]>th :
        Go(bsp,bsp);Steering(-127);
    elif sensor.IR[1]>th and sensor.IR[2]>th :
        Go(sp,sp);Steering(127); 
    elif sensor.IR[2]>th and sensor.IR[3]>100 :
        Go(bsp,bsp);Steering(127);
    elif sensor.IR[2]>th and sensor.IR[3]>th :
        Go(sp,sp);Steering(-127);
    elif sensor.IR[1]>th :
        Go(sp,sp);Steering(64);
    elif sensor.IR[3]>th :
        Go(sp,sp);Steering(-64);
    else :
        Go(sp,sp);Steering(0);


Open() 

# 1번 6번 적외선 센서 감지 시 출발
while 1 : 
    if sensor.IR[6] > 400 :
        break

Go(300, 300); Steering(-120); delay(200)

Old_Time=datetime.datetime.now() 
while 1 :
    Auto(1) 
    Time_Check=datetime.datetime.now()-Old_Time 
    if sensor.CDS <200 and Time_Check.seconds > 2 : 
        break                                 


# 터널 3을 감지하면 멈추고, 디스플레이에 "ALTINO" 출력
Go(-350,-350);Steering(0);delay(150)
Go(0,0);Steering(0)

name = ['A', 'L', 'T', 'I', 'N', 'O']

for i in range(0, 6) :
    Display(name[i])
    delay(500)

Display(0)


Old_Time=datetime.datetime.now()

while 1 :
    Auto(0) 
    Time_Check=datetime.datetime.now()-Old_Time
    if sensor.CDS <200 and Time_Check.seconds > 4 :
        break                                       


# 마지막 벽을 감지하면 곰세마리 재생
while 1 :
    Auto(1)
    if sensor.IR[1]>26 and sensor.IR[2]>26 and sensor.IR[3]>26 :
        break

Go(-350,-350);Steering(0);delay(150)
Go(0,0);Steering(0)


Sound(37);delay(400);Sound(0);delay(100)
Sound(37);delay(200);Sound(0);delay(100)
Sound(37);delay(200);Sound(0);delay(100)
Sound(37);delay(400);Sound(0);delay(100)
Sound(37);delay(400);Sound(0);delay(100)
Sound(41);delay(400);Sound(0);delay(100)
Sound(44);delay(200);Sound(0);delay(100)
Sound(44);delay(200);Sound(0);delay(100)
Sound(41);delay(400);Sound(0);delay(100)
Sound(37);delay(400);Sound(0);delay(100)
Sound(44);delay(200);Sound(0);delay(100)
Sound(44);delay(200);Sound(0);delay(100)
Sound(41);delay(400);Sound(0);delay(100)
Sound(44);delay(200);Sound(0);delay(100)
Sound(44);delay(200);Sound(0);delay(100)
Sound(41);delay(400);Sound(0);delay(100)
Sound(37);delay(400);Sound(0);delay(100)
Sound(37);delay(400);Sound(0);delay(100)
Sound(37);delay(800)
Sound(0)


close()
