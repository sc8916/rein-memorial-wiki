from bs4 import BeautifulSoup
import markdown

with open("template.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

start_content = soup.find("div", {"id": "start"})

with open("text.md", "r") as file:
    md_content = file.read()
    md = markdown.markdown(md_content)

text_soup = BeautifulSoup(md, "html.parser")

### replace all images with links that show image on hover

image_tags = text_soup.find_all("img")

hover_image_string = """
<sup class="reference">
<a class="image-link">
    [{index}]
    {image_tag}
</a></sup>
"""

for i, image_tag in enumerate(image_tags):
    image_tag["class"] = "hover-image"
    hover_image_tag = hover_image_string.format(image_tag=image_tag, index=i + 1)
    hover_image_soup = BeautifulSoup(hover_image_tag, "html.parser")
    image_tag.replace_with(hover_image_soup)

### format h2 and h1 as wikipedia does

wikipedia_heading = """
<span class="mw-headline" id="Bank_of_Estonia">Bank of Estonia</span>
"""

h2_and_h3_tags = text_soup.find_all(["h2", "h3"])
headings_nested = []

# Replace each <h2> and <h3> with a <span>
for h_tag in h2_and_h3_tags:
    name = h_tag.get_text(strip=True)
    span = soup.new_tag("span")
    span["class"] = "mw-headline"
    span["id"] = name
    span.string = name

    h_tag.string = ""
    h_tag.append(span)

    if h_tag.name == "h2":
        headings_nested.append((name, []))
    elif h_tag.name == "h3":
        headings_nested[-1][1].append(name)

start_content.insert_after(text_soup)

start_heading = soup.find("li", {"id": "toc-mw-content-text"})

h2_string = """
<li class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded" id="toc-{heading_name}">
<a class="vector-toc-link" href="#{heading_name}">
<div class="vector-toc-text">
<span class="vector-toc-numb">1</span>{heading_name}</div>
</a>
<button aria-controls="toc-{heading_name}-sublist" aria-expanded="true" class="cdx-button cdx-button--weight-quiet cdx-button--icon-only vector-toc-toggle">
<span class="vector-icon vector-icon--x-small mw-ui-icon-wikimedia-expand"></span>
<span>Toggle {heading_name} subsection</span>
</button>
<ul class="vector-toc-list" id="toc-{heading_name}-sublist">
</ul>
</li>
"""

h3_string = """
<li class="vector-toc-list-item vector-toc-level-2" id="toc-{heading_name}">
<a class="vector-toc-link" href="#{heading_name}">
<div class="vector-toc-text">
<span class="vector-toc-numb">1.3</span>{heading_name}</div>
</a>
<ul class="vector-toc-list" id="toc-{heading_name}-sublist">
</ul>
</li>
"""

h2_soups = []
for h2_name, h3s in headings_nested:
    h3_soups = []
    for h3_name in h3s:
        h3_str = h3_string.format(heading_name=h3_name)
        h3_soups.append(BeautifulSoup(h3_str, "html.parser"))

    h2_str = h2_string.format(heading_name=h2_name)
    h2_soup = BeautifulSoup(h2_str, "html.parser")
    h2_ul = h2_soup.find("ul", {"id": f"toc-{h2_name}-sublist"})
    for h3_soup in h3_soups:
        h2_ul.append(h3_soup)

    h2_soups.append(h2_soup)

for h2_soup in reversed(h2_soups):
    start_heading.insert_after(h2_soup)

with open("index.html", "w") as file:
    file.write(str(soup))
