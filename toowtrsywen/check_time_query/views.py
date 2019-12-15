from collections import defaultdict
from datetime import datetime, timedelta
from typing import List

from django.template.defaulttags import register
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from check_in_out.models import CheckTime
from manager_user.models import ManagerWorkers
from django.contrib.auth.models import User


class WorkInterval:
    start: datetime
    end: datetime
    length: datetime

    def __init__(self):
        self.start = None
        self.end = None
        self.length = None


class DailyWork:
    intervals: List[WorkInterval]
    sum: timedelta
    date: datetime

    def __init__(self):
        self.intervals = []
        self.sum = timedelta(0)
        self.date = None

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def chop_microseconds(delta):
    return delta - timedelta(microseconds=delta.microseconds)

def unique(seq):
   s = set(seq)
   return list(s)

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    current_user = request.GET.get("current_user", request.user.get_username())
    check_times = CheckTime.objects.filter(name_text=current_user).order_by('timestamp')

    workers = list(map(lambda entry: entry.worker_name, ManagerWorkers.objects.filter(manager_name=request.user.get_username())))
    workers.append(request.user.get_username())

    if request.user.is_superuser:
       workers = workers + list(map(lambda entry: entry.username, User.objects.all()))

    workers = unique(workers)

    work_intervals_by_date = defaultdict(list)
    daily_work_log: List[DailyWork] = []
    for check_time in check_times:
        work_intervals_by_date[check_time.timestamp.date()].append(check_time)
    for date in work_intervals_by_date:
        daily_work = DailyWork()
        daily_work.date = date
        work_interval = WorkInterval()
        for check_time in work_intervals_by_date[date]:
            if check_time.in_or_out == "in" and work_interval.start is None:
                work_interval.start = check_time.timestamp
            elif check_time.in_or_out == "out" and work_interval.start is not None:
                work_interval.end = check_time.timestamp
                work_interval.length = chop_microseconds(work_interval.end - work_interval.start)
                daily_work.intervals.append(work_interval)
                daily_work.sum += work_interval.length
                work_interval = WorkInterval()

        daily_work.sum = chop_microseconds(daily_work.sum)
        daily_work_log.append(daily_work)

    weekly_work_log = defaultdict(list)
    weekly_work_sum = defaultdict(timedelta)
    for daily_work in daily_work_log:
        week = daily_work.date.isocalendar()[1]
        year = daily_work.date.isocalendar()[0]
        weekly_work_log[(year, week)].append(daily_work)
        weekly_work_sum[(year, week)] = weekly_work_sum[(year, week)] + daily_work.sum

    return render(request, 'names/query.html',
                  {'query': check_times,
                   'workers': workers,
                   'current_user': current_user,
                   'daily_work_log': daily_work_log, 'weekly_work_log': dict(weekly_work_log),
                   'weekly_work_sum': dict(weekly_work_sum),
                   'maximum_daily_work': timedelta(hours=12),
                   'maximum_weekly_work': timedelta(hours=48),
                   },
                  )

