# Amberley's Art Store

The Live App can be found at: [Amberley's Art Store](https://amberley-art-store-fa04ced04eb7.herokuapp.com/)

Amberley's Art Store is an online store for my partner to sell her artwork.

## Project Goals and User Experience

### Project Goals
- Create a fully functioning eCommerce site that allows users to view products.
- Allow users to checkout their purchases seamlessly.
- Save a user's basket when they are logged in.
- Continuously improve the website through updates, bug fixes, and feedback.

Ultimately, the goal of the app is to create a secure and easy way to browse artwork and purchase it.

***

## User Stories

### First Time User
1. **As a first-time user,**  
   I want to be able to view products  
   so that I can purchase them.  
   **Acceptance Criteria:** A user can view products.

2. **As a first-time user,**  
   I want to be able to register  
   so that I am able to have a personal account.  
   **Acceptance Criteria:** The user can register a new account.

3. **As a first-time user,**  
   I want to be able to add products to my basket  
   so that I can save products.  
   **Acceptance Criteria:** Users can view their basket.

4. **As a first-time user,**  
   I want to have a clear navigation menu  
   so that I can easily find what I’m looking for.  
   **Acceptance Criteria:** Users can easily navigate to different sections of the website.

5. **As a first-time user,**  
   I want to see high-quality images of the artwork  
   so that I can appreciate the details.  
   **Acceptance Criteria:** All product images are displayed clearly.

### All Users
6. **As a user,**  
   I want to be able to go back to my basket at any time  
   so that I can review my selected items.  
   **Acceptance Criteria:** Users can save and access their baskets.

7. **As a user,**  
   I want to be able to checkout  
   so that I can finalize my purchase.  
   **Acceptance Criteria:** Users can complete the checkout process successfully.

8. **As a user,**  
   I want to receive confirmation of my order  
   so that I know my purchase was successful.  
   **Acceptance Criteria:** Users receive an order confirmation email.

9. **As a user,**  
   I want to be able to filter products by category  
   so that I can find specific types of artwork easily.  
   **Acceptance Criteria:** Users can see filter options on the store page.

10. **As a user,**  
    I want to be able to view my order history  
    so that I can keep track of my past purchases.  
    **Acceptance Criteria:** Users can access a list of their previous orders.

***

## Design
### Wireframes
Below are the designs that were used as a reference point to build the project. These designs were built while keeping in mind the needs of the above user stories.

#### Home Page
![Image of homepage.html](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/Home-Page.png)

#### Store Page
![Image of store page](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/store-page.png)

#### Item Page
![Image of item page](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/Item-page.png)

#### Order Page
![Image of order page](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/order-page.png)

***

### Database Schema
![Image of database schema](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/models-plan.png)

***

### Colour Choices
![Image of colour schema](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/colour_Schema.png)

***

### Font Selection
Google Fonts was used for all fonts on the website, as it provides simple and clean refined fonts.

#### Oswald
Used for headers
![Image of Oswald font](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/oswald-font.png)

#### Poppins
Used for the rest of the text throughout the website
![Image of Poppins font](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/poppins-font.png)

***

### Features

#### User Registration
The registration page allows users to create a new account to access personalized features. This includes input validation and error handling.

#### Product Listing
A page where all available artworks are displayed with options to filter by category. Each product has a brief description, price, and image.

#### Product Detail Page
Provides detailed information about each artwork, including images, descriptions, and an option to add to the basket.

#### Shopping Basket
Users can add products to their basket and view their selections at any time, ensuring the items are saved even when navigating away from the page.

#### Checkout Process
A streamlined checkout process that allows users to finalize their purchases securely with a confirmation screen.

***

### Future Implementations
- Implement user ratings for products to enhance user interaction.
- Add a feature for users to save favorite artworks for easy access later.
- Include promotional features like discounts and special offers for registered users.
- Enhance mobile responsiveness for a better experience on smaller devices.

***

## Testing

### W3 HTML Validator
* Home: [W3 HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Famberley-art-store-fa04ced04eb7.herokuapp.com%2F)
* Login Page: [W3 HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Famberley-art-store-fa04ced04eb7.herokuapp.com%2Fproducts%2F)
* Store: [W3 HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Famberley-art-store-fa04ced04eb7.herokuapp.com%2Fproducts%2F)

### CSS Validator
* CSS: [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Famberley-art-store-fa04ced04eb7.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

### JavaScript
There were no errors when passing the js through the official JSHint Validator. The below metrics were returned:
* There are 3 functions in this file.
* The function with the largest signature takes 1 arguments, the median is 1.
* The largest function has 8 statements in it, the median is 5
* The most complex function has a cyclomatic complexity value of 3 with the median being 2.

### Lighthouse Accessibility Testing
#### Accessibility Reports: 
* Home [Lighthouse Report](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/lighthouse-home.png)
* Store [Lighthouse Report](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/lighthouse-store.png)
* Profile [Lighthouse Report](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/lighthouse-profile.png)
* Basket [Lighthouse Report](https://github.com/darrenrob25/AmberleyArtStore/blob/main/media/lighthouse-basket.png)

### User Story Testing
Below are the tests for each user story and their results:

| User Story No. | Test Case | Status |
|----------------|-----------|--------|
| 1 | Verify that all products are displayed on the homepage. | **Passed** |
| 2 | Check the registration form and submit with valid information. | **Passed** |
| 3 | Add a product to the basket and verify it appears in the basket view. | **Passed** |
| 4 | Test navigation links to ensure they redirect to the correct pages. | **Passed** |
| 5 | Verify that all product images load without distortion or errors. | **Passed** |
| 6 | Navigate to the basket from various pages and check that it retains items. | **Passed** |
| 7 | Complete a checkout process with valid payment details and verify a success message. | **Passed** |
| 8 | Check email inbox for an order confirmation after completing a purchase. | **Passed** |
| 9 | Use filter options on the store page and verify that results match the selected category. | **Passed** |
| 10 | Access the order history page and verify it displays previous purchases accurately. | **Passed** |

***

### Manual Testing
- Tested across different web browsers (Chrome, Firefox, Safari).
- Ensured the website is responsive and looks good on various device sizes (desktop, tablet, mobile).
- Verified all links function correctly.
- Confirmed that user registration, login, adding to basket, and checkout functionalities work as expected.
- Checked for usability and ensured that navigation is intuitive and user-friendly.
- Verified that all images load correctly and display at the intended size.
- Ensured that form inputs are validated and error messages are displayed appropriately.
- Tested accessibility features, including keyboard navigation and screen reader compatibility.

***

### Bugs
#### Bug 1
The first issue encountered was with product images not loading. This was resolved by ensuring all images were correctly linked and uploaded to the server. Test case passed for image display.

#### Bug 2
Another issue was the checkout process failing due to incorrect payment integration. This was fixed by debugging the payment gateway and ensuring secure transactions. Test case passed for checkout functionality.

***

### Cloning & Forking

#### Fork
1. On GitHub.com, navigate to the [Amberley's Art Store](https://github.com/darrenrob25/AmberleyArtStore) repository.
2. In the top-right corner, click Fork.
3. By default, forks are named the same as their parent repositories.
4. Add a description to your fork.
5. Click Create fork.

#### Clone
1. Above the list of files, click the button that says 'Code'.
2. Copy the URL for the repository.
3. Open Terminal. Change the directory to the location where you want the cloned directory.
4. Type `git clone`, and then paste the URL.
5. Press Enter.

#### Local Deployment
1. Sign up to [Gitpod](https://gitpod.io/).
2. Download the Gitpod browser extension.
3. On GitHub.com, navigate to the [Amberley's Art Store](https://github.com/darrenrob25/AmberleyArtStore) repository.
4. Above the list of files, click the button that says 'Gitpod'.

#### Remote Deployment
1. Log in to your hosting service (e.g., Heroku).
2. Click on the 'Create new app' button.
3. Give your application a unique name, select the closest region to you, and click 'Create app'.
4. Follow the service's instructions for setting up the application.

***

## Credits

### Content
- Processes from the CI eCommerce project were used to help create this website.
- HTML, CSS, Python, and JavaScript code help was taken from W3Schools.
- Bootstrap was used for styling.
- Various [Stack Overflow](https://stackoverflow.com) articles provided guidance.

### Media
* All images were sourced from [Unsplash](https://unsplash.com) and [Pexels](https://www.pexels.com/).
