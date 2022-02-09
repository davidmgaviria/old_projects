# -*- coding: utf-8 -*-
hours_imp = input('Hours Worked: ')
rate_imp = input('Pay Rate: ')

total_hours = int(hours_imp)
standard_rate = int(rate_imp)
over_rate = standard_rate*1.5

if total_hours > 40:
    over_time = total_hours-40
    over_pay = over_rate*over_time
    pay = ((40*standard_rate)+over_pay)
    print('Check: {}'.format(pay))
else:
    pay = (total_hours*standard_rate)
    print('Check: {}'.format(pay))