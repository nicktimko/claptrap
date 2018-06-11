# claptrap

> I'll stop talking when I'm dead!

Generate random phrases using bigram frequencies. Counts some punctuation as objects when creating bigrams so it includes realistic punctuation.

Useful if you want something maybe humorous to put into text fields other than totally random strings.

```pythons
import claptrap

phrasegen = claptrap.PhraseGenerator.from_dump(file='dumps/markov-dracula.xz')

for _ in range(10):
    print(phrasegen.phrase([70, 80]))
```

Kicks out:

```text
Hark! Arthur. So that you? Don't want souls? I can fight in terror afoot
Ha, but all night. Me have seen and I wondered at once to keep strict injunction
That it behind us who is better to loathe it, we should get abreast of
Gold piece of one thing? His patients. Harker began to heaven where he
Could speak without getting out. Having seen her and letters: colophon
New courage is paler as she who was some evil that the reading his departure
Such a little before the horses and his seat was silent, however, I have
So strong in the towns or say sadly that the result in kindness I know
From behind us and was concerned about ten o'clock before my child was
Simply saying that the general plan. She turned to the geologic and take
```
