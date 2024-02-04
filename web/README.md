Build:
docker build --tag nafnaapp-backend .

Run:
docker run -d -p 5000:5000 --name bakendi nafnaapp-backend

Stop:
docker stop bakendi
