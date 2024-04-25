import os
import re
import logging


logging.basicConfig(level="INFO",
                    format="%(asctime)s - %(levelname)s - %(message)s"
        )
tags_pattern = re.compile(r"(#|--)\s(.*)")
problem_name = re.compile(r"^.*?([^\\\/]+).(py|sql)$")

ps_platform = [folder for folder in os.listdir() if os.path.isdir(folder) and folder != ".git"]
ps_platform.sort()
ps_platform

def get_solution_tags(solution_path):
    with open(solution_path, "r") as file:
        line = file.readline()
        try:
            return tags_pattern.match(line).group(2)
        except:
            logging.info(f"There is no Tags in the file: {solution_path}")
            return None
        
def extract_content():
    content_dict = {}
    for platform in ps_platform:
        technologies = os.listdir(platform)
        technologies.sort()
        content_dict[platform] = {}
        for technology in technologies:
            technology_path = f"{platform}/{technology}"
            raw_paths = [*map(lambda x: os.path.join(technology_path, x), os.listdir(technology_path))]
            solutions_paths = []
            while(raw_paths):
                solution_path = raw_paths.pop()
                if os.path.isdir(solution_path):
                    raw_paths += [*map(lambda x: os.path.join(solution_path, x), os.listdir(solution_path))]
                else:
                    solutions_paths.append(solution_path)
            solutions_paths.sort()
            content_dict[platform][technology] = [(solution, get_solution_tags(solution)) for solution in solutions_paths]
    return content_dict

def create_content_table(content_dict):
    table = "| Platform | Technology | Solutions | Tags |\n" \
            "| --- | --- | --- | --- |\n"
    for platform, technologies in content_dict.items():
        tech_names = list(technologies.keys())
        n = len(tech_names)
        for i in range(n):
            tech_name = tech_names[i]
            solutions = technologies[tech_name]
            m = len(solutions)
            for j in range(m):
                row = "| {} | {} | {} | {} |\n"
                name = "[{}]({})".format(problem_name.match(solutions[j][0]).group(1), solutions[j][0])
                if i == 0 and j == 0:
                        table += row.format(platform, tech_name, name, solutions[j][1])
                elif i != 0 and j == 0:
                        table += row.format("", tech_name, name, solutions[j][1])
                else:
                        table += row.format("", "", name, solutions[j][1])
    return table

def update_readme(content_table):
    with open("README.md", "r") as file:
        content = ""
        lines = file.readlines()
        for line in lines:
            content += line
            if line == "## Content Table":
                content = content + "\n\n" + content_table
                break
    with open("README.md", "w") as file:
        file.write(content)




if __name__ == "__main__":
    content_dict = extract_content()
    table = create_content_table(content_dict)
    update_readme(table)

