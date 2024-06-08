from Altino import* #알티노 모듈 


#자율주행 함수 Auto  
#Auto(0)->오른쪽 자율주행
#Auto(1)->왼쪽 자율주행

steering(0)

def Auto(direction=0,th=37,sp=280,bsp=-300) :
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

# 1번: 4번센서 손으로 터치하면 시작
while 1 : 
    if sensor.IR[4] > 400 and sensor.IR[5]> 400 :
        break

# 1번터널 감지시 함수 탈출
while 1 :
    Auto(0)
    if sensor.CDS < 130 :
        break
    
# 정지
Go(-350,-350)
delay(150)
Go(0,0)

# 2번: 4옥타브 파,도,파,라 소리내고 끈 후 출발
Sound(42);delay(500)
Sound(37);delay(500)
Sound(42);delay(500)
Sound(46);delay(500)
Sound(0)


Go(290,240)
Steering(40)
delay(800)
Go(300,180)
Steering(127)
delay(2400)
Go(-350,-350)
Steering(-127)
delay(150)

while 1 :
    Auto(1)
    if sensor.CDS < 120 :
        break
    
# 3번: 터널2 감지하면 멈추고
Go(-350,-350)
delay(150)
Go(0,0)

#3번: 도트매트릭스 8분음표
DisplayLine(0x00,0x06, 0x0F,0x0F, 0x06, 0xFE, 0x40, 0x38)
Delay(1000)
Display(0)

stop()

Close()