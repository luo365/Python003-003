学习笔记
1. 因为之前学过pandas，所以这次作业做得快；
2. 工作还是要靠平时积累，如果没有学过，直接上课，整个过程很辛苦，一周10个小时都打不住；
3. 补充一个老师提到替换字符串内容，使用map会更快：  
```python
list(df['status']) = ['announced', 'cancelled’,…]
status_map = {
    'announced':'筹建',
    'cancelled':'取消’,..}

df.replace({'status': status_map}) 
#4.47 ms ± 288 µs per loop   100 loops each

df['status'].map(status_map)
#1.42 ms ± 16 µs per loop     1000 loops each
```
4. 平时要多做笔记，replace 和 map 就是之前的笔记。