from config import m1,m2_base,wall,x1,x2,width1,width2,collisions
from physics import vel_block_collison,vel_wall_collision

print("Enter Upto Which digit of PI you want to see:")
digits = int(input())

m2 = m2_base**(digits-1)

vel1 = 0
vel2 = -30

dt = 0.001

def update(x1,x2,vel1,vel2,collisions):
    x1 += vel1*dt
    x2 += vel2*dt
    if x1 <= width1/2 and vel1 < 0:
            vel1 = vel_wall_collision(vel1)
            collisions += 1

        # Block collision
    if x2 - x1 <= (width1 + width2)/2 and vel2 < vel1:
        old_vel1 = vel1
        old_vel2 = vel2

        vel1 = vel_block_collison(m1, m2, old_vel1, old_vel2)

        vel2 = vel_block_collison(m2, m1, old_vel2, old_vel1)

        collisions += 1
    return x1, x2, vel1, vel2, collisions
