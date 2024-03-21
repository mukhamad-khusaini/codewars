def points(games):
    point=0
    for i in games:
        spliter=i.split(":")
        x,y=int(spliter[0]), int(spliter[1])
        if x>y: point+=3
        elif x<y: pass
        else: point+=1

    return point

print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))