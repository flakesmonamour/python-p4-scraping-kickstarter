from bs4 import BeautifulSoup
import ipdb

def create_project_dict():
    # Read the HTML content from the file
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    # Parse the HTML with BeautifulSoup
    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}

    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title = project.select("h2.bbcard_name strong a")[0].text
        
        projects[title] = {
            'image_link': project.select("div.project-thumbnail a img")[0]['src'],  # Corrected attribute access
            'description': project.select("p.bbcard_blurb")[0].text,
            'location': project.select("ul.project-meta span.location-name")[0].text,
            'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%", "")
        }
    
    # Return the projects dictionary
    return projects
