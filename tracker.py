#!/usr/bin/env python
# -'''- coding: utf-8 -'''-

from datetime import datetime, timedelta

start_work_at = datetime.strptime(input('Start work at (\'HH:MM\'): '), '%H:%M')
go_to_lunch_at = datetime.strptime(input('Go to lunch at (\'HH:MM\'): '), '%H:%M')
back_from_lunch_at = datetime.strptime(input('Back from lunch at (\'HH:MM\'): '), '%H:%M')
already_done = go_to_lunch_at - start_work_at
rest_to_do = datetime.strptime('08:00', '%H:%M') - already_done
end_work_at = back_from_lunch_at + timedelta(hours=rest_to_do.hour, minutes=rest_to_do.minute)
print('End work at: \'%s\'' % end_work_at.strftime('%H:%M'))
