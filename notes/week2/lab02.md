# Lab02 : Core Shell & Shell Scripting
用sh和py分别实现了具有相同功能的PhoneBook
---
## phoneBook主要功能
1. 增加新的联系人
- 支持添加联系人的`name`和`phone_number`
- 可以重复添加姓名相同的联系人
- 使用文件`phonebook_entries`每一行存储一位联系人
- `./phonebook new <name> <number>` 使用`echo`和`>`在文件后面追加
2. 查看所有联系人
- 打印文件中所有联系人的姓名和电话
- `./phonebook list`,使用`cat`直接打印文件的内容
3. 删除联系人
- 根据名字将与该名字关联的联系人全部删除
- `./phonebook remove <name>`，使用`sed -i pattern file`删除file中与pattern匹配的行 
4. 查找联系人电话
- 根据名字查找联系人的电话号码
- `./phonebook lookup <name>`使用`grep`查找匹配的行
5. 删除所有联系人
- `./phonebook clear`