# 浏览量统计
1. 安装依赖
```shell
pip install -r requirements.txt
```

2. 运行后端
```shell
bash run.sh
```

3. 在js中call后端api
- POST：http://127.0.0.1:5000/ 会增加一个浏览量，返回当前总浏览量
- GET：http://127.0.0.1:5000/ 只返回当前总浏览量

api调用参考[index.html](./index.html)
