# 100knock2015
http://cl.sd.tmu.ac.jp/groups/programming-drill

## 概要
東北大学乾・岡崎研究室で作成された[言語処理100本ノック][]を用い、プログラミングの演習を行ないます。  
言語は1回目の人は Python、2回目の人は Python 以外を用います。  
参加者は全員毎回課題を解いて、このリポジトリにプッシュしておいてください。  
gitって何？？？？→[Git使い方講座][]  

[言語処理100本ノック]: http://www.cl.ecei.tohoku.ac.jp/nlp100/
[Git使い方講座]: http://ace12358.tumblr.com/post/116453885344/git-for

## リポジトリについて
各人自分のディレクトリを作ってその中にコミットしてください。  
課題に必要なデータはコミットしなくてよいです。  
基本的に各人自分のブランチを作って作業をして、各章の課題をコミットし終えたらdevelopブランチにマージしてください。勉強会の直前にTAがmasterにマージします。  

具体例：  
![my_git_flow](https://github.com/tmu-nlp/100knock2015/blob/master/img/my_git_flow.png)

##他のリポジトリで管理している人
* [叶内　晨](https://github.com/shin-kanouchi/NLP100knock2015)
* [張 培楠](https://github.com/peinan/NLP100DrillExercises2015)

## コマンド説明
必要になりそうなコマンドをここに説明しておきます。  
<>で囲ってる部分は適宜適当な名前にしてください。(<>自体の入力は不要です。例：`<name_Nset>` -> `ryosuke_1set`)  


今自分がいるブランチがどこなのか意識してください。  
**masterブランチにいたら絶対にコミットしないで！！**  


### 一連の流れ  
#### 章の始め
ローカルのdevelopブランチを最新状態に更新  
現在のブランチがdevelopであることを確認しつつ  
`git fetch`  
`git merge origin/develop`  
developブランチから新しく自分のブランチに分岐（ブランチを切る）  
`git branch <name_Nset>`  
今作ったブランチに移動  
`git checkout <name_Nset>`  
作ったブランチを追跡ブランチにしてリモートにpush  
`git push -u origin <name_Nset>`  

#### 章の間
自分のブランチにいることを確認しつつ、コードカキカキ  
コード書いたら、リポジトリに変更履歴を保存  
`git add <file_name>`  
`git commit -m "<message>"`  
リモートにも反映  
`git push`  

#### 章の終わり
ローカルのdevelopブランチを最新状態に更新  
developブランチにいることを確認しつつ  
`git fetch`  
`git merge origin/develop`  
developブランチにさっきまで作業してた自分のブランチをマージ  
`git merge --no-ff <name_Nset>`  
なんかvimの画面がでてくるけど`:wq`で終了（マージするときのコミットメーセージを入力する画面です）  
リモートにも反映  
`git push`  
次の勉強会開始まで待機  
勉強会終わったら章の初めから繰り返し  
<br>

##### ちなみに
いらなくなった過去のブランチは消せます  
第2章のコード書いてる時に第1章のときのブランチとかもう不要ですよね  
章終わり or 章始めに 古い自分のブランチを削除しちゃっておｋです  
ローカルのブランチの削除  
`git branch -d <name_Nset>`  
リモートのブランチも削除（**自分以外のは勝手に消さないでね！**  ）
`git push origin :<name_Nset>`
<br>

##### ちなみにちなみに
他の人のディレクトリとか手元に置きたくない人   
`git config core.sparsecheckout true`  
`echo "<my_dicetory_name>" > .git/info/sparse-checkout`  
`git read-tree -m -u HEAD`  
と設定すると、設定したディレクトリのみが作業ディレクトリに存在するようになります  
（実際にはリポジトリには存在するけど、ワーキングツリーから消えるだけです）  
この状態でマージとかプッシュとかプルとかもちゃんとできます（はずです）    

  
### その他使いそうなコマンド一覧
#### ブランチ関連
ブランチ一覧  
\*のマークが付いているブランチが現在自分がいるブランチ  
`git branch -a`    
追跡ブランチの表示  
`git branch -vv`  
ブランチの作成  
`git branch <branch_name>`  
ブランチへの切り替え   
`git checkout <branch_name>`  
現在のブランチへ`<branch_name>`をマージ  
`git merge --no-ff <branch_name>`  



#### ローカルのリポジトリに変更を更新する
`git add <file_name>`  
`git commit -m "<message>"`  


#### リモート(つまりGitHub)にローカルの最新状況を更新する
リモートの設定  
`git remote add origin git@github.com:<name>/<repository>.git`  
リモートの確認  
とりあえず origin が表示されてればおｋ、されてなければ上のリモートの設定をする
`git remote`  
ローカルのブランチを新しくpush（追跡ブランチの設定をしつつ）  
`git push -u origin <branch_name>`  

追跡ブランチの設定が終わってる場合のpush  
`git push`  
もしなにかエラーがあったりしたら（エラーの文は一応読んでね）、恐らくリモートの方がローカルよりも最新だよってエラーだと思うので  
`git fetch`  
`git merge origin/<branch_name>`  
これでリモートの最新状況をローカルに更新する、そしたらもう一度push  
