# TestTask Readme 

## Install docker

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
```
1. Create `.env` file inside `aveds_2_test_task` with:
```sh
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=""
USER_UUID="" 
```
Where `USER_UUID` -  is the `id` of the user whose token we will use to run the bot.

1. Run this commands:
```sh
# Copy docker files to root dir
cp aveds_2_test_task/deploy/docker-compose.yml ./ && cp aveds_2_test_task/deploy/Dockerfile ./

# Run docker compose file
sudo docker compose up -d
```

## To stop and delete containers 
```sh
# Warning: It removes containers, volumes and networks.

# If you want to restart/stop better use docker compose restart/stop

sudo docker compose down
```