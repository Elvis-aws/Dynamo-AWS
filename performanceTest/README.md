# Installation
pip3 install locust
locust -V


# start locust server
locust -f performance_test/locustfile.py 

# Run Tests 
locust -f performance_test/locustfile.py
locust -f performance_test/locustfile.py -u 2 -r 2 -t 10s
locust -f performance_test/locustfile.py -u 3 -r 2 -t 10s --headless
locust -f performance_test/locustfile.py -u 2 -r 1 -t 5s --headless --only-summary
locust -f performance_test/locustfile.py -u 3 -r 2 -t 10s --headless --only-summary --tags emp
locust -f performance_test/locustfile.py --config performance_test/locust.conf

# Distributed mode 
locust --config performance_test/master.conf
locust --config performance_test/worker.conf

# Docker compose
docker-compose up --scale worker=4
# Docker 
docker run -p 8089:8089 -v $PWD:/mnt/locust -d locustio/locust -f /mnt/locust/locustfile.py
docker run -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py --html /mnt/locust/report.html --headless --only-summary -u 4 -r 2 -t 10s


# Documentation
https://docs.locust.io/en/1.5.2/running-locust-distributed.html
https://www.youtube.com/watch?v=FDYD2inSSPY&list=PLJ9A48W0kpRKMCzJARCObgJs3SinOewp5&index=18