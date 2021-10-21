from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for, session
import json


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

def format_date(date):
    return datetime.strptime(date, ('%Y-%m-%d %H:%M:%S'))

@app.route('/')
def index():
    return render_template('index.html', clubs=clubs)


@app.route('/showSummary',methods=['POST', 'GET'])
def showSummary():
    if request.method == 'POST':
        try:
            found_club = [club for club in clubs if club['email'] == request.form['email']][0]
            session['club'] = found_club
        except IndexError:
            flash("The email isn't found !")
            return render_template('index.html')
    now = datetime.now()
    club = session.get('club')
    return render_template('welcome.html', club=club, competitions=competitions, now=now, date=format_date)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition and datetime.now() < format_date(foundCompetition['date']):
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return redirect(url_for('showSummary'))


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if placesRequired > 0 and placesRequired < 13:
        if int(club['points']) - placesRequired >= 0 and int(competition['numberOfPlaces']) - placesRequired >= 0:
            club['points'] = int(club['points']) - placesRequired
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
            flash('Great-booking complete!')
            return redirect(url_for('showSummary'))
        else:
            flash('Error, you redeem more points or places than available') 
    else:
        flash("Error, you can't redeem more than 12 and less than 1")
    return render_template('booking.html',club=club, competition=competition)
    


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))