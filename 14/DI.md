## DIについて
- インスタンスの注入のこと
- たとえば図形と円、三角形があったとする。clientが円をnewして使う
  - このnewしてくれるadapter的なクラスを使うのがFactory pattern
- 楕円が最初factoryのインターフェースごしに、clientがモックfactoryを読んでいた
- 実装が終わった時に、つけかえる。DIを使う
- Factory使う人（client）に対して、Factoryを渡してあげる
- 使うインスタンスの生成を内部から外部にもっていくこと


## DIコンテナ
- フレームワークにDIコンテナがいて、インスタンスの管理をする
  - システムに1つ
  - singletonモードと都度作るモードがある
- CSVのインスタンスとかはDIコンテナで使いまわせる！すごい
- 静的なのは普通のクラスでよくて、動的にかわる（バリエーションがある）ものはDIコンテナで管理

