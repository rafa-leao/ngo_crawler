# ngo_crawler

This is a WebCrawler for NGOs from [Transparencia Social](http://transparenciasocial.com.br/ongs).

This project was specially made for [Donnu](http://donnu.com.br/).

## How to set the project up and running

- There are 2 Shell scripts to set the project up locally and run it:

    - ``` $ ./setup.sh ```  
        - Sets your ambient up. You must have [Pip](https://pip.pypa.io/en/stable/) and [Virtualenv](https://virtualenv.pypa.io/en/latest/) installed;

    - ``` $ ./run.sh ``` 
        - Executes the crawler. It'll only works if you had set the ambient up;
        - The information obtained goes to a csv file called final_file.csv and you decides to which directory it is placed

    - To enable executing permissions run: ``` $ chmod +x *.sh ```
