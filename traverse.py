import os
import datetime
import reviewFile
from config import FILE_TO_IGNORE, DIR_TO_IGNORE




# Start with an entrypoint and traverse all the related files



# Scan all the files in the directory and its subdirectories
def traverse_directory(path, ignore_folders=[], ignore_files=[]):
    for root, dirs, files in os.walk(path):
        # Exclude specified folders
        dirs[:] = [d for d in dirs if d not in ignore_folders]

        # Format the date and time as yyyy-mm-dd-hh-mm-ss
        report_path = f'reports/{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'

        allReports = ""

        for file in files:
            if file not in ignore_files and file not in ignore_folders:
                print(f"Processing {file}, which is NOT present in {ignore_files}...")
                file_path = os.path.join(root, file)
                report = reviewFile.evaluateCodeFile(file_path)
                if report == None:
                    print(f"Report is None, skipping {file_path}...")
                    continue
                report = f" ========= Code Security Report ========= \n\nCode file evaluated: {file_path}\n\n" + report + "\n\n"
                # "Code file evaluated: " + file_path, end="\n\n"
                allReports += report

                # write the report to a file
                writeToFile(report_path, f"code_security_report.md", report)
                # writeToFile(report_path, f"code_security_report-{os.path.basename(file_path)}.md", report)
                print("\n\n>> Report Saved to reports/code_security_report-" + os.path.basename(file_path) + ".md", end="\n\n")

        # summarize the reports
        report = reviewFile.summarizeReports(allReports)
        # write the summary report to a file
        print("\n\n >> Report Summary Saved to reports/" + ".md", end="\n\n")
        writeToFile(report_path, f"Summary_report.md", report)


def writeToFile(dir_path, file_name, content):
    if(content == None):
        print("Content is None")
        return
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, file_name)
    file = open(file_path, "a")
    file.write(content)
    file.close()



def main():
    path = input("Enter the path of the directory: ")
    traverse_directory(path, ignore_folders=DIR_TO_IGNORE, ignore_files=FILE_TO_IGNORE)

main()