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

# Replace each <h2> and <h3> with a <span>
for h_tag in h2_and_h3_tags:
    name = h_tag.get_text(strip=True)
    span = soup.new_tag("span")
    span["class"] = "mw-headline"
    span["id"] = name
    span.string = name

    h_tag.string = ""
    h_tag.append(span)
    print(span)

start_content.insert_after(text_soup)

with open("index.html", "w") as file:
    file.write(str(soup))
