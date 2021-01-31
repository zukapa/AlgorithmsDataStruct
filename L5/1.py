from collections import namedtuple


def profit():
    count_enterprise = int(input('Enter count enterprises: '))
    enterprise = namedtuple('et', 'name profit_q1 profit_q2 profit_q3 profit_q4')
    average = []
    average_less = []
    average_over = []
    for el in range(count_enterprise):
        globals()['ep_%s' % el] = \
            enterprise(name=input('Enter name enterprise: '),
                       profit_q1=int(input('Enter profit enterprise for 1 quarter: ')),
                       profit_q2=int(input('Enter profit enterprise for 2 quarter: ')),
                       profit_q3=int(input('Enter profit enterprise for 3 quarter: ')),
                       profit_q4=int(input('Enter profit enterprise for 4 quarter: ')))
        average.append((globals()['ep_%s' % el].profit_q1 +
                       globals()['ep_%s' % el].profit_q2 +
                       globals()['ep_%s' % el].profit_q3 +
                       globals()['ep_%s' % el].profit_q4) / 4)
    average_all = sum(average) / len(average)
    print('Average profits for all enterprises:', average_all)
    for ind, val in enumerate(average):
        if val > average_all:
            average_over.append(globals()["ep_%s" % ind].name)
        else:
            average_less.append(globals()["ep_%s" % ind].name)
    print('Profit enterprises > profits for all enterprises:', ', '.join(average_over))
    print('Profit enterprises < profits for all enterprises:', ', '.join(average_less))


profit()
