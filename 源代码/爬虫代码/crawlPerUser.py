from selenium import webdriver
from time import sleep
import json


# Initialize WebDriver
chrome_path = "./chromedriver" 
driver = webdriver.Chrome(executable_path = chrome_path)


# User ID List, generated through "generateUserID.py"
userList = [4537274, 75500504, 101577158, 9454533, 310670736, 293502404, 271692172, 401634242, 4716997, 258563401, 24385162, 391675776, 30852872, 283166474, 1192874383, 375149183, 401525779, 25587862, 226652311, 21914521, 31573915, 189529758, 514719, 43618467, 156723238, 317402919, 325035047, 17230633, 378519724, 375767726, 245507503, 321172656, 502313777, 23539887, 443919027, 294131763, 105160497, 8965686, 271177404, 35524158, 21278782, 43893696, 67233855, 686537540, 23838954, 245615817, 11996748, 160112078, 207347408, 425563089, 41683, 1810779476, 102315735, 481474138, 96650973, 94298079, 21712095, 16649057, 29317217, 441658210, 31114086, 313360363, 687595, 35836017, 690077810, 260987772, 16505725, 93872895, 31187483, 38351330, 122879, 102847230, 1897164216, 254463269, 378885845, 2200736, 585267, 371846699, 17819768, 285499073, 5294454, 433351, 21837784, 29329085, 375375, 72270557, 335573502, 498854705, 10874201, 3353026, 5689319, 25422790, 16720403, 25150941, 9824766, 43222001, 16794231, 12884177, 3766866, 1740850, 290728428, 163637592, 10416354, 317748513, 519872016, 403071811, 370415317, 79061224, 19255217, 517327498, 1177893348, 18202105, 15982391, 927587, 27756469, 7487399, 414641554, 59905809, 1532165, 5293668, 454719565, 515993, 23604445, 648113003, 472008134, 1958342, 3066511, 7788379, 452309333, 94281836, 10583143, 470156882, 5970160, 10119428, 673376925, 130997374, 116683, 16539048, 434832742, 37663924, 26240675, 238638655, 326246517, 31770382, 35095918, 62540916, 381374122, 2920960, 4474705, 345630501, 369750017, 26139491, 590490400, 1411030667, 6574487, 604003146, 4162287, 176037767, 450595813, 596324576, 79577853, 415479453, 2403047, 7792521, 488660572, 17409016, 3682229, 284120, 11870568, 9008159, 401516364, 237221399, 23340150, 400045435, 1463028352, 131732311, 19130415, 547889237, 48421904, 383444910, 8237763, 2679304, 24091560, 17134369, 1836322665, 385315631, 413748120, 30954515, 513532724, 454803876, 448436523, 566258416, 52079756, 1467772, 5848380, 21621895, 55775966, 327357792, 2303935, 170066477, 9344767, 20563366, 15377173, 43830802, 4957245, 36834263, 12175208, 2021519045, 474390659, 702946333, 31225950, 627605168, 669334488, 1304116, 440773030, 7435683, 2422052, 15940002, 628288620, 10294085, 543245410, 687830387, 288126180, 631255225, 14599980, 18462992, 624243924, 294702783, 279219712, 2041413426, 475661467, 84073684, 53614060, 475632235, 8066835, 507961306, 38983453, 483784677, 1815704886, 483162496, 669888703, 391762036, 37974444, 12890453, 384087053, 4127596, 627576351, 434346657, 396812396, 106197873]

# with open("bilibili1.txt", 'w') as fprint:

for userCount in range(1, 251): # 250 users
    userID = userList[userCount - 1]
    url = 'https://space.bilibili.com/' + str(userID) + '/video'
    
    driver.get(url)
    sleep(3)

    userName = driver.find_element_by_css_selector('#h-name').text
    userDescription = driver.find_element_by_css_selector('#app > div.h > div.wrapper > div.h-inner > div.h-user > div > div.h-basic > div.h-basic-spacing > h4').text
    userFan = driver.find_element_by_css_selector('#n-fs').text

    userPicture = driver.find_element_by_css_selector('#h-avatar').get_attribute('src')

    userData = {"username": userName, "userlink": url, "userdescription": userDescription, "userfan": userFan, "userpicture": userPicture}
    allMovieData = []
    totalData = {"username": userName, "userlink": url, "userdescription": userDescription,\
                 "userfan": userFan, "userpicture": userPicture, "movies": allMovieData}

    driver.find_element_by_css_selector('#page-video > div > div.main-content > div.row.page-head.clearfix > div.page-head__left > div > ul > li:nth-child(2) > input').click()
    sleep(1)
    
    # Movies
    movieLinkList = []
    moviePictureList = []
    
    for movieCount in range(1, 21):
        movieElement = driver.find_element_by_css_selector(f"#submit-video-list > ul.clearfix.cube-list > li:nth-child({movieCount})")
        movieLinkList.append(movieElement.find_element_by_tag_name('a').get_attribute('href'))
        moviePictureList.append(movieElement.find_element_by_tag_name('img').get_attribute('src'))

    for movieCount in range(1, 21):
        # Comments
        movieLink = movieLinkList[movieCount - 1]
        moviePicture = moviePictureList[movieCount - 1]
        driver.get(movieLink)
        sleep(4)

        # Skip bug movies
        if driver.find_elements_by_css_selector('#viewbox_report > h1 > span') == []:
            print(f"userID: {userID}, movieLink: {movieLink}")
            continue
        
        movieName = driver.find_element_by_css_selector('#viewbox_report > h1 > span').text
        movieDescription = driver.find_element_by_css_selector('#v_desc > div.desc-info.desc-v2 > span').text
        viewData = driver.find_element_by_css_selector('#viewbox_report > div > span.view').text.replace('\xa0', '').replace('·', '').replace(' ', '')
        popData = driver.find_element_by_css_selector('#viewbox_report > div > span.dm').text
        dateData = driver.find_element_by_css_selector('#viewbox_report > div > span:nth-child(3)').text
        likeInfo = driver.find_element_by_css_selector('#arc_toolbar_report > div.ops > span.like').text.replace('\n', '').replace(' ', '')
        coinInfo = driver.find_element_by_css_selector('#arc_toolbar_report > div.ops > span.coin').text.replace('\n', '').replace(' ', '')
        collectInfo = driver.find_element_by_css_selector('#arc_toolbar_report > div.ops > span.collect').text.replace('\n', '').replace(' ', '')
        shareInfo = driver.find_element_by_css_selector('#arc_toolbar_report > div.ops > span.share').text.replace('\n', '').replace(' ', '')
        
        driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
        sleep(2)

        driver.execute_script('window.scrollBy(0,1000)')
        sleep(2)

        commentElementList = driver.find_elements_by_css_selector('#comment > div > div.comment > div.bb-comment > div.comment-list > div > div.con > p')
        commentList = []
        for i in range(0, min(5, len(commentElementList))):
            comment = commentElementList[i].text.replace('�', '')
            commentList.append(comment)

        movieData = {}
        movieData = {"moviename": movieName, "movielink": movieLink, "moviedescription": movieDescription, \
                     "moviepicture": moviePicture, "movieview": viewData, "moviepop": popData, "moviedate": dateData, \
                     "movielike": likeInfo, "moviecoin": coinInfo, "moviecollect": collectInfo, "shareInfo": shareInfo, \
                     "moviecomment": commentList}
        allMovieData.append({"moviename": movieName, "movielink": movieLink, "moviedescription": movieDescription, \
                     "moviepicture": moviePicture, "movieview": viewData, "moviepop": popData, "moviedate": dateData, \
                     "movielike": likeInfo, "moviecoin": coinInfo, "moviecollect": collectInfo, "shareInfo": shareInfo, \
                     "moviecomment": commentList})
        movieData.update(userData)
        
        with open(f"mov{str(userCount).rjust(3, '0')}{str(movieCount).rjust(2, '0')}.json", 'w') as fmovie:
            json.dump(movieData, fmovie, ensure_ascii=False)
    
    with open(f"user{str(userCount).rjust(3, '0')}.json", 'w') as fuser:
        json.dump(totalData, fuser, ensure_ascii=False)
            
driver.quit()
