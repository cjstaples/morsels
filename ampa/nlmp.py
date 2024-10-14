# nlmp.py

from datetime import datetime
from dateutil import parser, tz
from dateutil.relativedelta import relativedelta

BD_TB = "="
BD_EDGE = "###"
NLMP_DATE = parser.parse("Jan 2, 2025 2:00 PM")
NLMP_DATE = NLMP_DATE.replace(tzinfo=tz.gettz("America/New_York"))


def time_amount(time_unit: str, countdown: relativedelta) -> str:
    t = getattr(countdown, time_unit)
    return f"{t} {time_unit}" if t != 0 else ""


def main():
    now = datetime.now(tz=tz.tzlocal())
    time_remaining = relativedelta(NLMP_DATE, now)
    # time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
    time_units = ["years", "months", "days", "hours"]
    output = (t for tu in time_units if (t := time_amount(tu, time_remaining)))
    separation_date = NLMP_DATE.strftime("%A, %B %d, %Y at %H:%M %p %Z")
    print( BD_EDGE + "   " + BD_TB * 20 +"   NL*MP   "+ BD_TB * 20 +"   " + BD_EDGE )
    print( BD_EDGE + "   " + separation_date)
    print( BD_EDGE + "   " + ", ".join(output))
    print( BD_EDGE + "   " + BD_TB * 20 +"   NL*MP   "+ BD_TB * 20 +"   " + BD_EDGE )


if __name__ == "__main__":
    main()
