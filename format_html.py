from bs4 import BeautifulSoup
import markdown

with open("template.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

start_content = soup.find("div", {"id": "start"})

with open("text.md", "r") as file:
    md_content = file.read()
    md = markdown.markdown(md_content)

text_soup = BeautifulSoup(md, "html.parser")


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


start_content.insert_after(text_soup)

with open("index.html", "w") as file:
    file.write(str(soup))
