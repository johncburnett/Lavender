# Lavender
Lavender is the culmination of my research into generative harmony. While the application is still very early in its development, Lavender itself is an algorithmic model of generative and adaptive harmony that learns from the choices of its user, creating a network of harmonic relations. A formalized model of this system is currently in the works, for those interested.

### Usage
To use Lavender, simply run `./lavender`. You will be presented with a shell-like interface.
Lavender comes with four pitch sets already loaded into its bank. To make a chain, use the following syntax:
```
<~lavender~>$ 0 -> 1 ! 2 - 0 -> 3
```
Lavender will output a chain of supersets for you. Each number refers to the index of the pitch set in your bank. To see the bank, run the command `list`. To add a pitch set to the bank, run `add <pset>` (using a set of your choosing). The `add_r` command will simply add a random set to the bank (use `add_r <n>` for multiple random sets). One can clear the bank with the `clear` command.

The power of Lavender lies in the `generate <n>` command. With each chain that the user inputs, Lavender adds to a network of harmonic relations. The `generate` command outputs a random walk through this network. Just pass it the length of the chain you would like. There is also the `path <start> <end>` command that will return a random path between two specified sets.

One can also instruct Lavender to train itself with the `train <n>` command, which automatically runs n randomly generated chains using the current bank. One may also use the `populate <n> <m>` command, which will create n random sets and train the model m times.

The `notate` command will transform the most recent chain into music notation.

##### Operators
* `->` will calculate the superset with the most common tones.
* `! ` will calculate the superset with the least common tones.
* `- ` will move arbitrarily between supersets

### Dependencies
* Python 2.7.10
* [Abjad](http://abjad.mbrsi.org/)

### What's to Come
The most exciting part of Lavender is currently still in the making. Lavender will learn from the input you give it and allow you to generate endless streams of harmonic material based on your taste. I plan to expand Lavender to handle octave-specific and microtonal harmonies as well as translate all of this into music notation through the wonderful Abjad API. 

Special thanks to the Oberlin Conservatory for supporting this research!
