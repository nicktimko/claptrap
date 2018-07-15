# claptrap

> I'll stop talking when I'm dead!

Generate random phrases using bigram frequencies. Counts some punctuation as objects when creating bigrams so it includes realistic punctuation.

Useful if you want something maybe humorous to put into text fields other than totally random strings.

## CLI

```bash
$ claptrap drac -l40 -n5
Sighted. Here; if trying to pull them ov
The horrible doubt himself shone with mo
Concealment of despair seized some islan
Of them on the room with a storey lowers
Whom? He made pets of my very happy look
```

Free-style [wub wub](https://www.youtube.com/watch?v=8Z5kjXvYpkk)

```bash
$ claptrap wub -l10-50 -n5
WUB; Wub wuB wUB wUB Wub
wUb. wUB Wub; WuB?
WUB: wub WuB WUb Wub WUb wuB WUB: wUB WUB WuB
wUB WuB wUB, wUb WUB.
WUb WUB wUB wuB WUB WuB
```

## Library

```python
import claptrap

phrasegen = claptrap.GraphPhraseGenerator.from_resource('dracula')

for _ in range(10):
    print(phrasegen.phrase([60, 80])
```

```text
Should tear or to the world! Jack, a little bargaining he remembered
Me what steps, as poor Harker's hand. Shall, and fed the left
Out two, and thicker and go to notice any particular part of
His wife dead! And feed! Oh, as much. I knew that churchyard
He said solemnly as we should have, but flew to cheer each of
His where to the snow, but we destroyed them both hands all my
Eyes closed behind us so thankful to two atmospheres, with the
Driver with dust had better not. The hand; instantly formed round
Her. He ask me. I told me not move forward hesitatingly; and
A few people are well, we have to home with the tide, for you
```
