用于合成cuffs系（Cuffs, Sphere, CUBE, mintCUBE, Sonora; 有名字不代表可以使用，具体自行测试）以及HULOTTE社，使用krkr引擎的较新作品的CG和立绘合成。  
建议和[KrkrExtract](https://github.com/xmoeproject/KrkrExtract) 或[GARbro](https://github.com/morkt/GARbro) 配合使用。  
本质是汉化工作的副产物，大概不怎么会更新。  
## 更新
* 230326 CUBE新作将large size的CG改为jpg格式，修改了代码以支持不同文件格式的图片合成  
* 230326 将合成结果改为有透明通道的png格式
* 230326 测试了更多游戏
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
会自动依照目录下的csv文件（.csv）和.tlg文件转换后的.png文件（.tlg.png）或.jpg文件（夏ノ終熄之后的CUBE作品，large size的CG为jpg格式）合成，合成结果在pic_out文件夹内
## 已知可用游戏
* [CUBE][200327] 神様のような君へ
* [CUBE][220325] 神様のような君へ Extended Edition
* [CUBE][220527] ネコと女子寮（ワカイ）せよ！
* [CUBE][220826] 夏ノ終熄
* [CUBE][221125] サメと生きる七日間
* [Sonora][201127] 響野さん家はエロゲ屋さん！
* [Sonora][211126] ウチはもう、延期できない。
* [HULOTTE][200327] 俺の姿が、透明に！？ 不可視の薬と数奇な運命
* [HULOTTE][210924] 俺の恋天使がポンコツすぎてコワ～い。

## 注意事项
* ~~合成出来是没有透明通道的，懒得改了，需要透明通道的立绘自己转换一下。~~ 已经修改为有透明通道了  
* 没有技术力，欢迎issue和pr，大佬们见笑了  
