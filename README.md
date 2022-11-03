<!-- PROJECT LOGO -->
<br />
<div align="center">
    <a href="https://uninest-app.herokuapp.com/home">
    <img src="app/static/imgs/Brand-Logo-Inline+FullColour.svg" alt="Logo" width="200" height="50">
    </a>
<p align="center">
    <br />
    <a href="https://uninest-app.herokuapp.com/home">Click here to access website</a>
    <br />
</p>
</div>
    
## About The Project

FIT3163/FIT3164 Data Science Group Project (2022)

A Flask web application that recommends a suburb in Victoria, Australia for students to live in based on rental budget, commute to university, environment, public transport availability, crime rates, and population demographic in the suburb.

## Description

Australia's higher education industry is ever-increasing with high demand from both domestic and international students. While searching for accommodation, students first need to consider the suburb where they want to live. Student’s typically consider many varying details about suburbs when researching their options; this process can be very time consuming and mentally demanding due to its importance and effect on their life. If not completed properly and with care, a student could potentially select a non-ideal suburb and miss out on what is best for their preferences. This is especially true for international students who don’t have the benefit of understanding the culture and other relevant details about Australian, and more specifically, Victorian living.

This clearly necessitates some program which automates this process of suburb selection for students by finding an optimal suburb given a student’s preferences. The program would need to be simple and user friendly so that the program is more appealing than the alternative which is to manually search for a suburb.

## Technicality

The application uses a decision tree model using the Python library sklearn which was trained on generated data which used official Australian Bureau of Statistics Census data from 2021 to generate said data. The application uses the Flask framework (which is built using Python) for handling the server-side, and uses plain HTML, CSS, and JS for the client-side of the application. Additionally, the application uses the Google Maps API to improve the results returned to the user by providing a visual representation of the area recommended and encourages the user to explore their recommendation further. The application also provides brief summaries of the important statistics about each suburb to aid the user in understanding why this suburb would be good for them during their studies. 

## Important Notes
- Please access the app on a PC/Laptop for the full experience.
- Only the training data is included under the data folder. Most data used in our application is not published due to file size limits on GitHub.
- The trained decision tree model pickle (.pkl) file is not included in the repository due to file size limits on GitHub.

## Website Pages

<a href="https://uninest-app.herokuapp.com/home">Home</a> | 
<a href="https://uninest-app.herokuapp.com/map">Map</a> | 
<a href="https://uninest-app.herokuapp.com/data">Data</a> | 
<a href="https://uninest-app.herokuapp.com/news">News</a> | 
<a href="https://uninest-app.herokuapp.com/privacy-policy">Privacy Policy</a> | 
<a href="https://uninest-app.herokuapp.com/terms-and-conditions">Terms & Conditions</a> | 
<a href="https://uninest-app.herokuapp.com/help">Help</a>  

## Repository Contents

``` txt
├─ ...
└─ 📁 repo         
    ├─ 📁 app                                       // Source code for WebApp front and back end.                      
    ├─ 📁 assets                                    // Research, inspiration, and developed designs and concepts used in the creation of the software.
    ├─ 📁 data                                      // Raw (original) versions of all datasets (used and considered) including the source of every dataset.
    ├─ 📁 notebooks                                 // Development Jupyter notebooks.
    └─ 📄 wsgi.py                                   // Flask web application run.
```

## Authors

- Jacob Low
- Cody Lewis 
- Jonathan Daswan 
- Chun Mok
