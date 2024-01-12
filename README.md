
# rein-memorial-wiki
A Memorial to my friend Rein, who loved Wikipedia, in the style of Wikipedia

## Editing

Did you also love Rein? Feel free to make edits and changes! Doing this is simple and should be accessible.

1. Create an account on github or log in if you already have an account. 
    - If you don't want to do this, don't worry, email me `mnoukhov@gmail.com` any changes you'd like to make and I'll do them for you!
2. Click on `text.md` above. This is the main file you need to edit.
3. Click on the upper-right hand pencil button to edit. Now you're editing the file!

### How to Edit

The file is written in a simple format called Markdown. 
- Just write sentences as normal.
- Make something **bold** with `**bold text**` or *italicized* with `*italics*`
- If you'd like to make a link e.g. to [a website](#), use brackets `[link text](urlformylink.com)`
- Drag and drop any photos directly from your computer into the text. It'll show up as a weird link like `![000012](https://github.com/mnoukhov/rein-memorial-wiki/assets/3391297/41fcc595-fec5-4142-8a7e-3d135b649744)`. In the actual Wiki page, it will look like a citation so that when someone hovers over the number, the image will pop up! Move the weird links to wherever you'd like the "citation" to be.

## Extension
Are you looking fork my repo to make a wikipedia-style page yourself? Here's how I did it.

HTML is autogenerated from the markdown to make it easier for everyone to edit and make changes

I use github actions that calls `format_html.py` on `template.html` and `text.md`
To make the action able to change `index.html`, I use a deploy key that I then add as an Action secret so GH actions can access it.
