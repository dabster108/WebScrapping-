# import requests


# def fetchAndSave(url, path):
#     r = requests.get(url)
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(r.text)

# url = "https://timesofindia.indiatimes.com/india/delhi"

# fetchAndSave(url, "data/times.html")


from bs4 import BeautifulSoup   
with open('home.html' , 'r') as html_file:
    content = html_file.read()



    soup = BeautifulSoup(content , 'lxml')
    courses_card = soup.find_all('div', class_ = 'card')
    for course in courses_card:
        #print(course)   all the tags associated with the class card 
        course_name = course.h5.text
        course_price = course.a.text

        # print(course_name)
        # print(course_price)

        print(f'{course_name} costs {course_price}')

    










    # soup = BeautifulSoup(content , 'lxml')
    # print(soup.prettify())

     # finds the first h5 element 
     #findall - all the elements included with h5 tags 
    # tags = soup.findAll('h5') 
    # print(tags)

    # courses_tags = soup.findAll('h5')
    # for courses in courses_tags: 
    #     print(courses.text)

    
   