def over_the_road(address, n):
    if address%2!=0:
        ad=address+1
        mid=n+0.5
        delta=abs(ad-mid)
        if ad>mid:
            return int(mid-delta+1)
        else:
            return int(mid+delta+1)
    else:
        ad=address-1
        mid=n+0.5
        delta=abs(ad-mid)
        if ad>mid:
            return int(mid-delta-1)
        else:
            return int(mid+delta-1)

print(over_the_road(8,6))