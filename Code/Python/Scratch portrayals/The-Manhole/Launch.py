# -*- coding:utf-8 -*-
print("Make sure to have webview installed.")

try:
    import webview
    window = webview.create_window('The Manhole: New and extended', 'readme.html')
    webview.start()
except Exception as exception:
    print(f"Something went wrong:\n{exception}")
    crash_file = open("crash_traceback.log", "w")
    crash_file.write(str(exception))
    crash_file.close()

    exit(1)
