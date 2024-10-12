# Project-Nyota

![Nichelle Nichols as Uhura on the set of Star Trek: The Original Series](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Nichelle_Nichols%2C_NASA_Recruiter_-_GPN-2004-00017.jpg/220px-Nichelle_Nichols%2C_NASA_Recruiter_-_GPN-2004-00017.jpg)
**Language tools for NeoTrinkey**

Inspired by Star Trek's Nyota Uhura, these programs provide a way to use a NeoTrinkey to review alien (or foreign) language words or phrases.

There are two programs, *langtutor.py* and *langtest.py* - copy the one you want to use to **code.py**. The helper files *wise.py* and *prt.py* are required.

The file "langs" is a list of the languages to review. Each line in "langs" should be the name of a file containing language information. In this archive the languages are: klingon, vulcan, mandoa, and Swahili (in honor of Uhura - "Nyota" means "star" in Swahili).

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

To toggle between languages, touch pad #1. When you reach the one you want to review (for the *langtutor.py* program) touch pad #2 and you'll see 5 random review pairs. For example from the Mando'a set:

```
You're right. : Gar serim.
twenty : ad'eta
seventy : tad'eta
eighty : shehn'eta
Good. : Jate.
```

With the *langtest.py* program, when you choose a language and touch pad#2, you'll get **four** tests where you're given a word or phrase, then a choice of two possible answers in the target language. Touch #1 or #2 to choose. A pixel will light green or red to indicate if you are right or wrong. (If wrong, the correct answer will be given). After four questions, you can touch #2 to get four more, or touch #1 to change languages.

For example:
```
Current lang: vulcan

advise
1:lahso
2:a'Tha

correct!

walk (action-word)
1:imroy
2:lahso

yes!

'logic', reality-truth, the way things are.
1:c'thia
2:lahso

wrong: c'thia

'immanence' direc experience of the creator
1:kah-hir
2:a'Tha

correct!

touch #2 for another quiz, or #1 to change language.
```

When running the programs, you can set the variable REPL to "True" or "False" to direct the output. If REPL=True, all output is sent to the REPL. If it is False, output is directed as if typed using the HID interface. There is a delay when that is the case, to give you time to switch to an open editor window to receive the output.


**Language sources:**

* Swahili vocab from: https://www.fluentin3months.com/swahili-words/
* Mando'a vocab from https://mandoa.org/
* Klingon vocab from: https://kli.org and https://hol.kag.org
* Vulcan vocab from: https://tinyurl.com/VulcanArchive - archive.org of Marketa Zvelbil's original Vulcan work (*note*: In case archive.org is not available, I've copied the Dictionary and Lexicon to vulcdict.txt and vulcanlex.txt)
* To create your own language, you can use a tool like this: https://rollforfantasy.com/tools/language-generator.php
