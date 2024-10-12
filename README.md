# Project-Nyota

![Nichelle Nichols as Uhura on the set of Star Trek: The Original Series](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Nichelle_Nichols%2C_NASA_Recruiter_-_GPN-2004-00017.jpg/220px-Nichelle_Nichols%2C_NASA_Recruiter_-_GPN-2004-00017.jpg)
**Language tools for NeoTrinkey**

Inspired by Star Trek's Nyota Uhura, these programs provide a way to use a NeoTrinkey to review alien (or foreign) language words or phrases.

There are two programs, *langtutor.py* and *langtest.py* - copy the one you want to use to **code.py**. The helper files *wise.py* and *prt.py* are required.

The file "langs" is a list or the languages to review. Each line in "langs" should be the name of a file containing language information. In this archive the languages are: klingon, vulcan, mandoa, and Swahili (in honor of Uhura - "Nyota" means "star" in Swahili).

Language files should be in the form:

```
"Word-or-phrase", "target-language-translation"
"Word-or-phrase", "target-language-translation"
"Word-or-phrase", "target-language-translation"
....
```

When either program runs, you'll see:

```
number of languages: 4

klingon
vulcan
mandoa
swahili
Current lang: klingon
```


* Swahili vocab from: https://www.fluentin3months.com/swahili-words/
* Mando'a vocab from https://mandoa.org/
* Klingon vocab from: https://kli.org and https://hol.kag.org
* Vulcan vocab from: https://tinyurl.com/VulcanArchive - archive.org of Marketa Zvelbil's original Vulcan work (*note*: In case archive.org is not available, I've copied the Dictionary and Lexicon to vulcdict.txt and vulclex.txt)
