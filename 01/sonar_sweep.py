depth_report = [199,200,208,210,200,207,240,269,260,263]

def count_increase(value_report):
    '''Iterate through a list and count number of times a measurement increases'''
    previous_depth = value_report[0]
    increases = 0
    for key, depth in enumerate(value_report):
        if depth > previous_depth:
            increases += 1
        #Set this value to previous for next loop
        previous_depth = value_report[key]
    return increases
result = count_increase(depth_report)

print(result)