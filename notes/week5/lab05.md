# Lab05: Introduction to Networking
## 1. 了解一些基础概念
- MAC
- IP
- ARP
- DNS
- TCP/UDP
- Port
---
## 2. 熟悉系统命令（Sysadmin Commands）
1. `hostname`
查看或临时设置本机的主机名及 IP 地址。
2. `ping`
发送 ICMP 回声请求测试网络连通性和延迟。
3. `traceroute`
追踪数据包到达目标主机所经过的路由跳数。
4. `arp`
查看或修改本机的 ARP 缓存（IP 地址与 MAC 地址的映射表）。
5. `dig`
执行高级 DNS 查询，获取域名的各种记录（如 A、MX、NS）。
6. `ip`
取代 ifconfig 的现代工具，显示并配置网络接口、路由、隧道等。
7. `curl` 
通过 URL 传输数据，支持 HTTP、FTP 等数十种协议（常用于 API 测试）。
8. `wget`
非交互式下载文件，支持递归、断点续传和后台下载
9. `netstat`
显示网络连接、路由表、接口统计及监听端口。
10. `nc`
网络工具箱中的“王者”，可读写 TCP/UDP 连接、端口扫描或传输文件。
---
## 3.回答下列问题
1. Does HTTP use TCP or UDP and why? How about Discord and Skype, why?
- **HTTP 使用 TCP，原因如下：**
    - 网页传输要求数据完整、有序（不能丢失或乱序）。
    - TCP 提供可靠连接、确认重传、顺序保证，适合网页、图片、API 数据等。
    - HTTP/3 虽然基于 UDP（通过 QUIC 协议），但传统 HTTP/1.1 和 HTTP/2 均使用 TCP。

- 语音/视频通话使用 UDP（RTP 协议），因为实时性要求高，少量丢包可以容忍，但延迟要低。
- 文本聊天、文件传输、登录等控制信令使用 TCP，因为需要可靠传输。
2. Who manufactured the NIC with mac address dc:fb:48:21:7b:23?
该 NIC 由 惠普企业/Aruba 制造。
3. How many distinct hosts can 127.0.0.0/8 contain?
- `127.0.0.0/8` 是 回环地址块，共 `2^(32-8) = 2^24 = 16,777,216` 个 IP。
- 但有效可用主机数也是 16,777,216（理论上全部可用）。
- 然而，通常只使用 127.0.0.1，其他地址虽能分配，但一般不用于实际通信
4. What are three types of records you can get when you perform a DNS lookup of google.com using the dig command?
常见三种记录类型：
- A：IPv4 地址（如 142.250.185.46）
- AAAA：IPv6 地址
- MX：邮件交换服务器（如 alt4.aspmx.l.google.com）
其他还有 NS（域名服务器）、TXT（文本记录）、CNAME（别名）等。
5. Is the result of running ping enough to determine whether or not you can reach a server? Why or why not?
不一定足够，原因如下：
- ✅ 能 ping 通	说明网络层（IP）可达，但应用层服务可能没开（如 Web 端口 80 被防火墙阻止）。
- ❌ ping 不通	不代表服务不可达，可能只是禁用了 ICMP 回应（很多服务器防火墙会屏蔽 ping）。
---
## 4. 练习
编写 `is_on.sh` 与 `mac.sh`
1. `is_on.sh` —— 检查主机是否在线
**目标：**
- 输入一个主机名/IP，ping 一次。
- 成功 → 输出 OK
- 失败 → 输出 Host is not reachable
- 不输出任何其他内容。
**关键知识点：**
- ping -c 1 ：只发一个包。
- ping 的返回值（退出码）：
    - 0 表示成功收到回复
    - 非 0 表示失败（超时、不可达等）
- `> /dev/null 2>&1` ：隐藏所有输出。
- `if` 判断 `$?` ping的退出状态码。
2. `mac.sh` —— 从 ip 命令提取 ens3 的 MAC 地址
**目标：**
- 使用 `ip` 命令获取网络接口 ens3 的信息
- 通过 `head / tail / cut` 精确提取 MAC 地址。
- 最终脚本可写成一行: `ip link show eth0 | head -n 2 | tail -n 1 | cut -c 16-32`
