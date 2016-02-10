# Lavender
Lavender is the culmination of my research into generative harmony. While the application is still very early in its development, Lavender itself is an algorithmic model of generative and adaptive harmony that learns from the choices of its user, creating a network of harmonic relations. A formalized model of this system is currently in the works, for those interested.

### Usage
To use Lavender, simply run `./lavender`. You will be presented with a shell-like interface.
Lavender comes with four pitch sets already loaded into its bank. To make a chain, use the following syntax:
```
<~lavender~>$ 0 -> 1 -> 2 -> 0 -> 3
```
Lavender will output a chain of supersets for you. Each number refers to the index of the pitch set in your bank. To see the bank, run the command `list`. To add a pitch set to the bank, run `add [0,5,9,11]` (using a set of your choosing). You can clear the bank with the `clear` command.

### Dependencies
* [Abjad](http://abjad.mbrsi.org/) (not yet, but soon)

### What's to Come
The most exciting part of Lavender is currently still in the making. Lavender will learn from the input you give it and allow you to generate endless streams of harmonic material based on your taste. I plan to expand Lavender to handle octave-specific and microtonal harmonies as well as translate all of this into music notation through the wonderful Abjad API. 

Special thanks to the Oberlin Conservatory for supporting this research!
