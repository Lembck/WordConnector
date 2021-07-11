# WordConnector
An exploration of Levenshtein distance

A program to connect words through other words through insertions, deletions, and swaps of a single letter

Featuring:
 - find([word, word, ...])
 - findLongest(word)
 
Examples:

```
find("otter", "rock")
otter outer router routes routs rots rocs rock 
```
 - in 0.2 seconds



```
find("stunning", "hello")
stunning sunning cunning canning caning casing basing basin basil bail hail hall hallo hello 
```
 - in 0.53 seconds
 
```
findLongest("flexing")
flexing fleeing freeing freezing breezing breeding bleeding blending bending beading bearing 
baring bring bing bang bane bake baked beaked peaked peeked peered petered pestered festered 
fettered bettered battered bantered cantered catered capered tapered tampered hampered hammered
```
36 words in length