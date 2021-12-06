'''
Use a binary number report to genereate gama rate, epsilon rate and calculate
the power consumption (gamma*epsilon)
'''

from collections import Counter

'''
Gamma rate can be determined by finding the most common bit
in the corresponding position of all numbers in report
'''

'''
Epsilon rate can be determined by finding the least common bit
in the correspinding position of all numbers in report
'''

BINARY_REPORT = ['00100','11110','10110','10111','10101','01111',
                 '00111','11100','10000','11001','00010','01010']

def calc_common(binary_data,option):
    '''find the most common '''
    final_value = []
    for i in range(len(binary_data[0])):
        nth_elements = []
        for items in binary_data:
            nth_elements.append(items[i])
        c = Counter(nth_elements)
        #For most common
        if option == 'most':
            most = c.most_common(1)[0][0]
            final_value.append(most)
        #For least common
        if option == 'least':
            least = c.most_common()[-1][0]
            final_value.append(least)
    binary = ''.join(final_value)
    return int(binary,2)
        
gamma = calc_common(BINARY_REPORT,'most')
epsilon = calc_common(BINARY_REPORT,'least')

power_consumption = gamma * epsilon

print(power_consumption)
