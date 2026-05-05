from datetime import datetime

now = datetime.now()
a = datetime(1970, 1, 1, 00, 00, 00)
time_diff = (now-a).total_seconds()

print(f"Seconds since January 1, 1970: {"{:,}".format(time_diff)} or \
        {"{0:.2E}".format(time_diff)} in scientific notation")
print(now.strftime("%b %d %Y"))
