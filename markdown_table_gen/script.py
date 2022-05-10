"""
Creates a template markdown file with the table of ingredients per input

pip install -r requirements.txt

"""

from mdutils.mdutils import MdUtils

def main(filename: str, recipe_name: str):

    more_ingredients = True
    table_values = ["Quantity", "Measure", "Ingredient"]
    while more_ingredients is True:
        new_values = input("Enter the next ingredient in this format: <quantity> - <measure> - <ingredient>\n").split("-")
        for element in new_values:
            element = str(element.strip())
        table_values.extend(new_values)
        more_bool = input("Was that the last ingredient? y/n\n")
        if more_bool in ["y", "yes"]:
            more_ingredients = False

    mdFile = MdUtils(file_name = filename, title = recipe_name)

    mdFile.new_header(level = 1, title = "Description")
    mdFile.new_paragraph(input("Type in an intro descriptive paragraph. Information could include how long it takes to make, are there any hard to get ingredients, how many people does it feed, how nice is it etc: \n"))

    mdFile.new_header(level = 1, title = "Ingredients")
    mdFile.new_line()
    num_rows = int(len(table_values) / 3)
    mdFile.new_table(columns = 3, rows = num_rows, text = table_values, text_align = "center")

    mdFile.new_header(level = 1, title = "Method")
    dummy_list = ["", "", ""]
    mdFile.new_list(dummy_list, marked_with = '1')

    mdFile.create_md_file()

filename = input("Filename:\n")
recipe_name = input("Name of the recipe:\n")

main(filename, recipe_name)