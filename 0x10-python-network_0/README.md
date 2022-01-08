![Holberton](https://user-images.githubusercontent.com/85451781/140782830-f3f4a341-3d98-4a6e-89d2-76d684c80e9e.png)

# 0x10. Python - Network #0

## Learning Objectives

### General

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## To obtain testing power in the provided container, follow the steps below:

Download holbertonschool image into docker from https://hub.docker.com/u/holbertonschool

For this proyect: Image = holbertonschool/299

- **Execute the following commands:**

  1. sudo docker pull <image>
  2. sudo docker run <image>
  3. sudo docker ps
  4. sudo docker exec -it <id> sh
  5. curl -sI <IP:PORT>

## Tasks

### 0. cURL body size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- The size must be displayed in bytes
- You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```bash
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$
```

**Repo:**

- GitHub repository: holbertonschool-higher_level_programming
- Directory: 0x10-python-network_0
- File: 0-body_size.sh

### 1. cURL to the end

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

- Display only body of a 200 status code response
- You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```bash
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$
```

**Repo:**

- GitHub repository: holbertonschool-higher_level_programming
- Directory: 0x10-python-network_0
- File: 1-body.sh

### 2. cURL Method

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

- You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```bash
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$
```

**Repo:**

- GitHub repository: holbertonschool-higher_level_programming
- Directory: 0x10-python-network_0
- File: 2-delete.sh

### 3. cURL only methods

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

- You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```bash
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$
```

**Repo:**

- GitHub repository: holbertonschool-higher_level_programming
- Directory: 0x10-python-network_0
- File: 3-methods.sh

### 4. cURL headers

Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

- A header variable X-School-User-Id must be sent with the value 98
- You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```bash
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$
```

**Repo:**

- GitHub repository: holbertonschool-higher_level_programming
- Directory: 0x10-python-network_0
- File: 4-header.sh

### 5. cURL POST parameters

Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

- A variable email must be sent with the value test@gmail.com
- A variable subject must be sent with the value I will always be here for PLD
- You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```bash
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$
```

**Repo:**

- GitHub repository: holbertonschool-higher_level_programming
- Directory: 0x10-python-network_0
- File: 5-post_params.sh

### 6. Find a peak

**Technical interview preparation:**

- You are not allowed to google anything
- Whiteboard first

Write a function that finds **a peak** in a list of unsorted integers.

- Prototype: def find_peak(list_of_integers):
- You are not allowed to import any module
- Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
- 6-peak.py must contain the function
- 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
- **Note:** there may be more than one peak in the list

```bash
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt
2 6-peak.txt
guillaume@ubuntu:~/0x10$
```

**Repo:**

- GitHub repository: holbertonschool-higher_level_programming
- Directory: 0x10-python-network_0
- File: 6-peak.py, 6-peak.txt
