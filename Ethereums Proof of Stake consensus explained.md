# Ethereum's Proof of Stake consensus explained

## Transcript
Gaspar is the consensus method Ethereum will be switching to when it moves from proof of work to proof of stake.

It is actually the combination of two different consensus methods called LMD GHOST and Casper FFG.

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

Here is the text broken up into sentences with line breaks:

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
