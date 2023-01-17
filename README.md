# New repo: https://github.com/Georeactor/reddit-one-ups

Datasets: https://huggingface.co/datasets?search=georeactor+one_ups


## DeepClapback

A Reddit comment dataset which searches for 'clapbacks' (comments
 which are scored higher than the original comments) and
 set up CSVs for Google AutoML to build a classification model.

Article: "Can DeepClapback learn to lol?" https://medium.com/@mapmeld/can-deepclapback-learn-when-to-lol-e4a2092a8f2c

## Running with cloud services
- sudo apt-get install python3-pip postgresql-client-10 postgresql-client-common transmission-cli
- cd /mnt/DISK
- bzip -d /mnt/DISK/reddit_data/year/RC_YEAR-MONTH.bz2
- python3 reddit_json_converter.py
- python3 reddit_comment_sql.py

## Torrent Warning

Downloading Reddit data as <a href="http://academictorrents.com/details/85a5bd50e4c365f8df70240ffd4ecc7dec59912b">a torrent from AcademicTorrents</a>, may be flagged by your work, school, ISP, VPN or other watchers. Consider your connection, tread carefully.

## Content Warning

Comments and responses in the torrent, 'clapback', and NOMEME datasets, all include NSFW language and links!

## License

Reddit comments are properties of Reddit and comment owners using their Terms of Service

Code is public domain
