# Lab06: Web Servers
## 回答下列问题
### Which networked services are already running
1. Which networked services are already running?
`netstat -tulpn`

2. Choose one service from the output and describe what it does.
以 sshd 为例：它是 SSH 守护进程，监听 22 端口，允许用户通过 SSH 协议远程安全登录到这台虚拟机。
---
### DNS
3. What is the systemctl command to show whether bind9 is running or not?
`sudo systemctl status bind9`

4. Why does the dig command (dig ocf.berkeley.edu) work if @localhost is not present at the end (if bind9 is not started) but times out when @localhost is added?
不加 `@localhost` 时，`dig` 会向 `/etc/resolv.conf` 中配置的外部 DNS 服务器（如 8.8.8.8）发送请求，这些服务器一直在运行所以能成功；加上 @localhost 则是向本机尚未启动的 DNS 服务（127.0.0.1:53）发送请求，没有程序监听所以超时。
5. What additional entries did you add to your DNS server config (the db.example.com file)?
在 `/etc/bind/db.example.com` 末尾添加了：
`test IN A <虚拟机IP地址>`
6. What commands did you use to make requests to the local DNS server for your additional entries?
`dig test.example.com @localhost`
---
### Load Balancing
7. Do you notice any pattern when you refresh the page multiple times?
每次刷新页面时，请求会按固定顺序轮流分配给不同的后端服务器（例如 server1、server2、server3 依次循环），呈现出轮询的访问模式。

8. What load balancing algorithm are you using?
使用的是 roundrobin（轮询）算法，该算法会将请求按顺序轮流分配给每个后端服务器。
9. What do you notice has changed on the stats page after adding health checks? What color are each of the servers in the backend now?
添加健康检查后，状态页会显示每台服务器的健康状态，所有正常运行的服务器都显示为 绿色（UP）。
10. What changes in the stats page when you crash a worker? What happened to the pattern from before?
崩溃的服务器在状态页中变为 红色（DOWN）；刷新页面时，请求模式会发生变化，流量只分配给仍为绿色的健康服务器，崩溃的服务器不再接收请求。
11. What HTTP status code (or error message) does HAProxy return if you crash all of the workers?
HAProxy 返回 503 Service Unavailable 错误，表示没有可用的服务器来处理请求。

