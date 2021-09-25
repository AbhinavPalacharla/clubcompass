Clubcompass is a website created to facilitate club signups at my highschool.
For the backend we used Flask because of how lightweight and responsive it is
For the serverside architecture we used 4 flask containers, 1 nginx loadbalancer with a round robin algorithm to equally distribute load, and 1 mongodb database container.
The frontend was done in pure HTML and CSS to maintain a lightweight experience. Additionally the website is completely responsive.
