## Thunders

迅雷非官方批量下载SDK。

感谢使用。


## 快速入门
### 创建批量自定义任务

```python
from thunders import Task, GroupTask

group_task = GroupTask(name="test")
group_task.append(Task("https://ahamega.com/1.mp4"))
group_task.append(Task("https://ahamega.com/2.mp4", name="自定义重命名2.mp4"))
group_task.run()   # 执行完后，迅雷会打开并弹出上面创建的批量任务，点击下载即可

# 也可以这么用
group_task.extend([
    Task("https://ahamega.com/1.mp4"),
    Task("https://ahamega.com/2.mp4", name="自定义重命名2.mp4")
])
group_task.run()   # 执行完后，迅雷会打开并弹出上面创建的批量任务，点击下载即可

```
