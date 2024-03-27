def sequence_sum(begin_number, end_number, step):
    current=begin_number
    sum=begin_number
    while True:
        if begin_number>end_number: return 0
        elif begin_number==end_number: return begin_number
        elif current==end_number or current+step>end_number: return sum
        current=current+step
        sum+=current


print(sequence_sum(2, 24, 22))

# Alternative
# def sequence_sum(start, end, step):
#     return sum(range(start, end+1, step))