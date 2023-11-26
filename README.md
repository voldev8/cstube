# CS_Tube

This project is for Counter Strike players who is looking to access necessary and catogorized nade videos by time on youtube.
You can also watch CS livestream on twitch with the most viewers and see top 5.

[heroku link](https://cstube.herokuapp.com)

## Some Notes

- List of all videos sorted by newest first and with a search function.
- Videos are also categorized by map and sorted by location in the map.
- New videos can be added by Add a Video form.
- Each video has
  title,
  timestamp,
  link,
  which map it belongs,
  which site (A,B,Mid),
  video (nade) type (smoke, molly, flash, grenade, strat, misc')
- Most viewed Counter Strike live stream can be watched, also top 5 list with links can be seen.

## Tech Stack / Built With

1. [Django](https://www.djangoproject.com/) - high-level Python Web framework
2. [postgreSQL](https://www.postgresql.org/) - Open Source Relational Database

## DB

```plaintext
accounts_user
+---------------------+--------------+------+-----+---------+----------------+
| Field               | Type         | Null | Key | Default | Extra          |
+---------------------+--------------+------+-----+---------+----------------+
| id                  | int          | NO   | PRI | NULL    | auto_increment |
| username            | varchar(150) | NO   | UNI | NULL    |                |
| password            | varchar(128) | NO   |     | NULL    |                |
| email               | varchar(254) | NO   |     | NULL    |                |
| first_name          | varchar(30)  | NO   |     | NULL    |                |
| last_name           | varchar(30)  | NO   |     | NULL    |                |
| date_joined         | datetime(6)  | NO   |     | NULL    |                |
| favorite_links      | manytomany   | YES  |     | NULL    |                |
| favorite_videos     | manytomany   | YES  |     | NULL    |                |
+---------------------+--------------+------+-----+---------+----------------+

catalog_maps
+---------------------+--------------+------+-----+---------+----------------+
| Field               | Type         | Null | Key | Default | Extra          |
+---------------------+--------------+------+-----+---------+----------------+
| id                  | int          | NO   | PRI | NULL    | auto_increment |
| name                | varchar(200) | NO   |     | NULL    |                |
+---------------------+--------------+------+-----+---------+----------------+

catalog_videos
+---------------------+--------------+------+-----+---------------------+----------------+
| Field               | Type         | Null | Key | Default             | Extra          |
+---------------------+--------------+------+-----+---------------------+----------------+
| id                  | int          | NO   | PRI | NULL                | auto_increment |
| title               | varchar(40)  | NO   |     | NULL                |                |
| created_at          | datetime(6)  | NO   |     | NULL                |                |
| link                | varchar(300) | NO   |     | NULL                |                |
| map_belong_id       | int          | YES  | MUL | NULL                |                |
| type_video          | varchar(6)   | YES  |     | NULL                |                |
| site                | varchar(3)   | YES  |     | a                   |                |
| admin_permission    | tinyint(1)   | NO   |     | 0                   |                |
+---------------------+--------------+------+-----+---------------------+----------------+

catalog_links
+---------------------+--------------+------+-----+---------------------+----------------+
| Field               | Type         | Null | Key | Default             | Extra          |
+---------------------+--------------+------+-----+---------------------+----------------+
| id                  | int          | NO   | PRI | NULL                | auto_increment |
| title               | varchar(40)  | NO   |     | NULL                |                |
| created_at          | datetime(6)  | NO   |     | NULL                |                |
| link                | varchar(300) | NO   |     | NULL                |                |
| map_belong_id       | int          | YES  | MUL | NULL                |                |
| type_video          | varchar(6)   | YES  |     | NULL                |                |
| site                | varchar(3)   | YES  |     | a                   |                |
+---------------------+--------------+------+-----+---------------------+----------------+
```

## REQUIRED ENVIRONMENT VARIABLES:

[Twitch Authentication](https://dev.twitch.tv/docs/authentication)

    TWITCH_CLIENT_SECRET
    In views.py twitch_auth function client_id should be changed to yours.
    client_secret should be authenticated from twitch.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

MIT © Volkan Uyarer
