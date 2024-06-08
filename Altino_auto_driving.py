from Altino import *


Open()


def auto(a, f_sp, b_sp):
    if sensor.IR[1] > a and sensor.IR[2] > a and sensor.IR[3] > a :
        if sensor.IR[4] > sensor.IR[5] :
            Go(b_sp, b_sp)
            steering(120)
        else :
            Go(b_sp, b_sp)
            steering(-120)
    else :
        if sensor.IR[1] > a and sensor.IR[2] > a :
            Go(b_sp, b_sp)
            steering(120)
        else :
            if sensor.IR[1] > a and sensor.IR[2] > a :
                Go(b_sp, b_sp)
                steering(120)
            else :
                if sensor.IR[1] > a :
                    Go(f_sp, f_sp)
                    steering(60)
                else :
                    if sensor.IR[3] > a :
                        Go(f_sp, f_sp)
                        steering(-60)
                    else :
                        Go(f_sp, f_sp)
                        steering(0)


while sensor.IR[4] > 300 :
    while sensor.CDS < 100 :
        auto(15, 350, -400)
        delay(1000)
        
Go(0, 0)
steering(0)

Close()
