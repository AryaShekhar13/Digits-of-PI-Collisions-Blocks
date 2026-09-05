from config import m1,m2_base,wall,x1,x2,width1,width2
from physics import vel_block_collison,vel_wall_collision

print("Enter Upto Which digit of PI you want to see:")
digits = int(input())

m2 = m2_base**(digits-1)
collisions = 0

vel1 = 0
vel2 = -20

dt = 0.001

def main():
    global x1, x2, vel1, vel2, collisions
    while True:
        x1 += vel1*dt
        x2 += vel2*dt
        if x1 <= wall and vel1 < 0:
            vel1 = vel_wall_collision(vel1)
            collisions += 1

        # Block collision
        if x2 - x1 <= width1 + width2 and vel2 < vel1:
            old_vel1 = vel1
            old_vel2 = vel2

            vel1 = vel_block_collison(m1, m2, old_vel1, old_vel2)

            vel2 = vel_block_collison(m2, m1, old_vel2, old_vel1)

            collisions += 1

        # No more collisions possible
        if vel2 >= vel1 and vel1 >= 0:
            break
main()
print("Digits of PI:",collisions)