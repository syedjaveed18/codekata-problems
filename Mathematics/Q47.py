L,B,H = map(int,input().split())
volume = L*B*H
surface_area = 2*(L*B + B*H + H*L)
print(surface_area,volume)
