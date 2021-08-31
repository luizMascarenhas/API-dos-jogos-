import json 
import requests  

class RequestApi:      
    def __init__(self):         
        self.token = 'ab9e4b8c9217438b85a0f9cf94d0bf00'
        self.headers = {'X-Auth-Token': self.token}             
    
    def request(self, team):         
        url = f'https://api.football-data.org/v2/teams/{team}/matches?status=SCHEDULED'              
        session = requests.Session()         
        response = session.get(url, headers=self.headers)          
        return json.loads(response.text)       
    
    def get_next_game(self, response):
        try: 
            competition = response['matches'][0]['competition']['name']         
            home_team = response['matches'][0]['homeTeam']['name']         
            away_team = response['matches'][0]['awayTeam']['name']          
            return f'Competição: {competition} - JOGO: {home_team} x {away_team}'
        except:
            return 'Time não encontrado'     
        
    def run(self):         
        response = self.request(team=87)         
        next_game = self.get_next_game(response=response)         
        print(next_game)   
        
api = RequestApi() 
api.run()