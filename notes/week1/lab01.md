# Lab 1 - Unix, the Shell, OSS
**Table of Contnets**
- Part 1: Shell spelunking
- Part 2: General Questions
---
## part1
**熟悉了一些基本命令**，如`ssh`, `tar`, `pwd`, `cat`, `grep`, `rm`, `chmod`, `echo`, `重定向`等
- chmod
  - 基本用法： chmod 755 file
  - 7 = rwx
  - 6 = rw-
  - 5 = r-x
  - 4 = r--
  - 3 = -wx
  - 2 = -w-
  - 1 = --x
  - 0 = ---
  - 添加权限：chmod +x file
- grep
  - 功能：打包，解包
  - 基本用法：`grep  "hello"  file.txt`
  - 常用参数：
    - -n：显示行号
    - -i：忽略大小写
    - -r：递归搜索
    - -E：正则表达式
    - -B：显示上面n行
- tar
  - 功能：搜索文本
  - 基本用法：
    - 打包：`tar -czf file.tar.gz folder/`
    - 解压：`tar -xzf file.tar.gz`
  - 常用参数：
    - -c：创建
    - -x：解压
    - -z：gzip
    - -f：指定文件
- ssh
  - 功能：远程登录
  - 基本用法：`ssh user@host`, `ssh -p port_number user@IP`
  - 常用参数：
    - -c：创建
    - -x：解压
    - -z：gzip
    - -f：指定文件
- 重定向
  - `echo "hello" > file.txt`       # 覆盖
  - `echo "world" >> file.txt`     `# 追加
---
## part2
**一些常见问题**
1. What differentiates Linux/OSX from operating systems like Windows?
> Linux 和 macOS（OSX）与 Windows 的主要区别在于其设计理念、系统架构和使用方式：
> - 内核与架构
>    - Linux/macOS：基于 Unix 或类 Unix（POSIX 标准）
>    - Windows：基于 Windows NT 内核（非 Unix）
> - 文件系统结构
>    - Linux/macOS：统一从 /（根目录）开始的树状结构
>    - Windows：使用多个盘符（C:, D: 等）
>- 大小写敏感
>   - Linux/macOS：区分大小写
>   - Windows：默认不区分大小写
>- 软件管理
>   - Linux：使用包管理器（apt、yum）
>   - macOS：brew 等工具
>   - Windows：主要依赖安装程序（.exe/.msi）
>- CLI 使用
>   - Linux/macOS：命令行是核心工具
>   - Windows：以 GUI 为主（CLI 次要）

2. What are some differences between the command line and normal (graphical) usage of an OS?
> 命令行（CLI）与图形界面（GUI）的主要区别：
> CLI（命令行）
> - 通过文本命令操作系统
> - 可脚本化、自动化
> - 更高效（尤其是批量任务）
> - 可远程使用（SSH）
> - 学习成本较高
> GUI（图形界面）
> - 通过窗口、按钮、图标操作
> - 更直观、易上手
> - 适合普通用户
> - 不适合复杂或重复操作
> - 自动化能力弱
> 👉 核心区别：
> - CLI = 精确控制 + 自动化
> - GUI = 易用性 + 可视化

3. What is the root directory in Linux filesystems? 
> 在 Linux 中，根目录 / 是整个文件系统的起点，所有文件和设备都组织在它下面，比如 /home、/etc 等，所有存储设备也会挂载到这个目录树中。


4. Briefly, what is the difference between permissive and copyleft licenses?
> 两者的核心区别在于对衍生作品的限制程度
> - Permissive License（宽松许可）
>   - 允许自由使用、修改、再发布
>   - 可以闭源
>   - 限制最少
> - Copykeft License（强制开源许可）
>   - 允许修改和使用
>   - 但衍生作品必须开源
>   - 必须使用相同许可证
> - 👉 一句话总结：
>   - Permissive：想怎么用都行
>   - Copyleft：可以用，但必须继续开源

5. Give an example of a permissive license. Give an example of (a) open-source software and (b) free, but closed-source software that you use.
> 一个典型的 permissive license 是 MIT License。开源软件的例子有 Linux 或 Git，而免费但闭源的软件，比如 Google Chrome 或 Zoom