def add_time(start, duration, startingDay=None):
    if startingDay != None:
        startingDay = startingDay.lower()

    nextPeriod = {
        "PM": "AM",
        "AM": "PM",
    }
    [startingHour, startingMinutes, startingPeriod] = parseStartDate(start)
    [durationHour, durationMinutes] = parseDurationDate(duration)

    [leftoverHours, resultMinutes] = calculateMinutes(startingMinutes, durationMinutes)
    [resultDays, resultHours, changePeriod] = calculateHours(
        startingHour, durationHour, leftoverHours, startingPeriod
    )
    period = startingPeriod.upper()
    if changePeriod != 0:
        period = nextPeriod[startingPeriod.upper()]
    dayText = ""
    if resultDays == 1:
        dayText = " (next day)"
    elif resultDays > 1:
        dayText = f" ({resultDays} days later)"

    return f"{formatHours(resultHours)}:{formatMinutes(resultMinutes)} {period}{getDay(resultDays,startingDay)}{dayText}"


def getDay(resultDays, startingDay):
    if startingDay == None:
        return ""

    days = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }
    days2 = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    thisDay = days[startingDay.lower()]
    return f", {days2[(thisDay + resultDays) % 7]}"


def formatHours(resultHours):
    if resultHours < 10:
        return f"{resultHours}"
    return f"{resultHours}"


def formatMinutes(resultMinutes):
    if resultMinutes < 10:
        return f"0{resultMinutes}"
    return f"{resultMinutes}"


def calculateHours(startingHours, durationHours, leftoverHours, startingPeriod):
    try:
        extraHalf = 0
        if startingPeriod.upper() == "PM":
            extraHalf = 12
        hours = int(startingHours) + int(durationHours) + int(leftoverHours)
        resultDays = (hours + extraHalf) // 24
        changePeriod = (hours // 12) % 2
        resultHours = hours % 12
        if resultHours == 0:
            resultHours = 12

    except ValueError:
        print("Wrong Input - Hours")

    return resultDays, resultHours, changePeriod


def calculateMinutes(startMinutes, durationMinutes):
    try:
        minutes = int(startMinutes) + int(durationMinutes)
        hours = minutes // 60
        minutes = minutes % 60

    except ValueError:
        print("Wrong Input - Minutes")

    return hours, minutes


def parseStartDate(start):
    splittedStarting = start.split(":")
    splittedStarting += splittedStarting[1].split(" ")
    return splittedStarting[0], splittedStarting[2], splittedStarting[3]


def parseDurationDate(duration):
    splittedDuration = duration.split(":")

    return splittedDuration[0], splittedDuration[1]
