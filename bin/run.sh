docker rm gol
docker run -it -p 3000:3000 --env-file=.env --name=gol games-of-life
