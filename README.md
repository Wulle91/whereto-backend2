# Whereto

Whereto is a travel companion app that revolutionizes the way users explore new cities. With Whereto, travelers have a wealth of information at their fingertips to make their journeys more enjoyable and enriching. The app allows users to effortlessly discover recommendations from fellow travelers, immerse themselves in captivating user-generated posts, and curate their own personalized travel bucket lists.

Whether you're seeking hidden gems, popular attractions, or delightful dining experiences, Whereto provides valuable insights to help you make informed decisions. The app goes beyond traditional travel guides by fostering a vibrant community where users can connect, share their travel stories, and engage in discussions. From exhilarating adventures to cultural festivals, Whereto keeps users informed about events and promotions happening near them, even when they're at home.

Whereto empowers travelers to explore with confidence and discover the essence of each city they visit. With its intuitive interface and user-friendly features, the app becomes an indispensable companion that enhances every step of the travel experience. From planning to reminiscing, Whereto ensures that every journey is filled with memorable moments and extraordinary discoveries.


### how to use

Whereto is a dynamic travel companion app that allows users to create profiles, share posts, discover exciting locations, engage with others through likes and comments, and stay connected with the travel community. It offers a range of features designed to enhance the user experience and facilitate exploration.

Upon creating an account and logging in, users can create their profiles, storing their information securely in the app's database. With their profile set up, users can dive into the world of travel and start sharing their experiences through posts. When creating a post, the location is automatically detected and associated with the content, providing context to other users.

The app's home page serves as a hub for users to discover posts from travelers worldwide. It showcases an array of captivating content, including travel stories, recommendations, and insights shared by fellow users. This immersive feed allows users to stay inspired, gain valuable travel information, and connect with others who share their passion for exploration.

To foster connections within the community, Whereto enables users to follow other users or specific locations of interest. By following people, users can stay updated on their latest posts, recommendations, and travel experiences. Similarly, following locations allows users to receive updates on popular places, upcoming events, and promotions.

Engagement is encouraged through likes and comments. Users can express appreciation for posts by liking them and leave thoughtful comments to spark conversations and provide feedback. This interaction creates a sense of camaraderie and encourages a supportive community where users can learn from one another and share their perspectives.

In addition to user-generated content, Whereto provides a comprehensive view of locations near the user. Users can easily explore places of interest, see their popularity based on likes and comments, and discover any popular events happening nearby. This feature enables users to stay informed about local activities, ensuring they make the most of their travel experiences.

Whereto empowers travelers to document their journeys, connect with like-minded individuals, and uncover hidden gems worldwide. With its intuitive interface, personalized content, and engagement-focused features, the app creates a vibrant and immersive travel community. Whether users seek inspiration, practical recommendations, or connections with fellow explorers, Whereto is the ultimate companion for their travel adventures.



### Featurs

1. Profile Creation: Users can create personalized profiles to showcase their travel preferences, experiences, and interests.

2. Post Creation: Users can create and share posts, including travel stories, recommendations, photos, and descriptions.

3. Automatic Location Detection: The app automatically associates location information with user-generated posts, providing context and making it easier for others to discover relevant content.

4. Location Discovery: Users can explore and discover exciting locations worldwide, accessing detailed information, ratings, reviews, and photos shared by the community.

5. Home Feed: The app's home feed displays a curated selection of posts from users worldwide, allowing users to stay inspired and informed about travel experiences and recommendations.

6. Following: Users can follow other users and specific locations, receiving updates on their latest posts and recommendations.

7. Likes and Comments: Users can engage with posts by liking them and leaving comments, fostering interaction and conversations within the community.

8. Nearby Locations: The app provides information about locations near the user, allowing them to discover popular places, events, and promotions in their vicinity.

9. Personalized Recommendations: Whereto offers personalized recommendations based on user preferences, helping users find places that match their interests and travel style.

10. Event Updates: Users can stay informed about local events, festivals, exhibitions, and other activities happening near them or in their selected cities.

11. Travel Bucket List: Users can create a travel bucket list, curating a collection of destinations they want to visit, and track their progress.


## Data Model 

1. Profile: The Profile model represents a user profile associated with the User model from Django's built-in authentication system. It contains fields for the profile owner (one-to-one relationship with User), creation and update timestamps, profile name, content, and an optional profile image. The model allows users to create and customize their profiles within the app.

2. Post: The Post model represents a user-generated post within the app. It is linked to the User model through a foreign key relationship, indicating the owner of the post. The model includes fields for creation and update timestamps, post name, address, image URL, title, content, and an optional image. Posts can be created by users to share their travel experiences, stories, and recommendations.

3. Location: The Location model represents a specific location within the app. It includes fields for the location name, address, creation timestamp, and an optional image URL. This model allows users to discover and explore various locations, which can be associated with posts and provide contextual information about the places being discussed.

4. Like: The Like model represents a user's like or appreciation for a specific post. It establishes a many-to-one relationship with both the User model and the Post model. The model includes fields for the owner (the user who liked the post), the post being liked, and a creation timestamp. Users can like posts to show their support and engagement with the content.

5. Follower: The Follower model tracks the relationship between users for the purpose of following other users. It establishes a many-to-one relationship with the User model, representing the user who initiates the follow action, and another User model as the followed user. The model includes a creation timestamp. Users can follow each other to stay connected, receive updates, and engage with each other's posts.

6. FollowLocation: The FollowLocation model represents the relationship between a user and a specific location they choose to follow. It establishes a many-to-one relationship with the User model and the Location model, allowing users to follow locations of interest. The model includes a creation timestamp. Users can follow locations to receive updates, discover relevant posts, and stay informed about events or promotions happening at those locations.

7. Comment: The Comment model represents a user's comment on a specific post. It establishes a many-to-one relationship with both the User model and the Post model. The model includes fields for the comment owner, the post being commented on, creation and update timestamps, and the comment content. Users can engage in discussions, share their thoughts, and interact with other users' posts through comments.

These data models provide the foundation for storing and organizing the relevant information in your app, enabling users to create profiles, share posts, interact with other users and locations, and engage in conversations.

- __Bugs__

  - As i was doing my project I encoutered many bugs, i didn't know how complex would this be to make and as i work on logic it became more and more complex so i often made errors in logic or improperly used functions or methods, often string with numbers misplaced and forever shearched where and what went wrong 
           
  - Whenn i was first done with the app i hade two functions with approx. 150 lines of code, it took a big chunk of my time tring to make my code "atomic"

  - I initially created one model to handle both followers and follow_locations. However, I found it to be complicated to work with the data properly when both functionalities were combined in one model. As a result, I decided to create two separate models for followers and follow_locations. This approach has proven to be more manageable, allowing for clearer data organization and smoother implementation of the desired functionalities.


- __Deployment__

  Steps for deployment:
             
  - Fork or clone this repository
  - Create new Heroku app
  - Set the buildbacks to Python and Node.JS in that order
  - Link the Heroku app to repository
  - Click on Deploy

- __Testing__

  I have manually tested this project by doing following:

  - Passed code throught PEP8 liner and confirmed there are no problems.
            
  - Given invalid inputs: strings when numbers are expected or out of bounds inputs

  - Tested in my local terminal and the code intitute Heroku terminal



`Poker`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Create Profile | create Profile| Tryed to create profile | Profile created | Pass |
| Create Post| create post, upload mage set location | Post displayed on page | Post created| Pass |
| Like Post | Like posts | Liked one selected post | Instace of like created | Pass |
| Comment Post | Leave comment on post | Wrote comment | comment displayed | Pass |
| Location created | On post creation location creates automaticly | Post created| location created | Pass |
| Follow user | Sellect user to follow | Follow displayed| Follow displayed | Pass |
| Follow location| Sellect location to follow  | pFollow displayed | Follow displaye | Pass |

I confirmed that the form works: requires entries in every field, will only accept number in the inpput field, and the errors work properly.



## Credits 

- Stack Overflow, YouTube, and other online resources have been invaluable in my development process. I have utilized code snippets and logic found on these platforms and tailored them to meet the specific requirements of my project. Adapting and customizing the code to fit my needs has allowed me to implement desired features effectively and efficiently. However, it's important to ensure compliance with licenses, copyrights, and attribution requirements associated with the resources used. I have taken care to review and adhere to any guidelines or obligations outlined by the authors or platforms. Thorough testing and validation have been conducted to ensure that the adjusted code works seamlessly within my project.

### Content 

- Code institute for deployment terminal     
- Stack overflow on numerous occasions. I looked all the time how have others solved problems as mine, which methods did they use and did we have the same or different logic for the same problems.  
- Wikipedia for the details of the Poker game



