# Git 与代码版本管理实践笔记
24级 读书实践周 Git 实践任务

## 一、学习资料来源
1. Git 官方文档：https://git-scm.com/doc
2. 菜鸟教程 Git：https://www.runoob.com/git/git-tutorial.html
3. Gitee 帮助中心：https://help.gitee.com/

## 二、实践流程
1. 安装 Git 并配置全局用户信息
git config --global user.name "你的姓名"
git config --global user.email "你的邮箱"

2. 创建本地仓库
mkdir git-practice
cd git-practice
git init

3. 关联远程仓库（Gitee/GitHub）
git remote add origin 你的仓库地址

4. 提交并推送代码
git add .
git commit -m "提交说明"
git push -u origin main

## 三、三次提交说明
1. 第一次提交：init
- 初始化仓库
- 创建 README.md 初稿
- 搭建项目基础结构

2. 第二次提交：add-note
- 添加 Git 学习笔记 git_note.md
- 记录基础命令与操作步骤

3. 第三次提交：update-readme
- 完善 README 全部内容
- 补充问题与解决方法
- 整理学习心得

## 四、遇到的问题及解决方法
1. 问题：git push 报错 remote origin already exists
解决：先删除原有远程地址
git remote remove origin
再重新关联新仓库

2. 问题：提交时提示 nothing to commit
解决：文件未加入暂存区，先执行 git add . 再提交

## 五、学习心得
通过本次实践，我掌握了 Git 安装、配置、仓库创建、提交、推送等基础操作，理解了版本管理的作用。Git 能清晰记录每一次修改，方便回溯与协作，是编程学习必备技能。后续会继续学习分支、合并、回退等高级功能，提升工程化开发能力。