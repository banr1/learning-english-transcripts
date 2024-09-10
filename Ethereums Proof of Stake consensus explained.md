# Ethereum's Proof of Stake consensus explained

## Transcript
Gaspar is the consensus method Ethereum will be switching to when it moves from proof of work to proof of stake.

It is actually the combination of two different consensus methods called LMD-GHOST and Casper FFG.

In this video I'll be going through how it works.

Firstly, what is stake and how exactly do you prove it?

Stake is the number of tokens you own in the network or your stake in the network.

Tokens are scarce resources that are difficult to replicate similar to how a proof-of-work cache is a difficult resource to replicate.

To prove your stake with Ethereum there is a smart contract that keeps track of all the validators who are staking.

You have to send 32 ETH along with your validator's public address and a withdrawal address to the smart contract.

Now whenever you sign something using the private key of your validator other people can check in the smart contract for your address and verify you are staking with 32 ETH.

Your validator's digital signature becomes your proof of stake.

The reason you actually have to lock up your stake on Ethereum unlike many other proof-of-stake protocols is to have slashing.

Slashing is when some of the validated stake will be burned if they are found misbehaving.

The reason each validator has to stake 32 ETH is that it allows for each signature from a validator to be treated equally as decentralized consensus methods are voting models with all signatures being equal.

It makes it easier to count the votes but how exactly do they cast their votes in the first place?

This is where the consensus method comes in.

The two main families of consensus methods used with cryptocurrencies are the longest chain model and the BFT model.

Ethereum has two consensus methods and uses both types.

First for the default consensus method called GHOST they have used a variation of the longest chain model with consensus methods being essentially voting models.

When you use the longest chain model, every block added to the blockchain is essentially a vote for the branch of the fork you want to win.

However, using the traditional longest chain model, you sometimes come into cases where a validator's vote isn't counted.

In this example, we can see a fork.

One side of the fork is two blocks long, and the other side has three blocks added, but they all reference the same block, so it's only one block long.

If we use the normal longest chain rule, then the top branch would become the winner as it is the longest chain.

However, is this actually what we want?

The top branch only had two validators to vote for it, whereas three validators voted for the bottom branch.

So shouldn't it be the bottom branch that wins?

Due to the three validators all referencing the same block, their three votes only counted as one using the traditional longest chain rule.

GHOST has changed the model slightly so that it counts every block in a fork as a vote, even if they are conflicting blocks and not a part of the longest chain.

This means that under GHOST, the bottom fork should win as more validators have voted for it compared to the top branch.

New blocks will be added to one of the three bottom blocks instead of the top fork.

If Ethereum is set up so that every 12 seconds there is a time slot where a random validator can add a block to the blockchain, with around four hundred thousand validator nodes already at the time of this video, if only one validator was able to add a block every 12 seconds, it would take almost eight weeks before all the validators will have voted on a block.

Whilst you don't need to wait for 100% of the validators to vote on something before you can be pretty sure it's safe and unlikely to be rolled back, even waiting for just 10% of the validators to vote on it would be around 5 days, which is way too long.

To shorten the amount of time to hear from all the validators, another aspect that Ethereum has changed is that producing a block is no longer the only way to vote in consensus.

They have another function called an attestation, which is essentially where validators don't produce a block but instead attest to an already existing block.

If validators attest to a block, that means they are voting for that block.

Now if we look at an example, there are two forks: the top one is clearly longer than the bottom one, but the bottom one has more validators attesting to the block, meaning more validators have voted for the bottom fork than the top fork.

So it is seen as the winning chain and new blocks should be added to the bottom branch.

This is a general idea behind how GHOST operates: the side of the fork with more voting weight from attestations becomes the winning branch, even if they are attestations in blocks that won't be included in the final chain.

With 400,000 validators, having them just randomly attesting to blocks would also be chaos, so some order is needed.

Ethereum splits up time slots into epochs, where an epoch is 32 time slots.

This makes an epoch 6 minutes and 24 seconds.

Every epoch, all the validators staking in the staking smart contract are randomly split into equal committees.

Each committee is then responsible for one time slot in the epoch.

The first member of the committee is chosen to produce a block for the time slot, and all the rest of the validators are assigned to attest to the block they think is the latest block, which should be the block that the block proposer proposed.

Every epoch, validators are only allowed to attest to one block; otherwise, they will be slashed.

If the block proposer for a time slot doesn't propose a block, then four seconds into the time slot, the attesting validators should instead just vote for the previous block.

Having 12,000 signatures attached to each block would also use up a ton of space so Ethereum uses a signature aggregation method called BLS signatures which allows hundreds of signatures to be aggregated together into one.

Even splitting up the validators into 32 committees, 12,000 signatures is still a lot.

This is why committees are split up even further into 128 subnets which would mean around 100 signatures per subnet.

In each subnet, 16 validators are randomly assigned to produce a BLS signature and the block proposer then takes the best signature from each of the 128 subnets and then aggregates them together into one final BLS signature so that in the final block there is only one BLS signature representing more than 12,000 validators.

All these signatures every block is the reason why they have set 32 ETH as the minimum requirement for staking as lowering it even more increases the number of signatures even further which would require increasing the node specs or improving the aggregation technique.

The BLS signatures are also a core part of bringing randomness to the protocol.

Making sure that committees are unpredictable and random is important to make sure an attacker can't try to gain the randomness to be the only block producer and censor transactions.

The way Ethereum assigns which validators are assigned to which committee is based on a function called round out.

Round out is a method where a number of people get together to produce an unpredictable random number.

In round out, all the participants pick a random number and commit to the number.

Once everyone has committed to the number, they share it and run all the random numbers for a mixer to produce an unpredictable random number.

As long as there is one honest party, the number should be random.

For Ethereum, this random number that validators have committed to is their private key.

They don't share their private key of course, but instead sign blocks with their private key.

When you make a digital signature, the signature is always different depending on the data you're signing.

So this means every block signed will produce a different random number that other people can't predict unless they know your private key.

The BLS signature is then where all the random numbers are mixed together to produce the final random number.

This random number is then used to assign validators into committees for the next epoch.

Seeing as people have to lock up some ETH and potentially get slashed if they misbehave or go offline, an incentive is required to stake or else nobody would run a validated node.

Ethereum gives a large reward for proposing a block and also gives a smaller reward to every validator that makes an attestation.

Seeing as validators attest every epoch but are rarely chosen to propose a block, most of their rewards will come from attestations.

The attestation rewards will vary on if they are on time and if they are voting the same as everyone else.

When Ethereum switches to proof of stake, the issuance rate and rewards will become variable and depend on the amount of ETH being staked.

They are likely to be between 0.54% and 0.94% per year.

Most validators will then earn around 5% per year.

I mentioned at the beginning of the video that Ethereum has two consensus methods.

GHOST is secure already, so why is the second one needed?

Casper the Friendly Finality Gadget is the name of the other consensus method, and as the name suggests, shows when blocks become final.

Ethereum can run perfectly fine without Casper, but finality is a nice feature to have.

Whilst GHOST is a variation of the longest chain wins model, Casper is a BFT method.

Byzantine fault tolerant models of consensus are typically two rounds of voting between the validators, and if one side has two-thirds of the vote after two rounds, it becomes final.

In the first round, validators commit to a vote, and in the second round actually go through with the vote.

You need two rounds because if it was only one round, an attacker could potentially tell two sides different things in order to split the network.

If we look at Ethereum, we can see that every epoch all the validators will vote, so an epoch can be seen as a round of a BFT vote.

After one round, everyone has committed their vote, but there could be a fork that is split with equal votes and an attacker double voting and voting for both sides of the fork, leading to both sides having more than 67% of the vote.

So one round isn't enough to guarantee finality.

After the epoch, the attacker will be heavily slashed for double voting.

If they go below 16 ETH, they are then kicked from the staking contract, so can only attempt to do it a few times.

The other case where there might be an issue is if validators aren't voting enough to reach 67%.

In this case, the validators that aren't voting will also get slashed for inactivity until 67% can be reached again.

Ethereum will wait until there are two rounds in a row where less than one-third of the stake is slashed before considering a block final.

Casper doesn't need to reach finality for Ethereum to run.

It can go on running using GHOST and still have good probabilistic finality.

So Ethereum won't go down and freeze if a third of the validators go offline like most protocols using a purely BFT-based consensus model.

When using proof of stake, there's a well-known attack called a long-range attack.

Essentially, an attacker will stake a large amount for a period of time and then stop staking.

Once they have stopped staking, they will create a secret fork from before they stop staking, so in their fork they are still staking, and then create a chain that is heavier than the honest chain and share it with the other nodes to take over with their fork.

For this type of attack, you can't slash the attacker's stake as they will have already stopped staking before they created the fork, so it is difficult to punish them.

Most nodes that are online won't accept the new fork as they will have already finalized the chain and the fork wasn't posting blocks on time, so it's clearly not the honest chain.

However, for new nodes joining the network or for nodes that went offline for a long period of time, they won't know the difference and if they follow the consensus rules will follow the attacker's chain.

The way Ethereum deals with this is by introducing a small level of subjectivity for nodes joining or rejoining the network.

They need to ask other nodes for an identifier from the latest block in the honest chain in order to figure out which fork to follow.

This is somewhat controversial as many within the space believe that you should be able to know what the correct state of the chain is just by knowing the rules to follow and not needing to ask other people.

If someone is trying an attack, the rules should be able to deal with it.

However, Ethereum argues that to even know the rules in the first place you need some subjectivity, and asking for the correct chain once when you first set up a node doesn't add much more subjectivity on top of that.

As an overview, every epoch validators are randomly split up into 32 committees and each committee is responsible for adding a block in their time slot.

All the validators have to attest to a block during their time slot.

Whichever chain ends up with the most attestations becomes the winning branch that new blocks should be added to.

After two epochs, if 67% of the vote are in agreement for both epochs and there wasn't any slashing recorded for validators voting on multiple forks, the chain can be finalized.

If this isn't achieved, the chain will keep running with probabilistic finality.

Then there should be validators that get slashed until finality can be achieved again.

Though this is the general idea behind consensus on Ethereum, most proof-of-stake protocols have an honest majority assumption.

As long as more than 51% of the stake is completely honest, then the protocol is meant to be secure.

Ethereum doesn't see this as secure enough and instead has an assumption that more than 51% of the stake is economically motivated.

Why this matters is that the honest majority assumption does not account for attackers potentially bribing their validators or even just users willing to re-org a chain for an MEV opportunity like a large arbitrage.

This is something that is extremely difficult to measure and actually prove you are secure against as it is subjective or unknown what amount is needed to bribe someone.

Ethereum has tried to take these attacks into account, which is why it has implemented slashing.

Slashing brings a huge cost to any dishonest validator, which massively discourages this behavior.

This arguably makes it the most secure proof-of-stake based consensus method currently because it is trying to protect against attacks that other proof-of-stake based protocols don't even look at.

To summarize, Ethereum managed to combine both the longest chain wins and BFT-based consensus model into one, allowing for very robust protocol due to using the longest chain and being able to have finality due to the BFT-based consensus running on top of it.

Whilst it is very complex, which can increase the chance of bugs and has given up on some speed compared to full BFT-based consensus methods, it's still very fast to our longest chain wins model and has aimed for security and decentralization to build an extremely secure proof-of-stake based consensus method.

If you enjoyed the video, please leave a like and subscribe if you want to catch my future content.

## Translated Transcript

Gasperは、EthereumがPoWからPoSに移行する際に採用する合意形成方式です。

実際には、LMD-GHOSTとCasper FFGという2つの異なる合意形成方式を組み合わせたものです。

このビデオでは、その仕組みについて説明します。

まず、ステークとは何か、そしてどのようにしてそれを証明するのでしょうか？

ステークとは、ネットワーク内で所有しているトークンの数、つまりネットワークにおけるあなたの持ち分のことです。

トークンは、PoWのキャッシュが複製困難なリソースであるのと同様に、複製が難しい希少なリソースです。

Ethereumでステークを証明するには、ステーキングを行っているすべてのバリデーターを追跡するスマートコントラクトがあります。

32 ETHと、バリデーターの公開アドレス、そして引き出し用アドレスをスマートコントラクトに送信する必要があります。

これにより、バリデーターの秘密鍵を使って何かに署名すると、他の人々はスマートコントラクトであなたのアドレスを確認し、32 ETHでステーキングしていることを検証できます。

バリデーターのデジタル署名が、あなたのPoSとなるのです。

Ethereumで実際にステークをロックアップする必要があるのは、他の多くのPoSプロトコルとは異なり、スラッシングを行うためです。

スラッシングとは、バリデーターが不正行為を行っていると判断された場合に、ステークの一部が焼却されることです。

各バリデーターが32 ETHをステークする理由は、分散型合意形成方式が全ての署名を平等に扱う投票モデルであるため、バリデーターからの各署名を平等に扱えるようにするためです。

これにより投票のカウントが容易になりますが、そもそもバリデーターはどのように投票を行うのでしょうか？

ここで合意形成方式が関係してきます。

暗号通貨で使用される主な合意形成方式には、最長チェーンモデルとBFTモデルの2つがあります。

Ethereumには2つの合意形成方式があり、両方のタイプを使用しています。

まず、GHOSTと呼ばれるデフォルトの合意形成方式では、最長チェーンモデルの変形を使用しています。合意形成方式は本質的に投票モデルです。

最長チェーンモデルを使用する場合、ブロックチェーンに追加される各ブロックは、本質的に勝たせたいフォークの枝に対する投票となります。

しかし、従来の最長チェーンモデルを使用すると、バリデーターの投票が計上されないケースが時々発生します。

この例では、フォークが発生しています。

フォークの一方は2ブロック長で、もう一方は3つのブロックが追加されていますが、すべて同じブロックを参照しているため、実質的には1ブロック長です。

通常の最長チェーンルールを使用すると、上部のブランチが最長チェーンであるため勝者となります。

しかし、これは本当に望ましい結果でしょうか？

上部のブランチには2つのバリデーターしか投票していませんが、下部のブランチには3つのバリデーターが投票しています。

下部のブランチが勝つべきではないでしょうか？

3つのバリデーターが同じブロックを参照しているため、従来の最長チェーンルールでは、3つの投票が1つとしてしか数えられません。

GHOSTでは、最長チェーンの一部ではない競合するブロックであっても、フォーク内のすべてのブロックを1票として数えるようにモデルを少し変更しています。

これにより、GHOSTの下では、上部のブランチよりも多くのバリデーターが投票しているため、下部のフォークが勝利するはずです。

新しいブロックは、上部のフォークではなく、下部の3つのブロックのいずれかに追加されることになります。

Ethereumでは、12秒ごとにランダムなバリデーターがブロックチェーンにブロックを追加できるタイムスロットが設定されています。このビデオの時点で約40万のバリデーターノードがすでに存在しており、12秒ごとに1つのバリデーターだけがブロックを追加できるとすると、すべてのバリデーターがブロックに投票するまでに約8週間かかることになります。

ブロックが安全で巻き戻される可能性が低いと確信するために、バリデーターの100%が投票するのを待つ必要はありませんが、バリデーターの10%が投票するのを待つだけでも約5日かかり、これは長すぎます。

すべてのバリデーターから意見を聞くまでの時間を短縮するために、Ethereumが変更したもう一つの側面は、ブロックの生成がもはや合意形成における唯一の投票方法ではないということです。

アテステーションと呼ばれる別の機能があり、これはバリデーターがブロックを生成せずに、既存のブロックを証明するものです。

バリデーターがブロックを証明すると、そのブロックに投票していることになります。

例を見てみましょう。2つのフォークがあり、上部のフォークは明らかに下部のフォークよりも長いですが、下部のフォークにはより多くのバリデーターがブロックを証明しています。つまり、より多くのバリデーターが下部のフォークに投票しているということです。

したがって、下部のフォークが勝利チェーンとみなされ、新しいブロックは下部のブランチに追加されるべきです。

これがGHOSTの背後にある一般的な考え方です。最終的なチェーンに含まれないブロック内のアテステーションであっても、アテステーションからの投票の重みが多いフォークの側が勝利ブランチとなります。

40万のバリデーターがいる場合、ランダムにブロックを証明するだけでは混乱を招くため、ある程度の秩序が必要です。

Ethereumは、タイムスロットをエポックに分割しています。1エポックは32のタイムスロットです。

これにより、1エポックは6分24秒となります。

毎エポック、ステーキングスマートコントラクトでステーキングしているすべてのバリデーターは、ランダムに均等な委員会に分割されます。

各委員会は、そのエポック内の1つのタイムスロットを担当します。

委員会の最初のメンバーがそのタイムスロットのブロックを生成するために選ばれ、残りのバリデーターは最新のブロックだと思うブロック（通常はブロック提案者が提案したブロック）を証明するよう割り当てられます。

毎エポック、バリデーターは1つのブロックにのみ証明することが許可されており、そうでない場合はスラッシングされます。

タイムスロットのブロック提案者がブロックを提案しない場合、タイムスロットの4秒後に、証明するバリデーターは代わりに前のブロックに投票すべきです。

各ブロックに12,000の署名を添付すると大量のスペースを使用してしまうため、EthereumはBLS署名と呼ばれる署名集約方法を使用しており、これにより数百の署名を1つに集約することができます。

バリデーターを32の委員会に分割しても、12,000の署名はまだ多すぎます。

そのため、委員会はさらに128のサブネットに分割され、サブネットあたり約100の署名となります。

各サブネットでは、16のバリデーターがランダムに割り当てられてBLS署名を生成し、ブロック提案者は128のサブネットそれぞれから最良の署名を取り、それらを1つの最終的なBLS署名に集約します。そのため、最終的なブロックには12,000以上のバリデーターを代表する1つのBLS署名のみが含まれます。

毎ブロックのこれらの署名が、ステーキングの最小要件を32 ETHに設定した理由です。これをさらに下げると署名の数がさらに増加し、ノードのスペックを上げるか集約技術を改善する必要が出てきます。

BLS署名は、プロトコルにランダム性をもたらす上でも重要な役割を果たしています。

委員会が予測不可能でランダムであることを確認することは、攻撃者がランダム性を利用して唯一のブロック生成者となり、トランザクションを検閲しようとするのを防ぐために重要です。

Ethereumがバリデーターを各委員会に割り当てる方法は、ラウンドアウトと呼ばれる関数に基づいています。

ラウンドアウトは、複数の人々が集まって予測不可能なランダムな数を生成する方法です。

ラウンドアウトでは、すべての参加者がランダムな数を選び、その数にコミットします。

全員が数字にコミットしたら、それを共有し、すべてのランダムな数をミキサーにかけて予測不可能なランダムな数を生成します。

少なくとも1人の正直な参加者がいれば、その数はランダムであるはずです。

Ethereumの場合、バリデーターがコミットしたこのランダムな数は彼らの秘密鍵です。

もちろん、彼らは秘密鍵を共有しませんが、代わりに秘密鍵でブロックに署名します。

デジタル署名を行う場合、署名する対象のデータによって署名は常に異なります。

つまり、署名されたすべてのブロックは、秘密鍵を知らない限り他の人が予測できない異なるランダムな数を生成することになります。

BLS署名は、すべてのランダムな数が混ぜ合わされて最終的なランダムな数を生成する場所です。

このランダムな数は、次のエポックのバリデーターを委員会に割り当てるために使用されます。

人々がETHをロックアップし、不正行為やオフラインになった場合にスラッシングされる可能性があるため、ステーキングのインセンティブが必要です。そうでなければ、誰もバリデーターノードを運用しないでしょう。

Ethereumは、ブロックの提案に大きな報酬を与え、アテステーションを行うすべてのバリデーターにも小さな報酬を与えています。

バリデーターは毎エポックアテステーションを行いますが、ブロックを提案するために選ばれることは稀であるため、彼らの報酬の大部分はアテステーションから得られることになります。

アテステーションの報酬は、タイミングが適切かどうか、そして他の人と同じ投票をしているかどうかによって変動します。

EthereumがPoSに移行すると、発行率と報酬は変動し、ステーキングされているETHの量に依存するようになります。

おそらく年間0.54%から0.94%の間になると予想されています。

ほとんどのバリデーターは年間約5%を稼ぐことになるでしょう。

ビデオの冒頭で、Ethereumには2つの合意形成方式があると述べました。

GHOSTはすでに安全ですが、なぜ2つ目の方式が必要なのでしょうか？

Casper the Friendly Finality Gadgetは、もう一つの合意形成方式の名前で、その名前が示すように、ブロックがいつ最終的になるかを示します。

EthereumはCasperなしでも完璧に機能しますが、ファイナリティは持っていて損のない機能です。

GHOSTが最長チェーン勝利モデルの変形であるのに対し、CasperはBFT方式です。

ビザンチン障害耐性（BFT）モデルの合意形成は、通常バリデーター間で2ラウンドの投票を行い、2ラウンド後に一方が3分の2の投票を得た場合、それが最終的となります。

第1ラウンドでは、バリデーターが投票を約束し、第2ラウンドで実際に投票を行います。

2ラウンド必要な理由は、1ラウンドだけだと、攻撃者がネットワークを分断するために両サイドに異なることを伝える可能性があるからです。

Ethereumを例にとると、毎エポックごとにすべてのバリデーターが投票するので、エポックはBFT投票の1ラウンドと見なすことができます。

1ラウンド後、全員が投票を約束しますが、攻撃者が二重投票をして分岐の両側に投票すると、両側が67%以上の票を得て、同等の票数で分岐が分かれる可能性があります。

そのため、1ラウンドだけでは確定性を保証するには不十分です。

エポック後、攻撃者は二重投票で大幅にスラッシングされます。

16 ETH未満になると、ステーキング契約から追放されるので、数回しか試みることができません。

もう一つの問題が発生する可能性があるのは、バリデーターの投票が67%に達しない場合です。

この場合、投票しないバリデーターも、67%に達するまで不活動によりスラッシングされます。

Ethereumは、ステークの3分の1未満がスラッシングされる2ラウンドが連続して発生するまで待ってから、ブロックを最終的なものとみなします。

CasperはEthereumを実行するために確定性に達する必要はありません。

GHOSTを使用して実行を続け、良好な確率的確定性を持つことができます。

そのため、純粋にBFTベースのコンセンサスモデルを使用するほとんどのプロトコルとは異なり、Ethereumはバリデーターの3分の1がオフラインになっても停止して凍結することはありません。

PoSを使用する際、よく知られた攻撃に長期攻撃があります。

基本的に、攻撃者は一定期間大量のステークを行い、その後ステークを停止します。

ステークを停止した後、ステークを停止する前の時点から秘密の分岐を作成し、その分岐では依然としてステークを行っているように見せかけ、正直なチェーンよりも重いチェーンを作成して他のノードと共有し、その分岐で乗っ取ろうとします。

この種の攻撃では、攻撃者が分岐を作成する前にすでにステークを停止しているため、攻撃者のステークをスラッシングすることができず、罰するのが難しくなります。

オンラインのほとんどのノードは、すでにチェーンを確定させており、分岐が時間通りにブロックを投稿していないことから明らかに正直なチェーンではないため、新しい分岐を受け入れません。

しかし、ネットワークに新しく参加するノードや長期間オフラインだったノードは、違いがわからず、コンセンサスルールに従えば攻撃者のチェーンに従うことになります。

Ethereumはこれに対処するため、ネットワークに参加または再参加するノードに小さなレベルの主観性を導入しています。

どの分岐に従うべきかを判断するために、正直なチェーンの最新ブロックの識別子を他のノードに尋ねる必要があります。

これはやや議論の余地があります。多くの人々は、ルールを知っているだけで正しいチェーンの状態がわかるべきで、他の人に尋ねる必要はないと考えているからです。

誰かが攻撃を試みている場合、ルールだけでそれに対処できるはずだと考えられています。

しかし、Ethereumは、そもそもルールを知るためにも多少の主観性が必要であり、ノードを最初に設定するときに一度だけ正しいチェーンを尋ねることは、それ以上の主観性をほとんど追加しないと主張しています。

概要として、毎エポックごとにバリデーターは無作為に32の委員会に分けられ、各委員会はそれぞれのタイムスロットでブロックを追加する責任があります。

すべてのバリデーターは、自分のタイムスロット中にブロックを証明する必要があります。

最も多くの証明を得たチェーンが、新しいブロックを追加すべき勝利ブランチとなります。

2エポック後、両エポックで67%の票が一致し、複数の分岐に投票したバリデーターのスラッシングが記録されていない場合、チェーンを確定させることができます。

これが達成されない場合、チェーンは確率的確定性で実行を続けます。

その後、再び確定性が達成されるまでバリデーターがスラッシングされるはずです。

これがEthereumのコンセンサスの一般的な考え方ですが、ほとんどのPoSプロトコルには正直な過半数の仮定があります。

ステークの51%以上が完全に正直である限り、プロトコルは安全であるとされています。

Ethereumはこれを十分に安全とは考えておらず、代わりにステークの51%以上が経済的に動機づけられているという仮定を持っています。

これが重要な理由は、正直な過半数の仮定が、攻撃者が潜在的にバリデーターを買収したり、大規模な裁定取引のようなMEV機会のためにチェーンを再編成しようとするユーザーを考慮していないからです。

これは非常に測定が難しく、実際に安全であることを証明するのが難しいものです。なぜなら、誰かを買収するのに必要な金額は主観的であったり不明だからです。

Ethereumはこれらの攻撃を考慮しようとしており、そのためにスラッシングを実装しています。

スラッシングは不正直なバリデーターに大きなコストをもたらし、このような行動を大きく抑制します。

これにより、他のPoSベースのプロトコルが考慮していない攻撃からも保護しようとしているため、現在最も安全なPoSベースのコンセンサス方式であると言えます。

要約すると、Ethereumは最長チェーン勝利とBFTベースのコンセンサスモデルを1つに組み合わせ、最長チェーンを使用することで非常に堅牢なプロトコルを実現し、その上で動作するBFTベースのコンセンサスにより確定性を持つことができました。

非常に複雑であるため、バグの可能性が高まり、完全なBFTベースのコンセンサス方式と比べて速度を犠牲にしていますが、それでも最長チェーン勝利モデルよりもはるかに高速で、セキュリティと分散化を目指して、非常に安全なPoSベースのコンセンサス方式を構築しています。

この動画を楽しんでいただけたなら、ぜひ「いいね」を押し、今後のコンテンツをお見逃しなく購読してください。
