from log_source_factory import LogSourceFactory

# เปลี่ยนตรงนี้ได้ว่าอยากอ่านแบบไหน
source = LogSourceFactory.create("csv", "log.csv")

logs = source.read_logs()   

for log in logs:
    print(log)