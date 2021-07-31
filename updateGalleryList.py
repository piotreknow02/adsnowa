import os
import json

# gallery
file_list = os.listdir("./static/gallery")
if not os.path.exists("./src/node_modules/"):
	os.mkdir("./src/node_modules/")
try:
	file_list.remove(".DS_Store")
except:
	pass
json_list = json.dumps(file_list)
with open("./src/node_modules/galleryList.js", "w") as file:
	file.write("const galleryList = " + json_list + "\nmodule.exports = { galleryList }")
	file.close()

# 2021
file_list = os.listdir("./static/2021")
try:
	file_list.remove(".DS_Store")
except:
	pass
json_list = json.dumps(file_list)
with open("./src/node_modules/2021.js", "w") as file:
	file.write("const galleryList = " + json_list + "\nmodule.exports = { galleryList }")
	file.close()