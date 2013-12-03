# Computing for mathematics handout 10 - File paths, Fullpage, Floating figures, cloud.sagemath and plagiarism.
Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

Some basic Sage code to solve differential equations:

    - ODEs;
    - Systems of ODEs;
    - Numerical solutions of ODEs (for when they can't be solved exactly).

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

## Plagiarism

## What you should do next:

- Work through LaTeX lab sheets.
- **Finish the coursework**
- Contribute to the wiki.
- If anything is still unclear **please** come and see me during office hours.
