# Processes and Services
## Part1：using systemed
1. 使用`systemctl`命令，熟悉了如何开启，控制，结束服务
- systemctl status [name]: Check the detailed status of a service.
- systemctl start [name]: Starts a service.
- systemctl stop [name]: Stops a service.
- systemctl restart [name]: Restarts a service.
- systemctl enable [name]: Sets a service to start automatically on boot.
- systemctl disable [name]: Prevents a service from starting on boot.
- systemctl reload [name]: Reload a service’s configuration.
2. 通过unit文件，实现了一个简单的服务
unit文件内容包括：
- [Unit]
- [Install]
- [Service]
3. 回答了以下问题：
### Question 1： What is the name of a systemd service running on your system? What does it do? 
**Answer:** `ssh.service`能够提供远程登陆，加密通信，文件传输以及远程管理服务器等功能
### Question 2: What is the difference between `systemctl reload yourservice` and `systemctl restart yourservice`?
**Answer:** 
- reload
让服务重新加载配置文件，但不中断正在进行的服务进程。
服务会平滑地应用新配置，适用于支持热加载的服务（如 Nginx、Apache、sshd）。
优点：不停机，对正在处理的请求影响小。
- restart
会完全停止服务，再重新启动，所有进程、连接、临时状态都会被清空。
会导致短暂的服务中断，适用于需要彻底重置或服务不支持 reload 的情况。
优点：确保配置完全生效，清除异常状态。
---
## Part 2 : Processes
掌握了几个查看进程的命令以及关于进程的概念：
- `ps -ef`
- `htop`
-
- 所有进程都来自于`/sbin/init`进程
- `Orphan Processes`: 父进程已经终止，但子进程仍在运行。这些子进程会被 init 进程（PID=1） 或 systemd（PID=1） 收养。
- `Zombie Processes`: 子进程已终止，但父进程尚未调用 wait() 或 waitpid() 来读取子进程的退出状态，导致子进程的进程描述符仍然保留在系统中。
- `Daemon Processes`: 在后台运行、脱离终端控制、通常随系统启动而启动的系统服务进程。
- 僵尸进程：已死但没被收尸（父进程的错）
- 孤立进程：爹死了，被孤儿院（init）收养
- 
守护进程：故意孤儿化，在后台默默工作的系统仆从