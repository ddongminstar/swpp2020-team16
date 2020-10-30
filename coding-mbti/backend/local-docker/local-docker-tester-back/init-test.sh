#bin/bash

echo "[Sanity Check]Checks if docker, docker-compose, docker-machine is properly installed."

if [ -x "$(command -v docker)" ]; then
    echo "[(1/3) docker is installed.]"
else
    echo "[(1/3) docker is not installed. please install.]"
    echo "aborting..."
    exit 1
fi

if [ -x "$(command -v docker-compose)" ]; then
    echo "[(2/3) docker-compose is installed.]"
else
    echo "[(2/3) docker-compose is not installed. please install.]"
    echo "aborting..."
    exit 1
fi

echo "Checks if docker is running..."
if docker info | grep -Fq "Cannot connect to the Docker daemon"; then
    echo "Docker is not running. please run it before you start this script."
    echo "aborting..."
    exit 1
else
    echo "[Docker is running.]"
fi

containerId=`docker ps | grep django-backend-server | awk '{print $1}'`

echo "Container[ID=$containerId] is the django-backend-server. Testing..."

docker  exec -it "$containerId" /bin/bash -c "cd /deploy/swpp2020-team16/coding-mbti/backend; coverage run --source='.' manage.py test"
