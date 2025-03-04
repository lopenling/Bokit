class Transifex:

    '''API wrapper for managing various operations on Transifex.'''
    
    def __init__(self, org, auth):

        '''Initializes the Transifex API wrapper.
        org | string | The organization slug.
        auth | string | The API token.

        '''
        
        import json
        import requests
        
        self.json = json
        self.requests = requests
        
        self.auth = auth
        self.org = org
        
        self.headers = {"accept": "application/vnd.api+json",
                        "content-type": "application/vnd.api+json",
                        "authorization": "Bearer " + self.auth}
        
    def list_teams(self):

        '''Lists all teams in the organization.'''

        out = []

        url = "https://rest.api.transifex.com/teams?filter[organization]=o%3A" + self.org

        response = self.requests.get(url, headers=self.headers)

        data = self.json.loads(response.text)['data']

        for i in range(len(data)):
            out.append(data[i]['id'])

        return out
    
    def list_projects(self):

        '''Lists all projects in the organization.'''

        out = []
        
        url = "https://rest.api.transifex.com/projects?filter[organization]=o%3A" + self.org

        response = self.requests.get(url, headers=self.headers)

        data = self.json.loads(response.text)['data']

        for i in range(len(data)):
            out.append(data[i]['id'])

        return out
    
    def project_details(self, project_slug):

        '''Lists all projects in the organization.
        project_slug | string | The project slug.
        '''

        url = "https://rest.api.transifex.com/projects/o%3A" + self.org + "%3Ap%3A" + project_slug
        
        response = self.requests.get(url, headers=self.headers)

        print(response.text)

    def project_resources(self, project_slug):

        '''Lists all projects in the organization.
        project_slug | string | The project slug.
        '''
        
        url = "https://rest.api.transifex.com/resources/o%3A" + self.org + "%3Ap%3A" + project_slug
        
        response = self.requests.get(url, headers=self.headers)

        print(response.text)  
        
    def create_project(self, name, slug, team):

        '''Creates a new project.
        name | string | The project name.
        slug | string | The project slug.
        team | string | The team slug.
        '''

        payload = {
            "data": {
                "attributes": {
                    "slug": slug,
                    "name": name,
                    "machine_translation_fillup": False,
                    "private": True,
                    "translation_memory_fillup": False
                },
                "relationships": {
                    "organization": {
                        "data": {
                            "type": "organizations",
                            "id": "o:" + self.org
                        }
                    },
                    "source_language": {
                        "data": {
                            "type": "languages",
                            "id": "l:bo"
                        }
                    },
                    "team": {
                        "data": {
                            "type": "teams",
                            "id": 'o:' + self.org + ':t:' + team
                        }
                    },
                },
                "type": "projects"
            }
        }
        
        url = "https://rest.api.transifex.com/projects"

        payload = self.json.dumps(payload)

        response = self.requests.post(url, data=payload, headers=self.headers)

        return response.text

    def read_text(self, project_slug, resource_slug, language_code):

        '''Reads text from a transifex project and resource.
        
        project | str | transifex project
        resource | str | transifex resource
        '''

        import requests
        import json

        headers = {
            "accept": "application/vnd.api+json",
            "authorization": "Bearer " + self.auth
        }

        # Get the source strings and meta
        strings_url = "https://rest.api.transifex.com/resource_strings?filter[resource]=o:"
        strings_url += self.org + ':p:' + project_slug + ':r:' + resource_slug
        strings_url += '&limit=1000'

        response = requests.get(strings_url, headers=headers)
        strings_json = json.loads(response.text)

        # Get the translations    
        translation_url = "https://rest.api.transifex.com/resource_translations?filter[resource]=o:"
        translation_url += self.org + ':p:' + project_slug + ':r:' + resource_slug
        translation_url += "&filter[language]=l:" + language_code
        translation_url += '&limit=1000'

        response = requests.get(translation_url, headers=headers)
        translation_json = json.loads(response.text)
        
        return strings_json, translation_json
