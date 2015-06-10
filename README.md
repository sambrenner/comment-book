# Comment Book

Comment Book extracts the comments from your code and converts them to Markdown.

The Markdown file can be converted to `icml`, a format that InDesign will consume for styling and layout. To do this, first download [`pandoc`](https://github.com/jgm/pandoc/releases/). Then run

    pandoc -s -f markdown -t icml -o my-book.icml my-book.md
