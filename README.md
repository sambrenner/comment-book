# Comment Book

Comment Book extracts the comments from your code and converts them to Markdown.

The Markdown file can be converted to `icml`, a format that InDesign will consume for styling and layout. To do this, first download [`pandoc`](https://github.com/jgm/pandoc/releases/). Then run

    pandoc -s -f markdown -t icml -o my-book.icml my-book.md

The provided python file will probably need some tweaking for your repo's tastes. For example, you might have to add a case to the switch statement that checks a file's extension and applies the revelant regexes.

## Regexes Used

These aren't always perfect - one major problem is that they don't check if they are part of a string. But they get the job done. Pull requests welcome!

### `// comment`

    (?<!http:)\/\/.*\n

### `/* comment */`

    \/\*.*?\*\/

### `<!-- comment -->`

    \<!--.*?--\>
    
### `{* comment *}`

    {\*.*?\*}
    
### `# comment`

    #.*\n

    
### `''' comment '''`

    '''.*?'''
    

