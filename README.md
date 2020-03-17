# entry
实现类桌面应用的网页版程序, exe可执行程序的自动启动文件。
1. python + subprocess + win32 + webbrowser
2. 实现用entry来启动exe程序的步骤：
  1. 将xx.exe,以及所依赖的static,templates,logo.ico等复制到entry项目dist文件夹下。
  2. 修改entry项目Config.py文件中
    PORT->       xx.exe程序的端口
    PROCESS_ID-> 进程ID即xx.exe
    ARGS->       xx.exe的路径
    ROOT_URL为-> xx.exe的URL
