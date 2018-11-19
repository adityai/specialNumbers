docker build -t prime-numbers .
docker run -d -p 6379:6379 --name primeredis redis
docker run -d -e DASHING_URL="https://iaditya.herokuapp.com/widgets/prime" -e AUTH_TOKEN="YOUR_AUTH_TOKEN" --link primeredis:primeredis --name prime-numbers prime-numbers

