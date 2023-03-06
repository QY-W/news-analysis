## News Sentimental Analysis 
1.  **Install instruction:**
	-   Frontend:  Install package and deploy Vue 
		```npm install ```
	-  Backend:    Active python virtual enviroment in backend folder and install necessary packages

		```
		 .\venv\Scripts\activate & activate flask & python app.py
		```
	 
2.  **Framework used  :** 
	- Frontend: Vue
	- Backend:  Flask (Python)
	- Database: MongoDB
4.  **Feature Description  (50 Points):**
    -   _**News Function:**_
		- 10: Data fetched from Guardian API, parse json and display news title, link, content and related information
		- 5:  User can search news
		- 5: Search result can be displayed in newest/oldest/relevence order
		- 5: Trending news can be displayed
		- 10: User can register, login and logout
    -   _**Text Analysis:**_
		- 10: LDA topic modeling carried through pyLDA dashboard, and sentimenel analysis are displayed with each news detail page 
			## [Implmentation Details and Visualization about LDA can be found in my NLP Machine Learning project](https://github.com/QY-W/Comments_NLP_Classification)
		- 5: word cloud, word frequency are displayed with each news detail page 
		
    -   _**Creative Portion:**_
		- 10: MongoDB
		- 5: search result further filter from and to date
		- 5: color palette
	   -   _**Best Practices :**_
	       -   Code is well formatted and easy to read, with proper commenting (2 points)
	       -   Code passes HTML validation (2 points)
	       -   node_modules folder is ignored by version control (1 points)
	   -   _**Usability:**_
	       -   Communicating with others and joining rooms is easy and intuitive (4 points)
	       -   Site is visually appealing (1 point)
