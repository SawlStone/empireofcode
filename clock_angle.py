# https://github.com/Empire-of-Code-Puzzles/checkio-empire-clock-angle

def clock_angle(time):
    hour = time.split(' ')[0].split(':')[0]
    minute = time.split(' ')[0].split(':')[1]
    if hour[0] == '0':
        hour = hour[1]
    if minute[0] == '0':
        minute = minute[1]
    angle = abs(360/12*int(hour)+0.5*int(minute)-360/60*int(minute))
    if angle > 360:
        return -(360 - angle)
    return 360 - angle if angle > 180 else angle


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
