import sys
import csv
class LogAnalyzer:
    def __init__(self,log_file):
        self.log_file = log_file
    def report_file(self):
        with open("report.csv","w") as csv_file:
            content = csv.writer(csv_file)
            content.writerow(["LogLevel","Count"])
            content.writerow(["ERROR",self.error_count])
            content.writerow(["WARNING",self.warning_count])
    def analyze_log(self):
        self.error_count = 0
        self.warning_count = 0
        try:
            with open(self.log_file,"r") as file:
                for reader in file:
                    main_area = reader.split(":")[0].strip()
                    if main_area == "WARNING":
                        self.warning_count +=1
                    elif main_area == "ERROR":
                        self.error_count +=1
                    else:
                        pass
            myobj.report_file()
        except Exception as e:
            print(e)
            print("Sorry this file cannot found in this directory")

 
myobj = LogAnalyzer(sys.argv[1])
myobj.analyze_log()

                    


    