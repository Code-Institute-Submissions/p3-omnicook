# [Omnicook](https://naturaldev0.github.io/p3-omnicook/)

Code-Institute Project #3 : An cookbook project that shows different varieties of recipe for hobbyist to get inspirations and ideas to jumpstart them in learning how to cook and make delicious form of dishes.
 
 
## UI / UX

### Interface
1. You can refer to the UI through [here](https://drive.google.com/file/d/15hE_VO6VaOnUheitaI-4sei5_7XlH8Kt/view?usp=sharing).

### Experience
User Stores: --> <i>(e.g. As a user type, I want to perform an action, so that I achieve a goal.)</i>

1. <i>(stories ...)</i> As a user type, I want to perform an action, so that I can achieve a goal.
1. <i>(stories ...)</i> As a user type, I want to perform an action, so that I can achieve a goal.
1. <i>(stories ...)</i> As a user type, I want to perform an action, so that I can achieve a goal.
1. <i>(stories ...)</i> As a user type, I want to perform an action, so that I can achieve a goal.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

<i>Users can ...</i>

* Feature #1 - 
* Feature #2 - 
* Feature #3 - 
* Feature #4 - 
* Feature #5 - 
* Feature #6 - 

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

<i>"< Delete this sectiion once done writing ...>"</i>

Things to write in this section are ...

1. Languages, Frameworks, Libraries, and any other tools
1. Structure of the sentence :
    1. [ name ]
    1. [ link to its official site ]
    1. [ short sentence ex ]
    
<i>"< Delete this sectiion once done writing ...>"</i>

1. HTML5 --- *required*
1. CSS3 --- *required*
1. JavaScript --- *required*
    * Use it add in certain functions such as (e.g. click, ready, on ...),
        * Dyanmically generate
1. [JQuery](https://jquery.com)
    * The project uses **JQuery** to simplify DOM manipulation.
1. Python 3
1. Flask
1. MySQL
1. ClearDB
    * *This is required to deploy on Heroku*


## Testing

<i>These are the tests I have done so far...</i>
<hr>

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

<i>[Please take note that your project environment will be different ...]</i>

* The website is currently hosted on Heroku, developed on AWS Cloud 9 IDE platform and the source code is stored on Github Repository. Occasionally, I would perform some lightweight code edits using Microsoft Visual Studio (VS) Code (e.g. README.md).

### Steps deployment

1. Create a new repository for your project on your local computer.
    ```
    git init .                  // initialize repo with all files
    git add .                   // add all files into local staging
    git status                  // check if any files are left out before commiting
    git commit -m "message"     // commit change with message of your files into repo
    ```
2. Add your remote git link for uploading your files onto Github later on.
    ```
    git remote add origin <your-remote-git-link>    // add your remote repo link
    ```
3. Push your files onto your remote
    ```
    git push -u origin master   // upload your files into your remote repo
    ```

4. Should you have the interest to work the files offline, you can do so by cloning a copy.
    ```
    git clone <remote-link>     // Clone the selected repo offline
    ```

NOTE: All commits are pushed to master branch, as currently there is no intention of creating new branches.
<br><br>

## Credits

### Content
* 

### Acknowledgements

<i>- I have took inspirations from the following sites...</i>

Misc

1. [Google Fonts](https://fonts.google.com/) - (Font)

→ Web layout
1. [kinokuniya](https://kinokuniya.com.sg/)
1. [justonecookbook](https://www.justonecookbook.com/)
1. [popular](https://www.popular.com.sg/)

→ Web layout, Fields to implement in DB
1. [allrecipes](https://www.allrecipes.com/)
1. [foodnetwork](https://www.foodnetwork.com/)
1. [bbcgoodfood's cuisines](https://www.bbcgoodfood.com/recipes/category/cuisines)
    * Idea on the ‘Type of cuisines’

→ Web layout content
[foodallergy's common-allergens](https://www.foodallergy.org/common-allergens)
* Idea on the ‘Type of allergens’

***This is for educational use.***