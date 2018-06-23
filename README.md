# Dormitory Girl Hunter

## Description

Define woman as a person with surname ending with `á`. The script searches persons on the specified floor and block defined by user via parameters. Women are displayed with red bold color.

## Usage

1. Install python3.6

    ```sh
    sudo add-apt-repository ppa:jonathonf/python-3.6

    sudo apt update

    sudo apt-get install python3.6
    sudo apt-get install python3-pip

    python3.6 -m pip install requests
    ```

2. Run

    ```sh
    python3.6 run.py [OPTIONS]
    ```

    OPTIONS:

        Help:
            -h
            --help

        Floor:
            -f=NUMBER
            --floor=NUMBER

        Block:
            -b=BLOCK
            --block=BLOCK

        Specific Room:
            -r=NUMBER
            --room=NUMBER

        Empty Rooms:
            -e
            -empty


### Example


* Help:<br>
    - `./run.py -h`
    - `python3.6 run.py -h`
<br>


* Common usage:<br>
    - `./run.py -b=B05 -f=2`
    - `python3.6 run.py -b=B05 -f=2`
