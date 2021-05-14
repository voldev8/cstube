# CS:GO_Tube
This project is for cs:go players who is looking to access necessary and catogorized nade videos by time on youtube. 
You can also watch csgo livestream on twitch with the most viewers and see top 5.

[heroku link](https://csgotube.herokuapp.com)


## Some Notes
List of all videos sorted by newest first and with a search function.
Videos are also categorized by map and sorted by location in the map.
New videos can be added by Add a Video form.
Each video has
    title,
    timestamp,
    link,
    which map it belongs,
    which site, (A,B,Mid)
    video (nade) type (smoke, molly, flash, grenade, strat, misc')
Most viewed cs:go live stream can be watched, also top 5 list with links can be seen.


## Tech Stack / Built With
1. [Django](https://www.djangoproject.com/) - high-level Python Web framework
2. [postgreSQL](https://www.postgresql.org/)  - Open Source Relational Database

## REQUIRED ENVIRONMENT VARIABLES:

    TWITCH_CLIENT_SECRET = [Twitch Authentication](https://dev.twitch.tv/docs/authentication)
    In views.py twitch_auth function client_id should be changed to yours.
    client_secret should be authenticated from twitch.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

MIT © Volkan Uyarer
