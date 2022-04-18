用于合成cuffs系（Cuffs, Sphere, CUBE, mintCUBE, sonora; 有名字不代表可以使用，具体自行测试）以及HULOTTE社，使用krkr引擎的较新作品的CG和立绘合成。  
建议和[KrkrExtract](https://github.com/xmoeproject/KrkrExtract) 或[GARbro](https://github.com/morkt/GARbro) 配合使用。  
本质是汉化工作的副产物，大概不怎么会更新。  
## requirements  
安装Python3环境，随后在命令行运行
```
pip install opencv_python
```
## 使用方式  
以KrkrExtract解包结果为例。
解包（TLG Image处勾选PNG），将文件放置在需要需要合成的目录，然后打开命令行，运行
```
python main.py
```
会自动依照目录下的csv文件（.csv）和.tlg文件转换后的.png文件（.tlg.png，如不是此格式自己修改代码）合成，合成结果在pic_out文件夹内
## 已知可用游戏
* [200327][CUBE] 神様のような君へ
* [220325][CUBE] 神様のような君へ Extended Edition
* [201127][Sonora] 響野さん家はエロゲ屋さん！
* [211126][Sonora] ウチはもう、延期できない。
* [210924][HULOTTE] 俺の恋天使がポンコツすぎてコワ～い。
## 注意事项
* 合成出来是没有透明通道的，懒得改了，需要透明通道的立绘自己转换一下  
* 没有技术力，欢迎issue和pr，大佬们见笑了  
