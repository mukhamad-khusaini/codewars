def sequence_sum(begin_number, end_number, step):
    i=begin_number
    count=0
    while i < end_number+1:
        if(i>end_number): return 0
        if(i==end_number): return count
        count+=i+step
        i=i+step


print(sequence_sum(1,5,1))