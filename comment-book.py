#!/usr/bin/python

# http://rubular.com/ is helpful for the regexes.
# to bring the markdown into indesign, download pandoc from https://github.com/jgm/pandoc/releases/
# then run:
# pandoc -s -f markdown -t icml -o my-book.icml my-book.md
# the .icml file can be imported and styled by indesign.

import os
import re
import sys

output = open("my-book.md", "w")

def find_comments_in_file(file_path):
    global output

    try:
        buffer = open(file_path).read()

        file_path_no_ext, file_ext = os.path.splitext(file_path)

        block_comments = slash_comments = angle_comments = smarty_comments = quote_comments = pound_comments = None

        if file_ext == ".js" or file_ext == ".json":
            block_comments = re.findall("(\/\*.*?\*\/)", buffer, re.DOTALL)
            slash_comments = re.findall("(?<!http:)\/\/.*\n", buffer)

        elif file_ext == ".css":
            block_comments = re.findall("(\/\*.*?\*\/)", buffer, re.DOTALL)

        elif file_ext == ".html":
            angle_comments = re.findall("(\<!--.*?--\>)", buffer, re.DOTALL)
            smarty_comments = re.findall("({\*.*?\*})", buffer, re.DOTALL)

        elif file_ext == ".py":
            pound_comments = re.findall("(#.*\n)", buffer)
            quote_comments = re.findall("('''.*?''')", buffer, re.DOTALL)

        elif file_ext == ".php":
            pound_comments = re.findall("(#.*\n)", buffer)
            block_comments = re.findall("(\/\*.*?\*\/)", buffer, re.DOTALL)
            slash_comments = re.findall("(?<!http:)\/\/.*\n", buffer)

        else:
            pound_comments = re.findall("(#.*\n)", buffer)

        for comment_grp in [pound_comments,block_comments,slash_comments,smarty_comments,quote_comments,angle_comments]:
                if comment_grp:
                    output.write("## `%s`\n" % file_path.replace('../',''))

                    for comment in comment_grp:
                        if not comment.endswith("\n"):
                            comment = "%s\n" % comment

                        output.write("```\n%s```\n\n" % comment)

        buffer = None
    except Exception, e:
        print e
        pass

for root, dirs, files in os.walk("./"):
    for file in files:
        file_path = os.path.join(root, file)

        # add any folders or file extensions you want to ignore here
        if re.search("(\.md)|(git)|(\.eot)|(\.woff)|(\.svg)|(\.ttf)|(\.jpg)|(\.gif)|(\.png)", file_path) is None:
            find_comments_in_file(file_path)
