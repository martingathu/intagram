# Personal gallery
A personal gallery application that allow users to display their photos for others to see.
   

## Built By [Martin Gathu](https://github.com/martingathu/)

## Description
Personal gallery is a web application that allow user to display their photos for others to see. Other users can view and also share available images by copying the image link.

#### You can view the site at: https://martingathupersonalgallery.herokuapp.com/

## User Stories
These are the behaviours/features that the application implements for use by a user. As a user I would like to:

* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo.
* Search for different categories of photos.
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv


### Cloning
* In your terminal:
        
        $ git clone https://github.com/martingathu/personal-gallery
        $ cd personal-gallery

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python 
        
* Installing django and other Modules

        $ python3.6 -m pip install django
        $ python3.6 -m pip install Flask-Bootstrap
       
        
        
* To run the application, in your terminal:
        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test image
   
## Technologies Used
* Python3.6
* Django


## License
MIT &copy;2020 [Martin Gathu](https://github.com/martingathu/)