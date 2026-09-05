def vel_block_collison(m1,m2,u1,u2):
    vel = ((m1-m2)*u1 + 2*m2*u2)/(m1+m2)
    return vel

def vel_wall_collision(vel):
    return -1*vel