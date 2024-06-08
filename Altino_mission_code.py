from Altino import* #알티노 모듈 
import datetime #타이머 체크 위한 객채


#자율주행 함수 Auto  
#Auto(0)->왼쪽 자율주행
#Auto(1)->오른쪽 자율주행
def Auto(direction=0,th=26,sp=280,bsp=-350) :
    if sensor.IR[1]>th and sensor.IR[2]>th and sensor.IR[3]>th :
        if direction == 0 :
            Go(bsp,bsp);Steering(127);Display(6);
        else :
            Go(bsp,bsp);Steering(-127);Display(128+4);
    elif sensor.IR[1]>100 and sensor.IR[2]>th :
        Go(bsp,bsp);Steering(-127);Display(128+4);#왼쪽 뒤
    elif sensor.IR[1]>th and sensor.IR[2]>th :
        Go(sp,sp);Steering(127);Display(5);#오른쪽 많이 
    elif sensor.IR[2]>th and sensor.IR[3]>100 :
        Go(bsp,bsp);Steering(127);Display(6);#오른쪽 뒤
    elif sensor.IR[2]>th and sensor.IR[3]>th :
        Go(sp,sp);Steering(-127);Display(128+5);
    elif sensor.IR[1]>th :
        Go(sp,sp);Steering(64);Display(4);#오른쪽 조금
    elif sensor.IR[3]>th :
        Go(sp,sp);Steering(-64);Display(128+6);
    else :
        Go(sp,sp);Steering(0);Display(3);#전진


Open() # 블루투스 연결

#로봇 A의 적외선 센서 4번을 손으로 터치하면(10점) 반복문 벗어남
while 1 : 
    if sensor.IR[4] > 400 :
        break

while 1 :
    Auto(1) #출발한다(오른쪽_자율주행)(10점)
    if sensor.CDS <130 : #터널 1을 감지하면(조도 값 200은 조명 상황에 따라 변경) 벗어남
        break

#멈추고(5점).
Go(-350,-350);Steering(0);delay(150)
Go(0,0);Steering(0)

#0.5초 간격으로 4옥타브 도, 미를 3번 소리 내고(10점)
Sound(37);delay(500);Sound(41);delay(500)
Sound(37);delay(500);Sound(41);delay(500)
Sound(37);delay(500);Sound(41);delay(500)
Sound(0) #소리를 끄고

Old_Time=datetime.datetime.now() #현재 시간 불러옴

while 1 :
    Auto(1) #출발한다(오른쪽으로 자율주행).(5점)
    Time_Check=datetime.datetime.now()-Old_Time #while문에 들어온 시간 체크 
    if sensor.CDS <200 and Time_Check.seconds > 2 : #while문에 들어온 시간이 2초 후면 
        break                                       #while문 벗어남

#멈추고(10점).
Go(-350,-350);Steering(0);delay(150)
Go(0,0);Steering(0)

#아래와 같이 도트매트릭스(디스플레이)에 출력하고
DisplayLine(0x38,0x44,0x42,0x21,0x21,0x42,0x44, 0x38)
delay(1000) #1초 후
Display(0) #끈다

close()






    






        
