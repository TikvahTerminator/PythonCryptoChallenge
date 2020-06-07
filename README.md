# PythonCryptoChallenge
*A tool developed as a CTF crypto challenge*

![Screenshot of Encrypter.py](https://i.imgur.com/s19YlVg.png)

## Solution?

It's a simple substitution cipher that basically split's the alphabet like so:

[[[["a","b","c"],["d","e","f"]],[["g","h","i"],["j","k","l"]]],[[["m","n","o"],["p","q","r"]],[["s","t","u"],["v","w","x","y","z"]]]]

These arrays are then used as numbers to access the specific values, for example, "Hello" would be:
*0,1,0,1:0,0,1,1:0,1,1,2:0,1,1,2:1,0,0,2:*  with : being the end of a letter. 
**That's it! Easy peasey lemon squeasy!  :)**
**0,0,1,1:0,0,0,0:1,1,0,0:1,1,1,3:1,0,1,0:0,0,1,1:0,0,0,0:1,1,0,0:0,0,1,1:1,1,1,3:0,1,1,2:0,0,1,1:1,0,0,0:1,0,0,2:1,0,0,1:1,1,0,0:1,0,1,1:1,1,0,2:0,0,1,1:0,0,0,0:1,1,0,0:1,1,1,3:**
