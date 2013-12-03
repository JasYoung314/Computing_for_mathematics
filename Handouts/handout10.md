# Computing for mathematics handout 10 - File paths, formatting, floating figures, cloud.sagemath, plagiarism and next semester.
Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

LaTeX.

## Paths

There are two (popular) types of operating systems:

- *nix (which powers Linux and Mac computers): more popular for coding.
- Windows: more popular for gaming.

File paths on *nix machines use `/` to separate directories:

    /home/vince/photos

On Windows machines `\` is used:

    C:\vince\photos

LaTeX uses the *nix syntax **even** on Windows.

Good practice:

- No spaces in files and/or directory names.
- Have a directory in your folder with your images: `Images`. Refer to those images:

        \includegraphics{./Images/pic.png}

    This helps keep your directory tidy.

## Page formatting

The following in your 'preamble' (before the `\begin{document}`) will use up the full page:

    \usepackage{fullpage}
    \usepackage{parskip}

There are other ways to change the layout of a LaTeX page: [http://en.wikibooks.org/wiki/LaTeX/Page_Layout](http://en.wikibooks.org/wiki/LaTeX/Page_Layout).

## Floating figures

## [cloud.sagemath](https://cloud.sagemath.com/)

The inventor of Sage: [William Stein](http://goo.gl/bkzDDP) has recently been working on a very ambitious project: cloud.sagemath.

> "There are 288 cores, 1216GB RAM and 50TB disk space dedicated to the Sagemath Cloud cluster."

You can read about the progress of cloud.sagemath on G+ but at the moment you can use it as a (more or less) full linux machine with access to:

- Python;
- Sage;
- LaTeX;
- R;
- Bash...

Note that this is an external service (the servers sit at Washington University).

## Plagiarism

Be careful to not not plagiarise. Here are the University's guidelines on plagiarism and unfair practice: [http://cardiff.ac.uk/regis/ifs/plag/](http://cardiff.ac.uk/regis/ifs/plag/).

As long as you reference any work that you use as a source you'll be fine (for example a website from which you have taken some code).

## What you should do next:

- Think of groups and topics for next semester
- **Finish the coursework**
- If anything is still unclear **please** come and see me during office hours.
