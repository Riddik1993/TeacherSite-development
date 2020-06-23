from calendar import HTMLCalendar, month_name,_localized_month, LocaleHTMLCalendar,different_locale
from datetime import datetime as dtime, date, time
import datetime
from datetime import date, datetime, timedelta, time
from .models import Event

# -*- coding: utf8 -*-
class EventCalendar(LocaleHTMLCalendar):
    def __init__(self, events=None,locale=None):
        super(EventCalendar, self).__init__()
        self.events = events
        self.locale=locale

    def formatday(self, day, weekday,theyear,themonth, events):
        """
        Return a day as a table cell.
        """
        events_from_day = events.filter(day__day=day)
        events_html = ""

        for event in events_from_day:
            events_html +="<div class='cal_ev_ex'>" + event.notes + "</div>"


        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            if day<datetime.today().day:
                return '<td class="%s"><span style="display:none">%s</span><div class="expired">%d</div>%s</td>' % (self.cssclasses[weekday],date(theyear,themonth,day),day, events_html)
            elif day==datetime.today().day:
                return '<td class="%s"><span style="display:none">%s</span><div class="today_cal">%d%s</div></td>' % (self.cssclasses[weekday],date(theyear,themonth,day), day, events_html)
            else:
                return '<td class="%s"><span style="display:none">%s</span>%d%s</td>' % (self.cssclasses[weekday],date(theyear,themonth,day), day, events_html)







    def formatweek(self, theweek,theyear,themonth, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd,theyear,themonth, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name as a table row.
        """


        if withyear:
            with different_locale(self.locale):
                s = '%s %s' % (month_name[themonth], theyear)
        else:
            with different_locale(self.locale):
                s = '%s' % month_name[themonth]
        return "<tr><th colspan='7' class='%s'><button class='prev_month cal_button' >пред. месяц </button>&nbsp&nbsp%s&nbsp&nbsp<button class='next_month cal_button'> след. месяц </button></th></tr>" % (
            self.cssclass_month_head, s)


    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """

        events = Event.objects.filter(day__month=themonth)

        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week,theyear,themonth, events))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)
