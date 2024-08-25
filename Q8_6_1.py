from detetime import detetime
t = '20180105120130'
dt = datetime.strptime(t, "%Y%m%d%H%M%S")
print(dt)
print(dt.strftime("%Y%m%d%H%M%S"))

