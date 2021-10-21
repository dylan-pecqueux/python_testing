from locust import HttpUser, task

class ProjectPerfTest(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def showSummary(self):
        self.client.post('/showSummary', {"email": "john@simplylift.co"})

    @task
    def book(self):
        self.client.get('/book/Fall%20Classic/Simply%20Lift')

    @task
    def purchasePlaces(self):
        self.client.post('/purchasePlaces', {"competition": "Spring Festival", "club": "Simply Lift", "places": "13"})