# 100knock2015
http://cl.sd.tmu.ac.jp/groups/programming-drill

## 概要
東北大学乾・岡崎研究室で作成された[言語処理100本ノック][]を用い、プログラミングの演習を行ないます。  
言語は1回目の人は Python、2回目の人は Python 以外を用います。  
参加者は全員毎回課題を解いて、このリポジトリにプッシュしておいてください。  

[言語処理100本ノック]: http://www.cl.ecei.tohoku.ac.jp/nlp100/

## リポジトリについて
各人自分のディレクトリを作ってその中にコミットしてください。  
課題に必要なデータはコミットしなくてよいです。  
基本的に各人自分のブランチを作って作業をして、各章の課題をコミットし終えたらdevelopブランチにマージしてください。勉強会の直前にTAがmasterにマージします。  

##他のリポジトリで管理している人
* [叶内　晨](https://github.com/shin-kanouchi/NLP100knock2015)
* [張 培楠](https://github.com/peinan/NLP100DrillExercises2015)

## コマンド説明
必要になりそうなコマンドをここに説明しておきます。  

### ブランチ関連
今自分がいるブランチがどこなのか意識してください。  
**masterブランチにいたら絶対にコミットしないで！！**  


ブランチ一覧  
\*のマークが付いているブランチが現在自分がいるブランチ  
`git branch -a`    
追跡ブランチの表示  
`git branch -vv`  
testブランチの作成  
`git branch test`  
testブランチへの切り替え   
`git checkout test`  
現在のブランチへtestブランチをマージ  
`git merge --no-ff test`  



### ローカルのリポジトリに変更を更新する
`git add <file_name>`  
`git commit -m "<message>"`  


### リモート(つまりGitHub)にローカルの最新状況を更新する
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
`git pull`  
これでリモートの最新状況をローカルに更新する、そしたらもう一度push  

### 各章の終わりとはじめにやりそうな一連の流れ  
#### 章の始め
developブランチから新しく自分のブランチに分岐（ブランチを切る）  
現在のブランチがdevelopであることを確認しつつ  
`git branch <ryosuke_3set>`

  
