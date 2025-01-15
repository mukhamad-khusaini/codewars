def row_weights(array):
    return (sum(array[i-1] for i in range(1,len(array)+1) if i%2!=0),sum(array[i-1] for i in range(1,len(array)+1) if i%2==0))