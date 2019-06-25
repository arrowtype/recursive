# Making a binary variable axis

It is possible to make a "binary" axis.

Initially, I thought that this would be done by making an axis's min–max values go from 0 to 1.

Instead, I learned from Petr van Blokland that it is done in a slightly unexpected way. In a designspace file, do the following for a given axis:

- Set the first master at `0`
- Set the second at `100`
- Make a duplicate `source` reference to the first master at `49.99`
- Make a duplicate `source` reference to the second master at `50`

See the designspace file included in this folder for an example of this.

## Caveats

I don't yet understand the impact of duplicate source references on final filesize.

It might be a little, or it might be a lot – presumably, it might be almost double the filesize, if each source reference adds a set of deltas. This needs testing.