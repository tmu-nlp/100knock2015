## 概要
このリポジトリに参加してコードを書き始めるまでのチュートリアルです.    
以下の画像の"第一章の始め"まで準備する手順を説明します.この画像を見ながらやるともしかしたらわかりやすいかもしれません.  
![my_git_flow](https://github.com/tmu-nlp/100knock2015/blob/master/img/my_git_flow.png)


## 手順
#### リポジトリのクローン
* 作業するディレクトリに移動する  
もし`/Users/ryosuke/work/100Knock2015/`で作業したければ, `/Users/ryosuke/work`に移動する  
* まずはこのリポジトリをクローン  
`git clone git@github.com:tmu-nlp/100knock2015.git`  
これで今いるディレクトリに`100Knock2015`というディレクトリができる, そこがローカルのリポジトリ  
* 今クローンしたディレクトリに移動  
`cd 100Knock2015`  


#### 自分のブランチの作成
* 現在のブランチを確認  
`git branch -a`  
恐らくmasterが一つとremotes/origin/みたいのがいっぱいあるはず  
つまりローカルにはmasterブランチのみ, リモートにはたくさんのブランチがあるということ  
* developブランチをもってくる  
`git checkout -b develop origin/develop`  
これでリモートからdevelopブランチをもってこられた  
* もう一度ブランチの確認  
`git branch -a`  
現在のブランチがdevelopになっているはず（*記号で示されているのが現在のブランチ）  
* developブランチから自分用のブランチを切る（作る, 枝分かれさせるという意味）  
`git branch <name_Nset>`  
`<name_Nset>`の部分は自分で決めた名前を入れてください, ryosukeの場合は  
`git branch ryosuke_1set`  
これでブランチを作成できた（`git branch -a`で確認すればあるはず）  
* 作ったブランチに移動  
作っただけではまだdevelopブランチにいるままなので, 作ったブランチに切り替える  
`git checkout <name_Nset>`  
この`<name_Nset>`も先ほどと同じ名前を入れてください  
`git branch -a`で確認すると現在のブランチが変わってるはず  
* 自分の作業用ディレクトリの作成  
ここまでの手順でブランチが切り替わったことを確認したら, 自分の作業用ディレクトリを作る  
`mkdir <name>`  
これもryosukeなら  
`mkdir ryosuke`  


ここまでで, "第一章始め"までの準備は終わりです.  
最後の手順で作成したディレクトリ(ryosukeなら`ryosuke`ディレクトリ)の中に課題を解いて, 適宜 `add`, `commit`, (`push`)しておいてください.  
それ以降の作業は次の勉強会で説明します.  
