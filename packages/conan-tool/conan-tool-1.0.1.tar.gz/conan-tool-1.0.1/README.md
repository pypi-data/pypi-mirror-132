
## 问题排查

绘制图形
[gprof2dot](https://github.com/jrfonseca/gprof2dot)

```bash
#安装依赖
yum install -y graphviz
#绘制图形
gprof2dot -f pstats cp.prof |dot -Tpng -o cp.png
```

